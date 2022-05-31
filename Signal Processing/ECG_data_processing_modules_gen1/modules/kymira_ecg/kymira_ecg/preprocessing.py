"""
Performs the basic filtering (Part I) and noise-reduction (Part II)
on the ecg data received from garment embedded ecg sensors.

This module expects ecg data in the standard JSON data format agreed for the multi-sensor smart garment.
This current version of the module is not designed to deal with missing data samples.

:author: Athanasios Anastasiou
:author: Min Yuan Chang
:author: DR. S. Chakraborty
:author: Sophie Charlwood
:date: Fri Jul 17 16:29:08 2020
"""

# from matplotlib import pyplot as plt
from datetime import datetime
from time import mktime
import numpy
from scipy import signal
from scipy.signal import find_peaks
import scipy.stats.mstats as stats
import copy
import pywt

from sklearn.decomposition import FastICA as fastica  # noqa N183
import scipy

# Constant variables and default values
#SEGMENT_LENGTH=

# Part I: Clean ecg data

def clean_data(ecg_data, segment_length=None, plot=None):
    data=copy.deepcopy(ecg_data)
    
    col_names=data.columns
    cleaned_data = data
    data_length=len(data)
    
    if segment_length==None:
        segment_length=SEGMENT_LENGTH
    
    for i in range(0,data_length-segment_length,segment_length):
    
        for col in col_names:
            if 'tstamp' not in col:
                #data=ecg_data[col]
                data_1channel=data[col][i:i+segment_length]
                data_indices=data_1channel.index # All indices
            
                data_std=data_1channel.std()
                data_median=data_1channel.median()
    
                low_th=data_median-3*data_std
                high_th=data_median+3*data_std
            
                good_data=data[(data[col]>=low_th) & (data[col]<=high_th)]
       
                good_data_values = good_data[col]
                good_data_indices = good_data.index  # Indices with finite values
        

                f_finite = scipy.interpolate.interp1d(good_data_indices, good_data_values, fill_value='extrapolate') #  interp1d    extrapolate=True
                s_interp = f_finite(data_indices)


                cleaned_data[col][i:i+segment_length]=s_interp
            
    if plot !=None:
        print('Plotting data ...')
        plt.figure('Clean data')
        num_cols=len(col_names)
        count=0;
        for i in range(num_cols):
            if 'tstamp' not in col_names[i]:
                count+=1
                plt.subplot(num_cols-1,1,count)
                plt.plot(ecg_data[col_names[i]])
                plt.plot(cleaned_data[col_names[i]])
                plt.legend(['Raw data', 'Cleaned data'])


    return cleaned_data


def notch_filtering(time_series, f_notch=50, q_factor=5, fs=500):
    """
    Apply a notch filter to isolate specific components.

    :param time_series: Time series of values to be filtered.
    :type time_series: numpy.array
    :param f_notch: Notch filter frequency (Hertz)
    :type f_notch: float
    :param q_factor: Selectivity of the notch filter
    :type q_factor: float
    :param fs: Sampling frequency (Hz)
    :type fs: float
    """
    # Build the notch filter to get rid of the 50Hz contamination
    c_b, c_a = scipy.signal.iirnotch(f_notch, q_factor, fs=fs)
    return scipy.signal.lfilter(c_b, c_a, time_series)


def butterworth_bandpass_filtering(time_series, f_lowcut, f_highcut, order, fs):
    """
    Bandpass filtering.

    :param time_series: Unfiltered ECG data
    :type time_series: pandas.DataFrame
    :param f_lowcut: Low frequency cut off point
    :type f_lowcut: float
    :param f_highcut: High frequency cut off point
    :type f_highcut: float
    :param fs: Sampling frequency
    :type fs: float
    :param order: Order of the filter
    :type order: unsigned int

    :returns: Filtered ECG data.
    """
    nyq = 0.5 * fs
    low = f_lowcut / nyq
    high = f_highcut / nyq

    b, a = scipy.signal.butter(order, [low, high], btype='bandpass')
    return signal.filtfilt(b, a, time_series)


def moving_average_lowpass_filtering(time_series, order):
    """
    Applies a very simple moving average filter.

    :param time_series: An individual ECG Time Series
    :type time_series: numpy.array.
    :param order: The order of the FIR filter (ideally an odd integer).
    :type order: int
    """
    coeffs_ma = numpy.ones((order,)) / order
    return scipy.signal.convolve(time_series, coeffs_ma, mode="same")


def wavelet_denoising(time_series, wavelet_name="sym8", denoise_level=0.004):
    """
    Denoises a time series using wavelet decomposition.

    Notes:
        * Uses sym8
        * Applies hard thresholding
        * The threshold was empirically derived

    :param time_series: A Kymira ECG object (Tuple of (fs, pandas.DataFrame))
    :type time_series: tuple
    :param wavelet_name: See https://pywavelets.readthedocs.io/en/latest/ref/wavelets.html#built-in-wavelets-wavelist
    :type wavelet_name: str
    :param denoise_level: The strength of denoising. This is the coefficient that scales the wavelet decomposition
                          coefficients.
    :type denoise_level: float
    :returns: The denoised time series.
    :rtype: numpy.array
    """
    # Input signal
    sig = copy.deepcopy(time_series)
    w = pywt.Wavelet(wavelet_name)
    # TODO: HIGH, probably worth having a fixed max level decomposition here.
    maxlev = pywt.dwt_max_level(len(sig), w.dec_len)
    # Decompose
    coeffs = pywt.wavedec(sig, wavelet_name, level=maxlev)
    # Apply threshold
    for i in range(1, len(coeffs)):
        coeffs[i] = pywt.threshold(coeffs[i], denoise_level * max(coeffs[i]))
    # Recompose
    sig_rec = pywt.waverec(coeffs, wavelet_name)
    return sig_rec


def spectral_flatness(time_series, window_length, f_high_cutoff, fs):
    """
    Estimates the spectral flatness of a time series.

    Notes:
        * The spectral flatness operates over vectors (e.g. kymira_ecg[0]) assuming that the tstmp does not contain
          gaps.
        * Estimates the spectral flatness as the "similarity" between the geometric and arithmetic means.

    :param time_series: A vector of float values.
    :type time_series: numpy.array
    :param window_length:
    :type window_length:
    :param f_high_cutoff:
    :type f_high_cutoff:
    :param fs:
    :type fs:
    
    :returns: An estimate of the spectral flattness given the time_series
    :rtype: float

    :returns: The spectral flatness of the time series.
    :rtype: float
    """
    # TODO: HIGH, Clarify detrending here (there is a separate detrending module that can do more than take out a simple linear detrending.
    # scipy.signal.detrend(kymira_ecg)
    # ic_sqrd = []
    # for i in single_lead_data:
    #     ic_sqrd.append(i**2)
    # rms = np.sqrt(np.mean(ic_sqrd))

    # Normalise the vector
    normalised_ic = copy.deepcopy(time_series)
    normalised_ic = normalised_ic / numpy.std(normalised_ic)

    # TODO: HIGH, Quantities FS, WINDOW_LENGTH, H_CUTOFF should be parameters to this function.
    # Get the spectrum.
    freq, psd = scipy.signal.welch(normalised_ic, fs=fs, nperseg=window_length, detrend='linear')

    # Estimate the spectral flatness over a specific frequency range.
    # TODO: HIGH, Do this with proper indexing
    comb_list = list(zip(freq.tolist(), psd.tolist()))
    rang_psd = []
    for i, j in comb_list:
        if i <= f_high_cutoff:
            rang_psd.append(j)
    # Flatness as a metric of how well the arithmetic and geometric means agree.
    a_mean = numpy.mean(rang_psd)
    g_mean = stats.gmean(rang_psd)
    return g_mean / a_mean


def peak_variance(time_series):
    """
    Estimates peak variance.

    Notes:
        * "Peak Variance" refers to the time domain ECG (**NOT THE SPECTRUM**)

    :param time_series: A timeseries to estimate the peak variance over (Typically one of the channels of kymira_ecg).
    :type time_series: numpy.array
    """
    # TODO: HIGH, PERCENTILE should really become a parameter to this function.
    rectified_timeseries = copy.deepcopy(time_series)
    rectified_timeseries = numpy.abs(time_series)
    threshold_value = numpy.percentile(rectified_timeseries, PERCENTILE)

    # TODO: HIGH, Clarify what is DISTANCE (?) and make it a parameter to this function
    # peaks, _ = find_peaks(rectified_array, height=threshold_value, distance=DISTANCE)
    peak_locs, _ = find_peaks(rectified_timeseries, height=threshold_value)
    return numpy.var(numpy.diff(peak_locs))


def ica_fastica(filtered_ecg, leads_to_be_used=None, plot=None):
    """
    Performs fastICA on bandpass filtered ECG

    :param filtered_ecg: Filtered ECG data
    :type filtered_ecg: pandas.DataFrame
    :param leads_to_be_used: List of channels to use during fastica.
    :type leads_to_be_used: list
    :returns: ICA Processed ECG data
    :rtype: pandas.DataFrame
    """

    noise_reduced_ecg = copy.deepcopy(filtered_ecg)

    data_length = len(filtered_ecg)
    keys = filtered_ecg[0].keys()
    if leads_to_be_used == None and data_length != 0:
        leads_to_be_used = []
        for key in keys:
            if 'tstamp' not in key:
                leads_to_be_used += [key]

    num_of_leads = len(leads_to_be_used)
    if num_of_leads <= 1: print('Need atleast two lead data')
    mixed_signals = numpy.zeros((data_length, num_of_leads))

    lead_number = 0
    for lead in leads_to_be_used:
        for sample in range(data_length):
            mixed_signals[sample, lead_number] = filtered_ecg[sample][lead]
        lead_number += 1

    ica = fastica(n_components=num_of_leads, whiten=True, random_state=0)
    source_signals = ica.fit_transform(mixed_signals)  # Reconstruct signal/independent sources
    mixing_matrix = ica.mixing_  # Estimated mixing signal
    # W = np.linalg.inv(mixing_matrix)           # Inverse of mixing signal, demixing matrix
    # Y = np.matmul(mixing_matrix,mixed_signals.T)            # Independent components

    scaled_sources = []
    count = 0
    for lead in leads_to_be_used:
        count += 1
        if count == 1:
            ic = [source_signals[i, count - 1] for i in range(data_length)]
            # print('IC '+str(count))
            sf = spectral_flatness(ic)

            if sf < SF_THRESH:
                var = peak_variance(ic)
                # print('peak variance= '+str(var))
                if PV_THRESH_L < var < PV_THRESH_H:
                    scaled_sources.append(ic)

                else:
                    print('IC' + str(count) + ' is noise (PV=' + str(var) + ')')
                    s_down = scale_down(ic)
                    scaled_sources.append(s_down)

            else:
                print('IC' + str(count) + ' is noise (sf=' + str(sf) + ')')
                s_down = scale_down(ic)
                scaled_sources.append(s_down)
        else:
            ic = [source_signals[i, count - 1] for i in range(data_length)]
            # print('IC '+str(count))
            sf = spectral_flatness(ic)

            if sf < SF_THRESH:
                var = peak_variance(ic)
                # print('peak variance= '+str(var))
                if PV_THRESH_L < var < PV_THRESH_H:
                    scaled_sources.append(ic)

                else:
                    print('IC' + str(count) + ' is noise (PV=' + str(var) + ')')
                    s_down = scale_down(ic)
                    scaled_sources.append(s_down)

            else:
                print('IC' + str(count) + ' is noise (sf=' + str(sf) + ')')
                s_down = scale_down(ic)
                scaled_sources.append(s_down)

    scaled_components = numpy.vstack(scaled_sources)
    noise_reduced_ecg_array = numpy.matmul(mixing_matrix, scaled_components)

    lead_number = 0
    for lead in leads_to_be_used:
        # print('Lead name: '+lead+' Lead number: '+str(lead_number))
        for sample in range(data_length):
            noise_reduced_ecg[sample][lead] = noise_reduced_ecg_array[lead_number, sample]
        lead_number += 1

    # for key in keys:
    #     if key not in leads_to_be_used:
    #         if key =='ecg3':
    #             lead1=[noise_reduced_ecg[i]['ecg1'] for i in range(data_length)]
    #             lead2=[noise_reduced_ecg[i]['ecg2'] for i in range(data_length)]
    #             for sample in range(data_length):
    #                 noise_reduced_ecg[sample]['ecg3']=lead2[sample]-lead1[sample]

    # if plot != None:
    #     fig = plt.figure('Data and components')
    #     count2 = 0
    #     lead_count = 0
    #     for lead in leads_to_be_used:
    #         count2 += 1
    #         ecg_data = [filtered_ecg[i][lead] for i in range(data_length)]
    #         # source_sig=[source_signals[i][lead_count] for i in range(data_length)]
    #         if count2 == 1:
    #             axs1 = fig.add_subplot(num_of_leads, 2, 2 * count2 - 1)
    #             axs1.plot(ecg_data)
    #             # axs1.plot(source_sig)
    #             plt.legend([lead])
    #
    #             y_signal = noise_reduced_ecg_array[lead_count, :]
    #             axs = fig.add_subplot(num_of_leads, 2, 2 * count2)
    #             axs.plot(y_signal)
    #
    #             lead_count += 1
    #
    #         else:
    #             axs = fig.add_subplot(num_of_leads, 2, 2 * count2 - 1, sharex=axs1)
    #             axs.plot(ecg_data)
    #             # axs.plot(source_sig)
    #             plt.legend([lead])
    #
    #             y_signal = noise_reduced_ecg_array[lead_count, :]
    #             axs = fig.add_subplot(num_of_leads, 2, 2 * count2)
    #             axs.plot(y_signal)
    #
    #             lead_count += 1

    # return noise_reduced_ecg, source_signals
    return noise_reduced_ecg


def scale_down(ic):
    scale_ic_down = numpy.where(ic != float(0), 0, ic)
    return scale_ic_down


# # To be used for offline module debugging purposes
# def seg_analysis(ecg_data, seg_length=None, leads_to_be_used=None):
#     clean_ecg_data = copy.deepcopy(ecg_data)
#     data_length = len(ecg_data)
#     keys = ecg_data[0].keys()
#
#     if seg_length == None:
#         seg_length = 5 * FS  # Default segment length is 5s long data
#
#     if leads_to_be_used == None and data_length != 0:
#         leads_to_be_used = []
#         for key in keys:
#             if 'tstamp' not in key:
#                 leads_to_be_used += [key]
#     num_of_leads = len(leads_to_be_used)
#     seg_count = 0
#
#     for sample in range(0, data_length - seg_length, FS):
#         seg_count += 1
#
#         data_seg = [ecg_data[i] for i in range(sample, sample + seg_length)]
#         # print('Segment num: '+str(seg_count)+ ';  Segment length: '+ str(len(data_seg)))
#         fil_sig = filter_ecg_data(data_seg)
#         clean_sig, _ = ica_fastica(fil_sig)
#
#         for elem in range(seg_length - FS, seg_length):
#             clean_ecg_data[sample + elem] = clean_sig[elem]
#
#         del fil_sig, clean_sig
#
#     # if plot != None:
#     #     fig = plt.figure('Data and components')
#     #     count2 = 0
#     #     lead_count = 0
#     #     for lead in leads_to_be_used:
#     #         count2 += 1
#     #         data = [ecg_data[i][lead] for i in range(data_length)]
#     #         # source_sig=[source_signals[i][lead_count] for i in range(data_length)]
#     #         if count2 == 1:  # i.e. first lead
#     #             axs1 = fig.add_subplot(num_of_leads, 2, 2 * count2 - 1)
#     #             axs1.plot(data)
#     #             # axs1.plot(source_sig)
#     #             plt.legend([lead])
#     #
#     #             clean_data = [clean_ecg_data[i][lead] for i in range(data_length)]
#     #             axs = fig.add_subplot(num_of_leads, 2, 2 * count2)
#     #             axs.plot(clean_data)
#     #
#     #             lead_count += 1
#     #
#     #         else:
#     #             axs = fig.add_subplot(num_of_leads, 2, 2 * count2 - 1, sharex=axs1)
#     #             axs.plot(data)
#     #             # axs.plot(source_sig)
#     #             plt.legend([lead])
#     #
#     #             clean_data = [clean_ecg_data[i][lead] for i in range(data_length)]
#     #             axs = fig.add_subplot(num_of_leads, 2, 2 * count2)
#     #             axs.plot(clean_data)
#     #
#     #             lead_count += 1
#     return clean_ecg_data


# Part III: Lead Extraction (Karl)

def get_extra_leads(ecg_list):
    # Extract Lead III and augmented leads from I and II (post processing / so that ECG trace conforms to what is expected from those leads.
    #    
    # Input:
    #   ecg_list(): list of 'n' dictionaries. n= number of samples.
    #                          Each dictionary element containing 
    #                          'm' key-values pairs of filtered (m)ecg lead data + time stamp
    # Output:
    #   ecg_list(): list of 'n' dictionaries. n= number of samples.
    #                          Each dictionary element containing the two leads that were in
    #                          the input plus lead III and the augmented leads aVR, aVL, aVF
    #
    augmented_list = []
    for sample in ecg_list:
        new_sample = {}

        # set leads I and II, common to all sensor configurations

        new_sample['ecg1'] = sample['ecg1']
        new_sample['ecg2'] = sample['ecg2']

        # check if this is a 3 lead or a 6 lead setup

        if ('ecg5' not in sample.keys()):  # if we are a 3 lead, check if lead 3 exists
            if ('ecg3' in sample.keys()):
                new_sample['ecg3'] = sample['ecg3']
            else:  # if not, derive it
                new_sample['ecg3'] = sample['ecg2'] - sample['ecg1']
        else:
            if 'ecg6' in sample.keys():  # else check if we have 6 physical leads
                new_sample['ecg3'] = sample['ecg3']
                new_sample['ecgV1'] = sample['ecg4']
                new_sample['ecgV3'] = sample['ecg5']
                new_sample['ecgV6'] = sample['ecg6']
            else:  # noqa: E125
                new_sample['ecg3'] = sample['ecg2'] - sample['ecg1']
                new_sample['ecgV1'] = sample['ecg3']
                new_sample['ecgV3'] = sample['ecg4']
                new_sample['ecgV6'] = sample['ecg5']

        # finally, derive the augmented leads
        new_sample['ecgaVR'] = -(sample['ecg1'] + sample['ecg2']) / 2
        new_sample['ecgaVL'] = (sample['ecg1'] - new_sample['ecg3']) / 2
        new_sample['ecgaVF'] = (sample['ecg2'] + new_sample['ecg3']) / 2

        augmented_list += [new_sample]
    return augmented_list


def process_6lead(ecg_list):
    # Extract Lead III and augmented leads from I and II
    #    
    # Input:
    #   ecg_list(): list of 'n' dictionaries. n= number of samples.
    #                          Each dictionary element containing 
    #                          'm' key-values pairs of filtered (m)ecg lead data + time stamp
    # Output:
    #   ecg_list(): list of 'n' dictionaries. n= number of samples.
    #                          Each dictionary element containing the two leads that were in
    #                          the input plus lead III and the augmented leads aVR, aVL, aVF
    #
    augmented_list = []
    for sample in ecg_list:
        new_sample = {}
        new_sample['ecg1'] = sample['ecg1']
        new_sample['ecg2'] = sample['ecg2']
        new_sample['ecg3'] = sample['ecg2'] - sample['ecg1']
        new_sample['ecgaVR'] = sample['ecg3']
        new_sample['ecgaVL'] = sample['ecg4']
        new_sample['ecgaVF'] = sample['ecg5']
        augmented_list += [new_sample]
    return augmented_list


def raw_to_ecg(value):
    ADC_MAX = 0xF30000
    V_REF = 2.4
    raw_value = value / ADC_MAX
    raw_value = raw_value - 0.5
    raw_value = raw_value * V_REF * 2
    out_value = raw_value / 3.5
    return out_value


def denoise_ecg_trial(an_ecg_object, channels=None):
    """
    Denoises an ecg object (or selected channels of it) using wavelet decomposition.

    Notes:
        * Uses sym8
        * Applies hard thresholding
        * The threshold was empirically derived

    :param an_ecg_object: A Kymira ECG object (Tuple of (fs, pandas.DataFrame))
    :type an_ecg_object: tuple
    :param channels: Which channels to apply the denoising on (if required)
    :type channels: list
    :return: The processed Kymira object.
    :rtype: tuple
    """
    d = copy.deepcopy(an_ecg_object)

    if channels is not None:
        channels_to_process = channels
    else:
        channels_to_process = list(range(1, 6))
    # TODO: HIGH, Raise exception here if channels is simply empty ([]). there should be at least one channel plotted.

    channels_to_process = list(map(lambda x: f"ecg{x}", channels_to_process))

    for a_channel in channels_to_process:
        sig = d[a_channel].to_numpy()
        w = pywt.Wavelet("sym8")
        maxlev = pywt.dwt_max_level(len(sig), w.dec_len)
        coeffs = pywt.wavedec(sig, "sym8", level=maxlev)
        for i in range(1, len(coeffs)):
            coeffs[i] = pywt.threshold(coeffs[i], 0.004 * max(coeffs[i]))
        sig_rec = pywt.waverec(coeffs, "sym8")
        d[a_channel] = sig_rec

    return d


# def pre_process_ecg_trial(an_ecg_object, channels=None):
#     """
#     Applies some standard pre-processing to have as clean ECG signals as possible for subsequent processing stages.
#
#     :param an_ecg_object: A tuple of (Fs, pandas.DataFrame) as returned from ``read_ecg_trial``.
#     :type an_ecg_object: tuple
#     :param channels: A list of integers from 1 to 5 to plot only specific channels.
#     :type channels: int
#
#     :return: The processed ecg "object"
#     :rtype: tuple
#     """
#
#     d = copy.deepcopy(an_ecg_object)
#
#     # Build a band-pass filter to keep only the ECG frequency range.
#     # TODO: MID, Need error checking here in case the Fs is not high enough for the cut offs.
#     # TODO: MID, Need to make the order of the filter parametrisable.
#     coeffs_bp = firwin(131, [0.05, 125], fs=500, pass_zero=False)
#     # Build the moving average filter to get rid of the wandering baseline
#     # TODO: MID, Parametrise the order of the filter.
#     coeffs_ma = numpy.ones((511,)) / 511
#     # Build the notch filter to get rid of the 50Hz contamination
#     # TODO: MID, Parametrise the Q factor.
#     c_b, c_a = iirnotch(50, 5, fs=500)
#
#     if channels is not None:
#         channels_to_preprocess = channels
#     else:
#         channels_to_preprocess = list(range(1, 6))
#     # TODO: HIGH, Raise exception here if channels is simply empty ([]). there should be at least one channel plotted.
#
#     channels_to_preprocess = list(map(lambda x: f"ecg{x}", channels_to_preprocess))
#
#     for a_channel in channels_to_preprocess:
#         chan_signal = d[a_channel].to_numpy()
#         # Apply the 50Hz notch filter
#         chan_signal = lfilter(c_b, c_a, chan_signal)
#         # Apply the bandpass
#         chan_signal = convolve(chan_signal, coeffs_bp, mode="same")
#         # Apply a simple threshold to get rid of the spikes
#         # Limits are static and the result of visual overview
#         chan_signal[(chan_signal >= 0.005)] = 0.005
#         chan_signal[(chan_signal <= -0.005)] = -0.005
#
#         # Detrend the signal
#         # Filter the original signal
#         chan_signal_ma = convolve(chan_signal, coeffs_ma, mode="same")
#         # Get the detrended signal
#         chan_signal = chan_signal - chan_signal_ma
#         d[a_channel] = chan_signal
#
#     return d

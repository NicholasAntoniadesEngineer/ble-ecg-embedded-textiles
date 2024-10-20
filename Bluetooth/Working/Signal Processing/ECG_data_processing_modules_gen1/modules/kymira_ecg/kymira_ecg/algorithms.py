"""
Calls WTdelineator to perform a wavelet based ECG delineation (identify the individual component waves P,
QRS-complex and T waves)  from a chosen single-lead ECG data to estimate a set of 6 basic parameters  that characterize
the heart beat.

:author: Ms. Min Yuan Chang
:author: DR. S. Chakraborty
:date: Mon Jul 27 11:00:51 2020
"""

import kymira_ecg.WTdelineator as wtd
import numpy as np

SAMPLING_FRQ = 500  # Hz
CHOSEN_LEAD = 'ecg2'

ECG_parameters = {}


def ecg_data_processing(ecg_data):
    """
    Processes a data segment and returns a set of estimates about it.

    :param ecg_data: Dataframe of ECG data.
    :type ecg_data: pandas.DataFrame

    :returns: A dictionary variable consisting of following  13 key value pairs
              * P_start(list): data samples at which P-waves begin
              * P_end(list): data samples at which P-waves end
              * QRS_start(list): data samples at which QRS-complexes begin
              * QRS_end(list): data samples at which QRS-complexes end
              * R_peak_loc(list): all the R-peak locations
              * T_start(list): data samples at which T-waves begin
              * T_end(list): data samples at which T-waves end
    
              * heart_rate(float): Number of heartbeats per minutes
              * hrv(float): root mean square of successive differences between each heartbeat
              * QRS_duration(list): Widths of identified QRS-complexes
              * PR_interval(list): Periods from the beginning of each P wave until the beginning of the next
                QRS complex
              * QT_interval(list): Periods from the beginning of each Q wave to the end of the next T wave.
              * ST_segment(list): Periods from the end of each S wave and the beginning of the next T wave
    """

    fil_lead_I = [ecg_data[i][CHOSEN_LEAD] for i in range(len(ecg_data) - 1)]
    # time=[i/SAMPLING_FRQ for i in range(len(ECG_data))]

    [P, QRS, T] = wtd.signalDelineation(np.array(fil_lead_I), SAMPLING_FRQ)

    P_start = [P[i, 0] for i in range(len(P))]
    P_end = [P[i, 3] for i in range(len(P))]
    QRS_start = [QRS[i, 0] for i in range(len(QRS))]
    QRS_end = [QRS[i, 4] for i in range(len(QRS))]
    R_peak_locations = [QRS[i, 2] for i in range(len(QRS))]
    T_start = [T[i, 0] for i in range(len(T))]
    T_end = [T[i, 3] for i in range(len(T))]

    ECG_parameters['P_start'] = P_start
    ECG_parameters['P_end'] = P_end
    ECG_parameters['QRS_start'] = QRS_start
    ECG_parameters['QRS_end'] = QRS_end
    ECG_parameters['R_peak_loc'] = R_peak_locations
    ECG_parameters['T_start'] = T_start
    ECG_parameters['T_end'] = T_end

    hr = heart_rate_estimator(R_peak_locations, SAMPLING_FRQ)
    QRS_duration = QRS_duration_estimator(QRS_start, QRS_end, SAMPLING_FRQ)
    PR_interval = PR_interval_estimator(P_start, QRS_start, SAMPLING_FRQ)
    QT_interval = QT_interval_estimator(QRS_start, T_end, SAMPLING_FRQ)
    ST_segment = ST_segment_estimator(QRS_end, T_start, SAMPLING_FRQ)
    hrv = RMSSD(R_peak_locations, SAMPLING_FRQ)

    ECG_parameters['heart_rate'] = hr
    ECG_parameters['QRS_duration'] = QRS_duration
    ECG_parameters['PR_interval'] = PR_interval
    ECG_parameters['QT_interval'] = QT_interval
    ECG_parameters['ST_segment'] = ST_segment
    ECG_parameters['heart_rate_variability'] = hrv

    return ECG_parameters


def heart_rate_estimator(r_loc, fs):
    """
    Computes the heart rate.

    :param r_loc: Location of the R peaks
    :type r_loc: list
    :param fs: Sampling frequency
    :type fs: float

    :returns: Heart rate
    :rtype: float
    """

    rr = []
    for i in range(len(r_loc) - 1):
        if r_loc[i] != 0 and r_loc[i + 1] != 0 and r_loc[i + 1] > r_loc[i]:
            rr += [(r_loc[i + 1] - r_loc[i]) / fs * 1000]  # Difference between consecutive R peaks in ms
    hr = [60000 / rr[i] for i in range(len(rr))]  # number of rr intervals in 1 min (60000 ms)

    # To ensure each run outputs only one PR_interval estimate
    if len(hr) >= 2:
        hr = np.mean(hr)
    elif len(hr) == 0:
        hr = 0

    return hr


def QRS_duration_estimator(qrs_on, qrs_end, fs):
    """
    Computes the QRS duration.

    :param qrs_on: Locations of the onset of the QRS complex
    :type qrs_on: list
    :param qrs_end: Locations of the end of the QRS complex
    :type qrs_end: list
    :param fs:
    :type fs: float

    :returns: The QRS duration
    :rtype: float
    """

    QRS_duration = []
    for i in range(len(qrs_on)):
        if qrs_on[i] != 0 and qrs_end[i] != 0 and qrs_end[i] > qrs_on[i]:
            QRS_duration += [qrs_end[i] - qrs_on[i]]

    # To ensure each run outputs only one QRS_duration estimate
    if len(QRS_duration) >= 2:
        QRS_duration = np.mean(QRS_duration)
    elif len(QRS_duration) == 0:
        QRS_duration = 0
    else:
        QRS_duration = QRS_duration[0]

        # Change unit from sample to ms
    QRS_duration = (QRS_duration / fs) * 1000

    return QRS_duration


def PR_interval_estimator(p_on, qrs_on, fs):
    """
    Computes the PR interval.

    This is the period that extends from the beginning of the P wave until the beginning of the QRS complex.

    :param p_on: Location of the onsets of each P wave
    :type p_on: list
    :param qrs_on: Locations of the onsets of the QRS complexes
    :type qrs_on: list
    :param fs: Sampling frequency
    :type fs: float

    :returns: The PR interval
    :rtype: float
    """

    PR_interval = []
    for i in range(len(p_on)):
        if p_on[i] != 0 and qrs_on[i] != 0 and p_on[i] < qrs_on[i]:
            PR_interval += [qrs_on[i] - p_on[i]]

    # To ensure each run outputs only one QT_interval estimate
    if len(PR_interval) >= 2:
        PR_interval = np.mean(PR_interval)
    elif len(PR_interval) == 0:
        PR_interval = 0
    else:
        PR_interval = PR_interval[0]

        # Change unit from sample to ms
    PR_interval = (PR_interval / fs) * 1000

    return PR_interval


def QT_interval_estimator(qrs_on, t_end, fs):
    """
    Computes the QT interval.

    This is defined as the period from the start of the Q wave to the end of the T wave.

    :param qrs_on: Locations of the onsets of the QRS complexes
    :type qrs_on: list
    :param t_end: Locations of the end of each T wave
    :type t_end: list
    :param fs: Sampling frequency
    :type fs: float

    :returns: The QT interval
    :rtype: float
    """

    QT_interval = []
    for i in range(len(t_end)):
        if t_end[i] != 0 and qrs_on[i] != 0 and t_end[i] > qrs_on[i]:
            QT_interval += [t_end[i] - qrs_on[i]]

    # To ensure each run outputs only one QT_interval estimate
    if len(QT_interval) >= 2:
        QT_interval = np.mean(QT_interval)
    elif len(QT_interval) == 0:
        QT_interval = 0
    else:
        QT_interval = QT_interval[0]

        # Change unit from sample to ms
    QT_interval = (QT_interval / fs) * 1000

    return QT_interval


def ST_segment_estimator(qrs_end, t_on, fs):
    """
    Computes the ST segment.

    This is defined as the flat isoelectric section of the ECG between the end of the S wave and the beginning of
    the T wave.

    :param qrs_end: Locations of the end of the QRS complex.
    :type qrs_end: list
    :param t_on: Locaions of the onset of each T wave.
    :type t_on: list
    :param fs: Sampling frequency
    :type fs: float

    :returns: The ST segment
    :rtype: float
    """
    ST_segment = []
    for i in range(len(t_on)):
        if t_on[i] != 0 and qrs_end[i] != 0 and t_on[i] > qrs_end[i]:
            ST_segment += [t_on[i] - qrs_end[i]]

    # To ensure each run outputs only one ST_segment estimate
    if len(ST_segment) >= 2:
        ST_segment = np.mean(ST_segment)
    elif len(ST_segment) == 0:
        ST_segment = 0
    else:
        ST_segment = ST_segment[0]

        # Change unit from sample to ms
    ST_segment = (ST_segment / fs) * 1000

    return ST_segment


def RMSSD(R_loc, fs):
    """
    Computes the heart rate variability.

     Uses the time-domain method to compute the root mean square of successive differences between each heartbeat.

    :param r_loc: Location of the R peaks
    :type r_loc: list
    :param fs: Sampling Frequency
    :type fs: float

    :returns: The heart rate variability
    :rtype: float
    """

    if len(R_loc) >= 3:
        rr = []
        for i in range(len(R_loc) - 1):
            if R_loc[i] != 0 and R_loc[i + 1] != 0 and R_loc[i + 1] > R_loc[i]:
                rr += [(R_loc[i + 1] - R_loc[i]) / fs * 1000]  # Difference between consecutive R peaks in ms

        rr_diff = np.diff(rr)  # Difference between RR intervals
        rmssd = np.sqrt(np.mean(np.square(rr_diff)))
    else:
        rmssd = 0

    return rmssd

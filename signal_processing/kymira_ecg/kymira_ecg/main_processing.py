"""
Kymira_task code that remains to be merged to the main module.

:author: Athanasios Anastasiou
:date: Jan 2022
"""

# from descriptives import read_ecg_trial, plot_ecg_trial, pre_process_ecg_trial
# from matplotlib import pyplot as plt
# import pywt
# import copy
# import numpy


if __name__ == "__main__":
    # Point this a different directory to look at a different trial
    input_dir = "../data/"
    # Use this list as a "filter" to inlcude data files for a specific trial.
    input_files = ["Sitting_data.csv",
                   "stairs_normal_pace.csv",
                   "walking_normal_pace.csv",
                   "walking_fast_pace.csv", ]
    # Which file to focus the analysis on
    file_to_analyse = 0
    channel_to_focus_on = "ecg4"
    
    # Build the final filename
    input_file_name = f"{input_dir}{input_files[file_to_analyse]}"
    
    # Read the signal
    ecg_ob = read_ecg_trial(input_file_name)
    sig_before = ecg_ob[1][channel_to_focus_on].to_numpy()

    # Preprocess the signal to get rid of the common disturbances.
    ecg_ob = pre_process_ecg_trial(ecg_ob)
    # Plot before
    # plot_ecg_trial(ecg_ob, [2])
    # Denoise it
    ecg_ob = denoise_ecg_trial(ecg_ob)
    # Plot after
    # plot_ecg_trial(ecg_ob, [2])
    sig_after = ecg_ob[1][channel_to_focus_on].to_numpy()

    # Calculate the SNR vector (non-overlapping windows)

    N_SIG = len(sig_before)
    win_snr = []
    N_STRIDE = 500
    for k in range(0, len(sig_before), N_STRIDE):
        start_at = k
        end_at = k + N_STRIDE if k + N_STRIDE < N_SIG else N_SIG
        # Pads the vector with the same number which is the estimate across the window.
        win_snr.extend(numpy.ones((N_STRIDE,)) *
                       10 * numpy.log((numpy.sum(sig_after[start_at:end_at]**2)) /
                                      (numpy.sum((sig_after[start_at:end_at] -
                                                  sig_before[start_at:end_at])**2))))

    # Visualise the before, after (denoising) and the SNR vector.
    ax=plt.subplot(311)
    plt.plot(sig_before)
    plt.title(f"{channel_to_focus_on} - Before denoising")
    plt.xlabel("Time (Samples)")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.subplot(312, sharex=ax)
    plt.plot(sig_after)
    plt.title(f"{channel_to_focus_on} - After pre-processing & denoising")
    plt.xlabel("Time (Samples)")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.subplot(313, sharex=ax)
    plt.plot(win_snr)
    plt.title(f"{channel_to_focus_on} - SNR Vector (Higher is better)")
    plt.xlabel("Time (Samples)")
    plt.ylabel("SNR (dB)")
    plt.grid()
    plt.tight_layout()
    plt.show()
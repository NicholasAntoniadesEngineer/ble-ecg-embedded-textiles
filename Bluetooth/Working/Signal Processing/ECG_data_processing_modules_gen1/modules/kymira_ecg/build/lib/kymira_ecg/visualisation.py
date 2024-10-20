"""
Handles any visualisation required for depicting Kymira ECG signals using a variety of techniques and outputs.

:author: Athanasios Anastasiou
:date: Jan 2022
"""

# from matplotlib import pyplot as plt
# try:
#     import bokeh.io
#     import bokeh.plotting
#     import bokeh.layouts
# except ModuleNotFoundError:
#     # TODO: MID, this must be incorporated to the exception hierarchy.
#     #raise Exception("Module bokeh is not installed")
#     pass

import bokeh.io
import bokeh.plotting
import bokeh.layouts
import scipy.signal


def plot_ecg_matplotib(an_ecg_object, channels, ax, plot_time_freq):
    """
    Plots a Kymira dataset using matplotlib

    :param an_ecg_object: A tuple of (Fs, pandas.DataFrame) as returned from ``read_ecg_trial``.
    :type an_ecg_object: tuple
    :param ax: An optional axis to position the plots in.
    :type ax: matplotlib.Axis
    :param channels: A list of integers from 1 to 5 to plot only specific channels.
    :type channels: int
    :param plot_time_freq: Determines whether to plot the time domain or a spectrogram.
    :type plot_time_freq: bool
    """
    d = an_ecg_object
    if channels is not None:
        channels_to_plot = channels
    else:
        channels_to_plot = list(range(1, 6))
    # TODO: HIGH, Raise exception here if channels is simply empty ([]). there should be at least one channel plotted.
    channels_to_plot = list(map(lambda x: f"ecg{x}", channels_to_plot))

    if plot_time_freq:
        channels_to_plot = list(map(lambda x: scipy.signal.spectrogram(d[x], 500, mode="magnitude"), channels_to_plot))

    if ax is None:
        if not plot_time_freq:
            ax = d.plot("tstamp", channels_to_plot[0])
        else:
            ax = plt.pcolormesh(channels_to_plot[0][1], channels_to_plot[0][2][0:15], channels_to_plot[0][3][0:15, :])
            plt.ylabel('Frequency [Hz]')
            plt.xlabel('Time [sec]')
    else:
        if not plot_time_freq:
            d.plot("tstamp", channels_to_plot[0], ax=ax)
        else:
            plt.pcolormesh(channels_to_plot[0][1], channels_to_plot[0][0], channels_to_plot[0][2])
            plt.ylabel('Frequency [Hz]')
            plt.xlabel('Time [sec]')

    for u in channels_to_plot[1:]:
        if not plot_time_freq:
            d.plot("tstamp", u, ax=ax)
        else:
            plt.pcolormesh(u[1], u[0][0:15], u[2][0:15, :])
            plt.ylabel('Frequency [Hz]')
            plt.xlabel('Time [sec]')


def plot_ecg_bokeh(an_ecg_object, channels=None):
    """
    Creates interactive ECG plots using Bokeh.

    Notes:
        * This function produces a fixed "column" layout to specifically review ECG signals in the time domain in
          Jupyter notebooks.

    :param an_ecg_object: A Kymira ECG dataset
    :type an_ecg_object: pandas.DataFrame
    :param channels: A list of integers that specify which `ecgn` (where n is a channel) to plot. If not specified,
                     the function will generate plots for all of the channels.
    :type channels: list[int]

    :returns: Nothing. The side effect of this function is to create the plot.
    """
    # Enable notebook output
    bokeh.io.output_notebook()
    # Make the timestamp the common "axis" between all plots.
    shared_x_values = an_ecg_object["tstamp"]

    # Include all channels if channels is not specified.
    if channels is None:
        channels = list(range(1, len(an_ecg_object.columns)))

    # TODO: HIGH, Raise exception if the contents of channels refer a channel that does not exist
    ecg_channel_values = list(map(lambda x: an_ecg_object[f"ecg{x}"], channels))

    # Build up all individual plots.
    figures = []
    for a_channel_idx, a_channel_waveform in enumerate(ecg_channel_values):
        if a_channel_idx == 0:
            figures.append(bokeh.plotting.figure(width=900,
                                                 height=350,
                                                 x_axis_label="Time (Samples)",
                                                 y_axis_label="Amplitude",
                                                 toolbar_location="below",
                                                 tools="pan, box_zoom, reset",
                                                 title=f"ecg{channels[a_channel_idx]}"))
        else:
            figures.append(bokeh.plotting.figure(x_range=figures[0].x_range,
                                                 width=900,
                                                 height=350,
                                                 x_axis_label=figures[0].xaxis.axis_label,
                                                 y_axis_label=figures[0].yaxis.axis_label,
                                                 toolbar_location=figures[0].toolbar_location,
                                                 tools="pan, box_zoom, reset",
                                                 title=f"ecg{channels[a_channel_idx]}"))
        figures[-1].line(shared_x_values, a_channel_waveform)

    # Build the layout from the existing plots
    grid_plot_figure = bokeh.layouts.column(*figures)
    # Show it back to the notebook.
    bokeh.io.show(grid_plot_figure)

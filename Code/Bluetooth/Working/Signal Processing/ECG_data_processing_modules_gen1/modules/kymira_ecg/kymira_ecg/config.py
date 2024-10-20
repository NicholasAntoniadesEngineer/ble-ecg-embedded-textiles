"""
General coniguration parameters.

.. warning ::
    These parameters need to be reviewed and embedded in the right context.

:author: Athanasios Anastasiou
:date: Jan 2021
"""

# Constants
FS = 500  # Sampling frequency

H_CUTOFF = 40  # Higher-cutoff for bandpass filter
L_CUTOFF = 0.5  # Lower-cutoff for bandpass filter
ORDER = 4  # Order of the Butterworth filter

SF_THRESH = 0.675  # Spectral flatness threshold
PV_THRESH_L = 1  # Peak variance lower threshold
PV_THRESH_H = 80000  # Peak variance higher threshold
WINDOW_LENGTH = 2 ** 10
PERCENTILE = 95  # Percentile used for the height when identifying peaks
DISTANCE = FS / 2  # Distance between peaks being identified
NFFT = 2500          # Length of the signal

# PERCENTILE = 93      # Percentile used for the height when identifying peaks
# DISTANCE = 230       # Distance between peaks being identified
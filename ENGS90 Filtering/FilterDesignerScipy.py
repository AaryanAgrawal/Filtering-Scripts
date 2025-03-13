import numpy as np
import scipy.signal as signal

# Sampling frequency
fs = 333  # Adjust based on your system

# ------------------------------------------------------------------------
# 1) Bandstop (Band-Reject) Filter
#    Example: remove frequencies from 5 Hz to 8 Hz
# ------------------------------------------------------------------------
f_stop_low = 2.0   # Lower edge of stop band (Hz)
f_stop_high = 16.0  # Upper edge of stop band (Hz)
order_bs = 2       # Bandstop filter order

# Design the bandstop Butterworth filter
b_bs, a_bs = signal.butter(
    order_bs, 
    [f_stop_low / (fs / 2), f_stop_high / (fs / 2)], 
    btype='bandstop'
)

# ------------------------------------------------------------------------
# 2) Low-Pass Butterworth Filter
#    Example: cutoff at 20 Hz
# ------------------------------------------------------------------------
f_cutoff = 20.0    # Hz
order_lp = 1       # Filter order
b_lp, a_lp = signal.butter(
    order_lp, 
    f_cutoff / (fs / 2), 
    btype='low'
)

# ------------------------------------------------------------------------
# 3) Convert Each Filter to SOS (Second-Order Sections)
# ------------------------------------------------------------------------
sos_bs = signal.tf2sos(b_bs, a_bs)
sos_lp = signal.tf2sos(b_lp, a_lp)

# ------------------------------------------------------------------------
# 4) Cascade the Bandstop and Low-Pass Filters
# ------------------------------------------------------------------------
sos_combined = np.vstack((sos_bs, sos_lp))

# ------------------------------------------------------------------------
# 5) Convert the Combined SOS Filter to Direct-Form Coefficients
# ------------------------------------------------------------------------
b_combined, a_combined = signal.sos2tf(sos_combined)

# Print the results
print("Feedforward coefficients (b):", b_combined)
print("Feedback coefficients (a):", a_combined)

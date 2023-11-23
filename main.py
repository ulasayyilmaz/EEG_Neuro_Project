import os
import matplotlib.pyplot as plt
import numpy as np
import mne

# path
file_path = '/Users/ulasayyilmaz/Desktop/POM Super Junior/Neuro/EEG_Neuro_Project/AA0005.vhdr'

# Read the EEG data
raw = mne.io.read_raw_brainvision(file_path)

# Print information about the data
print(raw)


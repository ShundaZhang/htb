import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("data.npy.gz")
core_data = np.loadtxt("known_samples.npy.gz")
all_data = np.vstack((core_data, data))
del data

class_count = len(core_data)

out_labels = np.full((all_data.shape[0],), -1)

assert(np.all(np.logical_and(0 <= out_labels, out_labels < 256)))

file_data = bytearray(out_labels[256:].shape[0])
for ix, val in enumerate(out_labels[256:]):
    file_data[ix] = val
file_data = bytes(file_data)
with open("flag.jpg", "wb") as outfile:
    outfile.write(file_data)
del file_data


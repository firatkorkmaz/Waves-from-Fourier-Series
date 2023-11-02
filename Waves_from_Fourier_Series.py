# Square Waves from Trigonometric Fourier Series #

import numpy as np
import matplotlib.pyplot as plt

freq_hertz = 2
duration_sec = 3
sample_in_sec = 10000
sample_number = np.arange(duration_sec * sample_in_sec)

total_wave_s = np.full(sample_number.shape, 1.0 / 2)

fig_s = plt.figure(figsize=(8, 6))
ax_s = fig_s.add_subplot(111)
ax_s.set_ylim([-2, 2])

fig_s.show()
fig_s.canvas.draw()

for i in np.arange(1, 50, 2):
    ax_s.clear()
    
    p_s, = ax_s.plot(sample_number / sample_in_sec, np.full(sample_number.shape, total_wave_s))
    wave_s = 2 / (i * np.pi) * np.cos(2 * np.pi * freq_hertz * sample_number * i / sample_in_sec - np.pi / 2)
    total_wave_s += wave_s
    
    p_s.set_data(sample_number / sample_in_sec, total_wave_s)
    fig_s.canvas.draw()
    plt.pause(0.3)

plt.show()

#############################################################

# Triangle Waves from Trigonometric Fourier Series #

import numpy as np
import matplotlib.pyplot as plt

freq_hertz = 2
duration_sec = 3
sample_in_sec = 10000
sample_number = np.arange(duration_sec * sample_in_sec)

total_wave_t = np.full(sample_number.shape, 1.0 / 2)

fig_t = plt.figure(figsize=(8, 6))
ax_t = fig_t.add_subplot(111)
ax_t.set_ylim([-2, 2])

fig_t.show()
fig_t.canvas.draw()

for i in np.arange(1, 50, 2):
    ax_t.clear()
    
    p_t, = ax_t.plot(sample_number / sample_in_sec, np.full(sample_number.shape, total_wave_t))
    wave_t = -4 / (np.pi**2 * i**2) * np.cos(2 * np.pi * freq_hertz * sample_number * i / sample_in_sec)
    total_wave_t += wave_t
    
    p_t.set_data(sample_number / sample_in_sec, total_wave_t)
    fig_t.canvas.draw()
    plt.pause(0.3)

plt.show()
from scipy.signal import square
import numpy as np
from matplotlib.widgets import Slider
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi, num=1000)

fig, ax = plt.subplots(figsize=(10, 4))
plt.subplots_adjust(bottom=0.25)

ax_slider = plt.axes([0.2, 0.1, 0.65, 0.05])
slider = Slider(ax_slider, label='Частота (Гц)', valmin=0.0, valmax=10.0, valinit=2.0, valstep=0.1)


def update(val):
    ax.clear()
    freq = slider.val
    wave = square(2 * np.pi * freq * t)
    ax.plot(t, wave, linewidth=1.5)
    ax.axhline(y=0, color='black', linewidth=0.8)
    ax.set_title(f"Прямоугольный сигнал: частота = {freq:.1f} Гц")
    ax.set_xlabel('t (rad)')
    ax.set_ylabel('Амплитуда')
    ax.set_ylim(-1.5, 1.5)
    ax.grid(True)
    fig.canvas.draw_idle()

slider.on_changed(update)
update(slider.val)

plt.show()
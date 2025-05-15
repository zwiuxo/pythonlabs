import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

f1, a1 = 1.0, 1.0  
f2, a2 = 2.0, 0.5  
x = np.linspace(0, 2*np.pi, 500)


fig = plt.figure(figsize=(10, 6))
ax1 = fig.add_subplot(311)
ax2 = fig.add_subplot(312)
ax_sum = fig.add_subplot(313)


line1, = ax1.plot(x, a1 * np.sin(f1 * x), 'r')
line2, = ax2.plot(x, a2 * np.sin(f2 * x), 'b')
line_sum, = ax_sum.plot(x, a1 * np.sin(f1 * x) + a2 * np.sin(f2 * x), 'g')


ax1.set_title('Волна 1')
ax2.set_title('Волна 2')
ax_sum.set_title('Сумма волн')


ax_f1 = plt.axes([0.2, 0.02, 0.6, 0.03])
ax_a1 = plt.axes([0.2, 0.06, 0.6, 0.03])
ax_f2 = plt.axes([0.2, 0.10, 0.6, 0.03])
ax_a2 = plt.axes([0.2, 0.14, 0.6, 0.03])

s_f1 = Slider(ax_f1, 'Частота 1', 0.1, 5.0, valinit=f1)
s_a1 = Slider(ax_a1, 'Амплитуда 1', 0.1, 5.0, valinit=a1)
s_f2 = Slider(ax_f2, 'Частота 2', 0.1, 5.0, valinit=f2)
s_a2 = Slider(ax_a2, 'Амплитуда 2', 0.1, 5.0, valinit=a2)

def update(val):
    y1 = s_a1.val * np.sin(s_f1.val * x)
    y2 = s_a2.val * np.sin(s_f2.val * x)
    line1.set_ydata(y1)
    line2.set_ydata(y2)
    line_sum.set_ydata(y1 + y2)
    fig.canvas.draw_idle()

for slider in [s_f1, s_a1, s_f2, s_a2]:
    slider.on_changed(update)

plt.tight_layout()
plt.show()
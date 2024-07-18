# %%

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

img = Image.open("oval.png")
img = img.convert("L")
sqrWidth = np.ceil(np.sqrt(img.size[0]*img.size[1])).astype(int)
img = img.resize((sqrWidth, sqrWidth))
img = img.rotate(45)
pic = np.array(img, dtype=np.float32)

plt.imshow(pic, cmap="gray")
plt.show()

x = pic.sum(0)
y = pic.sum(1)
t = list(range(len(x)))

b, a = signal.butter(1, 0.01, btype='low', analog=False)
x = signal.filtfilt(b, a, x)
y = signal.filtfilt(b, a, y)

out = np.zeros((len(x), len(y)))

out = np.apply_along_axis(lambda t: t+y, 0, out)
out = np.apply_along_axis(lambda t: t+x, 1, out)

out /= np.max(out)

plt.imshow(out, cmap="gray")
plt.show()

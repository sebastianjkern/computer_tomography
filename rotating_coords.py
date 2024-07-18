# %%
from PIL import Image
import numpy as np
from scipy import signal

img = Image.open("oval.png")
img = img.convert("L")
sqrWidth = np.ceil(np.sqrt(img.size[0]*img.size[1])).astype(int)
img = img.resize((sqrWidth, sqrWidth))

aggregations = {}

for angle in range(90):
    temp = img.rotate(angle)
    pic = np.array(img, dtype=np.float32)
    x = pic.sum(0)
    y = pic.sum(1)
    t = list(range(len(x)))
    b, a = signal.butter(1, 0.01, btype='low', analog=False)
    x = signal.filtfilt(b, a, x)
    y = signal.filtfilt(b, a, y)

    aggregations[angle] = x
    aggregations[angle+90] = y

print(aggregations)
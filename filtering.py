### fake rgb coloring to imitate monitor filtering schemes

import sys 
import numpy as np
from scipy.stats import bernoulli
from PIL import Image, ImageMath, ImageMode

img = Image.open(sys.argv[1])
imgr, imgg, imgb = img.split()
(xdim, ydim) = img.size

masks = []
for i in range(3):
    masks.append(np.uint8(np.array([[((x+y)%3 == i) for x in range(xdim)] \
    for y in range(ydim)], dtype=int)))

colorprobabilityarrays = []
for x in [imgr, imgg, imgb]:
    colorprobabilityarrays.append((np.array(x) / 255))
    
pixelarrays = []
for x in range(3):
    pixelarrays.append(np.uint8(np.array([bernoulli.rvs(p) * 255 \
    for p in colorprobabilityarrays[x] ]) * masks[x]))
    
(rnext, gnext, bnext) = (Image.fromarray(x, mode='L') for x in pixelarrays)

finimage = Image.merge("RGB", (rnext, gnext, bnext))

finimage.show()


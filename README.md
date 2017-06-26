# subpixels
fake RGB coloring to imitate montior filtering schemes

How it works
============

Usage
-----

>python filter.py \<imagename\>

Details
-------

Red, green, and blue pixels can appear along alternating diagonals. A colored
pixel appears based on draws from Bernoulli distributions which take their
probabilities from the corresponding RGB value of the original image.

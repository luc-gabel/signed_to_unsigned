import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import axes_grid1

def add_colorbar(im, aspect=20, pad_fraction=0.5, **kwargs):

    divider = axes_grid1.make_axes_locatable(im.axes)
    width = axes_grid1.axes_size.AxesY(im.axes, aspect=1./aspect)
    pad = axes_grid1.axes_size.Fraction(pad_fraction, width)
    current_ax = plt.gca()
    cax = divider.append_axes("right", size=width, pad=pad)
    plt.sca(current_ax)
    return im.axes.figure.colorbar(im, cax=cax, **kwargs)

def to_uint(img):
    new_img=np.zeros(shape=img.shape, dtype=np.uint16)
    for i in range(len(img)):
        for j in range(len(img[i])):
            new_img[i][j]= img[i][j] + 32768
                                    
    assert np.max(new_img)<65536
                                    
    return new_img
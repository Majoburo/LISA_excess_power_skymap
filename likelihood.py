from lisatools.detector import EqualArmlengthOrbits, ESAOrbits
from lisatools.sensitivity import get_sensitivity, A1TDISens, E1TDISens, T1TDISens
from matplotlib import pyplot as plt
import numpy as np
import healpy as hp
from h5py import File
from lisagwresponse import StochasticBackground
from lisagwresponse.psd import ifft_generator

orbits_file = "esa-orbits-1-0-2.h5"
with File(orbits_file) as f:
    orbit_t0 = f.attrs['t0']

npix = hp.nside2npix(8)
skymap = np.arange(npix) / np.sqrt(npix)
generator = ifft_generator(lambda f: f**(-2/3))
background = StochasticBackground(skymap, generator, orbits=orbits_file, dt=5, size=10000, t0=10 + orbit_t0)
background.plot(background.t)
plt.show()





if __name__ == '__main__':
    # basically, time chunk data, then use blip-esque likelihood
    # Sgw^{IJ}(f,t) = 1/sqrt(4pi*sum(A)) * sum_{pixels}(A_{pixel} R^{IJ}_{pixel}(f,t))
    pass
    # need responses at a pixel in each channel, at each frequency

    

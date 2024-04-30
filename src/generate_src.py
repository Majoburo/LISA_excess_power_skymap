import numpy as np
import matplotlib.pyplot as plt

import h5py
from fastlisaresponse import pyResponseTDI, ResponseWrapper
from astropy import units as un

from lisatools.detector import EqualArmlengthOrbits, ESAOrbits

YRSID_SI = 31558149.763545603

class GBWave:
    def __init__(self, use_gpu=False):

        if use_gpu:
            self.xp = xp
        else:
            self.xp = np

    def __call__(self, A, f, fdot, iota, phi0, psi, T=1.0, dt=10.0):

        # get the t array
        t = self.xp.arange(0.0, T * YRSID_SI, dt)
        cos2psi = self.xp.cos(2.0 * psi)
        sin2psi = self.xp.sin(2.0 * psi)
        cosiota = self.xp.cos(iota)

        fddot = 11.0 / 3.0 * fdot ** 2 / f

        # phi0 is phi(t = 0) not phi(t = t0)
        phase = (
            2 * np.pi * (f * t + 1.0 / 2.0 * fdot * t ** 2 + 1.0 / 6.0 * fddot * t ** 3)
            - phi0
        )

        hSp = -self.xp.cos(phase) * A * (1.0 + cosiota * cosiota)
        hSc = -self.xp.sin(phase) * 2.0 * A * cosiota

        hp = hSp * cos2psi - hSc * sin2psi
        hc = hSp * sin2psi + hSc * cos2psi

        return hp + 1j * hc

gb = GBWave(use_gpu=False)

use_gpu = False

T = 2.0  # years
t0 = 10000.0  # time at which signal starts (chops off data at start of waveform where information is not correct)

sampling_frequency = 0.1
dt = 1

# order of the langrangian interpolation
order = 25

# 1st or 2nd or custom (see docs for custom)
tdi_gen = "2nd generation"

index_lambda = 6
index_beta = 7

tdi_kwargs_esa = dict(
    order=order, tdi=tdi_gen, tdi_chan="AET",
)

gb_lisa_esa = ResponseWrapper(
    gb,
    T,
    dt,
    index_lambda,
    index_beta,
    t0=t0,
    flip_hx=False,  # set to True if waveform is h+ - ihx
    use_gpu=use_gpu,
    remove_sky_coords=True,  # True if the waveform generator does not take sky coordinates
    is_ecliptic_latitude=True,  # False if using polar angle (theta)
    remove_garbage=True,  # removes the beginning of the signal that has bad information
    orbits=EqualArmlengthOrbits(),
    **tdi_kwargs_esa,
)

# define GB parameters
A = 1.084702251e-22
f = 2.35962078e-3
fdot = 1.47197271e-17
iota = 1.11820901
phi0 = 4.91128699
psi = 2.3290324

beta = 0.9805742971871619
lam = 5.22979888

chans = gb_lisa_esa(A, f, fdot, iota, phi0, psi, lam, beta)

#fig, ax = plt.subplots(3, 1, sharex=True)

#for i, lab in enumerate(["A", "E", "T"]):
#    ax[i].plot(np.arange(len(chans[0])) * dt / YRSID_SI, chans[i])
#    ax[i].set_ylabel(lab)

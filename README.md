# Excess power skymap

Hopefully this will take in LISA data and put it on a skymap ignoring any kind of coherence.

Dependencies:
  - fastlisaresponse
  - ??

TODO:
  - likelihood 
    inputs: parameters(healpix index, amplitude) 
    outputs: likelihood
    - noise model
    - response (fastlisaresponse)
  - sampling
  - data generation
    - amplitude at each healpix pixel in each frequency
    - instrument noise
  - output plots

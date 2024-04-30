# Excess power skymap

Hopefully this will take in LISA data and put it on a skymap ignoring any kind of coherence.

Dependencies:
  - fastlisaresponse
  - ??

TODO:
  - likelihood -- could copy blip one basically
    inputs: parameters(healpix index, amplitude) 
    outputs: likelihood
    - noise model
    - response (fastlisaresponse)
      - this turned out to be hard. might be able to adapt it from lisagwresponse, pixel basis but currently generates timeseries when not needed
        - figure out right things to sum to get stochastic response. I think it's something like abs(hplus)^2 + abs(hcross)^2
  - sampling
  - data generation
    - amplitude at each healpix pixel in each frequency
    - instrument noise -- working!
  - output plots

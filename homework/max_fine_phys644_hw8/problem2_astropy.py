from astropy.cosmology import Planck18 as cosmo
from astropy.constants import c, sigma_T
import astropy.units as u
import numpy as np

# Given parameters
z = 1000
delta_z = 200
n_e0 = 0.25 * u.m**-3  # present-day electron density

# Hubble parameter at redshift z
H_z = cosmo.H(z)

# Silk damping scale (comoving)
r_silk_comoving = (1 + z)**(-0.5) * np.sqrt(
    (delta_z / z) * (1 / H_z) * (c / (sigma_T * n_e0))
)

# Convert to comoving Mpc
r_silk_comoving = r_silk_comoving.to(u.Mpc)

print(f"Silk damping scale (comoving): {r_silk_comoving:.2f}")

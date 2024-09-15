# llh_to_ecef.py
#
# Usage: python3 llh_to_ecef.py lat_deg lon_deg hae_km
#  Converts LLH (Latitude, Longitude, Height Above Ellipsoid) to ECEF coordinates
#  See "Fundamentals of Astrodynamics and Applications, Fourth Edition" by
#  David A. Vallado, pages 174-175
# Parameters:
#  lat_deg: Latitude in degrees
#  lon_deg: Longitude in degrees
#  hae_km: Height Above Ellipsoid in km
# Output:
#  Prints the ECEF x, y, and z coordinates in km
#
# Written by Nick Davis
# Other contributors: None
#
# This work is licensed under CC BY-SA 4.0

# import Python modules
import math  # math module
import sys   # argv

# "constants"
R_E_KM = 6378.1363  # Equatorial radius in kilometers
E_E    = 0.081819221456  # Earth's eccentricity

# helper functions

## calculated denominator
def calc_denom(ecc, lat_rad):
  return math.sqrt(1.0 - (ecc**2) * (math.sin(lat_rad)**2))

# initialize script arguments
lat_deg = float('nan')  # Latitude in degrees
lon_deg = float('nan')  # Longitude in degrees
hae_km  = float('nan')  # Height Above Ellipsoid in km

# parse script arguments
if len(sys.argv) == 4:
  lat_deg = float(sys.argv[1])
  lon_deg = float(sys.argv[2])
  hae_km  = float(sys.argv[3])
else:
  print('Usage: python3 llh_to_ecef.py lat_deg lon_deg hae_km')
  exit()

# write script below this line

# convert degrees to radians
lat_rad = math.radians(lat_deg)
lon_rad = math.radians(lon_deg)

# calculate the denominator and radius of curvature in the prime vertical
denom = calc_denom(E_E, lat_rad)
c_E = R_E_KM / denom

# calculate ECEF coordinates
r_x_km = (c_E + hae_km) * math.cos(lat_rad) * math.cos(lon_rad)
r_y_km = (c_E + hae_km) * math.cos(lat_rad) * math.sin(lon_rad)
r_z_km = (c_E * (1 - E_E**2) + hae_km) * math.sin(lat_rad)

# print ECEF x, y, and z coordinates in km
print(f"ECEF X: {r_x_km} km")
print(f"ECEF Y: {r_y_km} km")
print(f"ECEF Z: {r_z_km} km")

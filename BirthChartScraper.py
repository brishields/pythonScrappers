import pyswisseph as swe
import matplotlib.pyplot as plt
import numpy as np

# Function to get planet's longitude
def get_planet_longitude(jd, planet):
    xx, ret = swe.calc_ut(jd, planet)
    return xx[0]

# Function to get Part of Fortune
def get_part_of_fortune(jd):
    xx, _ = swe.calc_ut(jd, swe.SUN)
    sun = xx[0]
    xx, _ = swe.calc_ut(jd, swe.MOON)
    moon = xx[0]
    xx, _ = swe.calc_ut(jd, swe.ASC)
    asc = xx[0]
    return (asc + moon - sun) % 360

# Function to plot a planet on the chart
def plot_planet(ax, planet_longitude, planet_symbol):
    x = np.cos(np.radians(planet_longitude))
    y = np.sin(np.radians(planet_longitude))
    ax.plot(x, y, 'o', label=planet_symbol)
    ax.annotate(planet_symbol, (x, y), textcoords="offset points", xytext=(5,5))

# Sample birth data
year, month, day = 2023, 9, 26
jd = swe.julday(year, month, day)

# Retrieve planetary positions
planets = {
    swe.SUN: '☉',
    swe.MOON: '☽',
    swe.MERCURY: '☿',
    swe.VENUS: '♀',
    swe.MARS: '♂',
    swe.JUPITER: '♃',
    swe.SATURN: '♄',
    swe.URANUS: '♅',
    swe.NEPTUNE: '♆',
    swe.PLUTO: '♇',
    swe.CHIRON: '⚷',
    swe.TRUE_NODE: '☊',
    swe.MEAN_APOG: '⚸'  # Black Moon Lilith
}

# Create an astrological wheel using matplotlib
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)

# Plot planets
for planet, symbol in planets.items():
    plot_planet(ax, get_planet_longitude(jd, planet), symbol)

# Plot Part of Fortune
plot_planet(ax, get_part_of_fortune(jd), '⊕')

# Legend and show
ax.legend()
plt.show()

#!/usr/bin/python3

from fontParts.world import *
import sys

# Open UFO
ufo = sys.argv[1]
font = OpenFont(ufo)

# Modify UFO
danda = font['u0A66']
danda.name = 'zero.guru'

# Save UFO
font.changed()
font.save()
font.close()

from PIL import Image, ImageDraw, ImageFont
from enum import Enum
import quicklibs as qlib

margin = 10
resize_scale = 1

map_name = "Asgorath's Fang"

map_era = "Unique"

map_lore = """Map Lore:

"""

# Map Size
map_width = 1920 + margin
map_height = 1080 + margin
map_anchor_x = margin
map_anchor_y = margin

class Color(Enum):
    BACKGROUND = (195,180,145)
    OUTLINE = (158, 146, 117)
    PLANE = (59, 55, 44)
    HILL = (14, 15, 15)
    TUNDRA = "white"

# Default Colors

# Text Sizes
fontsize_title = 16

names_used = [""]

def name_taken(name):
    taken = False
    for i in names_used:
        if i == name:
            taken = True
        return taken

# Fonts
title_font = ImageFont.truetype("TrueFonts/1997.ttf", size = fontsize_title)
description_font = ImageFont.truetype("TrueFonts/1997.ttf", size = fontsize_title)
capitals_font = ImageFont.truetype("TrueFonts/1997.ttf", size = fontsize_title)
cities_font = ImageFont.truetype("TrueFonts/1997.ttf", size = fontsize_title)
village_font = ImageFont.truetype("TrueFonts/1997.ttf", size = fontsize_title)

# Background and Foreground
full_image = Image.new('RGBA', (map_width, map_height), Color.BACKGROUND.value)

# Start drawing stuff
draw = ImageDraw.Draw(full_image)

# Resize
full_image = full_image.resize((map_width * resize_scale, map_height * resize_scale), Image.NEAREST)

full_image.save("maps/" + map_name + ".png")
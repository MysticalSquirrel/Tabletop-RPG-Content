from PIL import Image, ImageDraw, ImageFont
margin = 10
image_width = 800
image_height = 400

item_name = "10 Characters!"

item_quality = "10 Characters"

item_prefix = "Maximum 29 Characters per Line!"
item_subprefix = "Maximum 29 Characters per Line!"
item_suffix = "Maximum 29 Characters per Line!"
item_subsuffix = "Maximum 29 Characters per Line!"

item_description = """Item Lore:
Maximum 42 Characters per line before
using \"\\n\"! (< How to change onto a
new line when using \" \")
(Using \"\"\" \"\"\" makes new lines in the code
also change line!)
Maximum 7 Lines!"""

image_width = 64
image_height = 128
image_anchor_x = margin
image_anchor_y = margin

title_width = 162
title_height = 10
title_anchor_x = margin + image_width + margin
title_anchor_y = margin

quality_width = 94
quality_height = 10
quality_anchor_x = title_anchor_x + title_width + margin
quality_anchor_y = margin

modifier_width = 256
modifier_height = 64
modifier_anchor_x = margin + image_width + margin
modifier_anchor_y = margin*2 + title_height + margin

prefix_y = modifier_anchor_y
subprefix_y = prefix_y + (modifier_height/4)
suffix_y = subprefix_y + (modifier_height/4)
subsuffix_y = suffix_y + (modifier_height/4)

description_width = 256
description_height = 64
description_anchor_x = margin
description_anchor_y = margin*4 + modifier_height + margin

combined_width = image_width + margin + modifier_width
full_width = margin + combined_width + margin
full_height = margin + description_anchor_y + description_height + margin

background_color = (195,180,145)
text_color = "black"

file = open(("items/" + item_name + ".txt"), "w")

full_image = Image.new('RGB', (full_width, full_height), background_color)
draw = ImageDraw.Draw(full_image)

fontsize_title = 16
fontsize_quality = 9
fontsize_modifier = 9
fontsize_description = 8

title_font = ImageFont.truetype("TrueFonts/1997.ttf", size = fontsize_title)
quality_font = ImageFont.truetype("TrueFonts/1997.ttf", size = fontsize_quality)
modifier_font = ImageFont.truetype("TrueFonts/1997.ttf", size = fontsize_modifier)
description_font = ImageFont.truetype("TrueFonts/Bitty.ttf", size = fontsize_description)

# Title
draw.text((title_anchor_x, title_anchor_y), item_name, text_color, font=title_font)
file.write("Name:\n" + item_name + "\n\n")

# Quality
draw.text((quality_anchor_x, quality_anchor_y), item_quality, text_color, font=quality_font)
file.write("Quality:\n" + item_quality + "\n\n")

# Modifiers
draw.text((modifier_anchor_x, prefix_y), item_prefix, text_color, font=modifier_font)
draw.text((modifier_anchor_x, subprefix_y), item_subprefix, text_color, font=modifier_font)
draw.text((modifier_anchor_x, suffix_y), item_suffix, text_color, font=modifier_font)
draw.text((modifier_anchor_x, subsuffix_y), item_subsuffix, text_color, font=modifier_font)
file.write("Prefix:\n" + item_prefix + "\n\n")
file.write("SubPrefix:\n" + item_subprefix + "\n\n")
file.write("Suffix:\n" + item_suffix + "\n\n")
file.write("SubSiffx:\n" + item_subsuffix + "\n\n")

# Description
draw.text((description_anchor_x, description_anchor_y), item_description, text_color, font=description_font)
file.write("Description:\n" + item_description + "\n\n")

#img.putdata(my_list)
full_image.save("items/" + item_name + ".png")
file.close()

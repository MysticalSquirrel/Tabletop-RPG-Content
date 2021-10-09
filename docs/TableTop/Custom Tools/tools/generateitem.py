from PIL import Image, ImageDraw, ImageFont
margin = 10
result_size = 2
icon = Image.open ("items/icons/dagger.png")

item_name = "Asgorath's Fang"

item_quality = "Unique"

item_prefix = "Effects:"
item_subprefix = "Deals 1d6 Slashing or Piercing Damage."
item_suffix = "Add an extra 1 Poison Damage."
item_subsuffix = "Can be used in alchemy as poison source."

#----------------------Text Width Limit ----------------#
item_description = """Item Lore:
In a fight between Asgaroth and Lolth, a fang was broken.
In the breaking of the fang, a portal opened sending it in
in the safest place it could quickly go out of Lolth's reach.
On the material plane where Lokr stumbled upon it.

""" ### The line above is the limit.

file = open(("items/" + item_name + ".txt"), "w")

# Icon Size & Anchor
icon_width = 64
icon_height = 128
icon_anchor_x = margin
icon_anchor_y = margin

# Title Size & Anchor
title_width = 181
title_height = 24
title_anchor_x = icon_anchor_x + icon_width + margin
title_anchor_y = margin

# Quality Size & Anchor
quality_width = 65
quality_height = 24
quality_anchor_x = title_anchor_x + title_width + margin
quality_anchor_y = margin + int(quality_height/4)

# Modifier Size & Anchor
modifier_width = 256
modifier_height = 94
modifier_anchor_x = icon_anchor_x + icon_width + margin
modifier_anchor_y = margin + title_height + margin

# Modifiers individual Anchors
prefix_y = modifier_anchor_y
subprefix_y = prefix_y + (modifier_height/4)
suffix_y = subprefix_y + (modifier_height/4)
subsuffix_y = suffix_y + (modifier_height/4)

# Description Size & Anchor
description_width = icon_width + margin + modifier_width
description_height = 64
description_anchor_x = margin
description_anchor_y = icon_anchor_y + icon_height + margin

# Combining the Sizes & Anchor
combined_width = icon_width + margin + modifier_width
full_width = margin + combined_width + margin
full_height = margin + description_anchor_y + description_height + margin

# Default Colors
background_color = (195,180,145)
foreground_color = (158, 146, 117)
panel_color = (59, 55, 44)
iconpanel_color = (14, 15, 15)
text_color = "white"

# Text Sizes
fontsize_title = 16
fontsize_quality = 9
fontsize_modifier = 9
fontsize_description = 8

# Rarity Colors
unique_color = (255,255,255)
if item_quality.lower() == "common":
    background_color = (125, 125, 125)
    unique_color = (255,255,255)
elif item_quality.lower() == "uncommon":
    background_color = (8, 137, 8)
    unique_color = (48, 237, 38)
elif item_quality.lower() == "magical":
    background_color = (8, 57, 137)
    unique_color = (38, 157, 237)
elif item_quality.lower() == "legendary":
    background_color = (137, 84, 8)
    unique_color = (237, 184, 38)
elif item_quality.lower() == "unique":
    background_color = (107, 5, 78)
    unique_color = (207, 105, 178)
else:
    background_color = (125, 125, 125)
    unique_color = (255,255,255)

# Fonts
title_font = ImageFont.truetype("TrueFonts/1997.ttf", size = fontsize_title)
quality_font = ImageFont.truetype("TrueFonts/1997.ttf", size = fontsize_quality)
modifier_font = ImageFont.truetype("TrueFonts/1997.ttf", size = fontsize_modifier)
description_font = ImageFont.truetype("TrueFonts/1997.ttf", size = fontsize_description)

# Background and Foreground
full_image = Image.new('RGBA', (full_width, full_height), background_color)

foreground_image = Image.new('RGBA', (full_width-margin, full_height-margin), foreground_color)

full_image.paste(foreground_image,(int(margin/2), int(margin/2)))

# Start Drawing Stuff
draw = ImageDraw.Draw(full_image)

# Icon
panel_image = Image.new('RGBA', (icon_width, icon_height), iconpanel_color)
full_image.paste(panel_image, (icon_anchor_x, icon_anchor_y))

full_image.paste(icon, (icon_anchor_x, icon_anchor_y), mask=icon)

# Title
panel_image = Image.new('RGBA', (title_width, title_height), panel_color)
full_image.paste(panel_image, (title_anchor_x, title_anchor_y))

draw.text((title_anchor_x+1, title_anchor_y), item_name, text_color, font=title_font)
file.write("Name:\n" + item_name + "\n\n")

# Quality
panel_image = Image.new('RGBA', (quality_width, quality_height), panel_color)
full_image.paste(panel_image, (quality_anchor_x, title_anchor_y))

draw.text((quality_anchor_x+1, quality_anchor_y), item_quality, unique_color, font=quality_font)
file.write("Quality:\n" + item_quality + "\n\n")

# Modifiers
panel_image = Image.new('RGBA', (modifier_width, modifier_height), panel_color)
full_image.paste(panel_image, (modifier_anchor_x, modifier_anchor_y))

draw.text((modifier_anchor_x+2, prefix_y), item_prefix, text_color, font=modifier_font)
draw.text((modifier_anchor_x+2, subprefix_y), item_subprefix, text_color, font=modifier_font)
draw.text((modifier_anchor_x+2, suffix_y), item_suffix, text_color, font=modifier_font)
draw.text((modifier_anchor_x+2, subsuffix_y), item_subsuffix, text_color, font=modifier_font)
file.write(item_prefix + "\n")
file.write(item_subprefix + "\n")
file.write(item_suffix + "\n")
file.write(item_subsuffix + "\n\n")

# Description
panel_image = Image.new('RGBA', (description_width, description_height), panel_color)
full_image.paste(panel_image, (description_anchor_x, description_anchor_y))

draw.text((description_anchor_x+2, description_anchor_y), item_description, text_color, font=description_font)
file.write(item_description + "\n\n")

# Resize
full_image = full_image.resize((full_width * result_size, full_height * result_size), Image.NEAREST)

full_image.save("items/" + item_name + ".png")
file.close()

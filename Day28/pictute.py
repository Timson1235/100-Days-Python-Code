from PIL import Image, ImageDraw, ImageFont

# Create a blank image with white background
width, height = 800, 600
image = Image.new('RGB', (width, height), color='white')
draw = ImageDraw.Draw(image)

# Load a default font
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
title_font = ImageFont.truetype(font_path, 50)
subtitle_font = ImageFont.truetype(font_path, 30)
author_font = ImageFont.truetype(font_path, 20)

# Define text content
title_text = "Treatment Time Prediction Project"
subtitle_text = "Using Machine Learning with TensorFlow"
authors_text = "Lukas Julius Eule and Tim Prause"
date_text = "Data: 04.01.2021 - 30.04.2024"

# Calculate text size and position
title_width, title_height = draw.textsize(title_text, font=title_font)
subtitle_width, subtitle_height = draw.textsize(subtitle_text, font=subtitle_font)
authors_width, authors_height = draw.textsize(authors_text, font=author_font)
date_width, date_height = draw.textsize(date_text, font=author_font)

title_position = ((width - title_width) / 2, height / 4)
subtitle_position = ((width - subtitle_width) / 2, height / 4 + title_height + 20)
authors_position = ((width - authors_width) / 2, height / 2 + 20)
date_position = ((width - date_width) / 2, height / 2 + authors_height + 40)

# Add text to image
draw.text(title_position, title_text, fill="black", font=title_font)
draw.text(subtitle_position, subtitle_text, fill="black", font=subtitle_font)
draw.text(authors_position, authors_text, fill="black", font=author_font)
draw.text(date_position, date_text, fill="black", font=author_font)

# # Save the image
# image_path = "/mnt/data/presentation_cover.png"
# image.save(image_path)

# Display the image
image.show()

# image_path
# ``` &#8203;:citation[oaicite:0]{index=0}&#8203;

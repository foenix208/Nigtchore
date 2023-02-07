from PIL import ImageFont, ImageDraw


draw = ImageDraw.Draw("img/img2")

# use a bitmap font
font = ImageFont.load("arial.ttf")

draw.text((10, 10), "hello", font=font)

# use a truetype font
font = ImageFont.truetype("arial.ttf", 15)

draw.text((10, 25), "world", font=font)
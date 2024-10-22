from PIL import Image, ImageDraw, ImageFont

# Open background and character images and combine into a comic panel
background = Image.open("background.png")
character = Image.open("Main_hero_character.png")

# Create a new image for the comic panel
panel = Image.new('RGB', (background.width, background.height))
panel.paste(background, (0, 0))
panel.paste(character, (50, 100), character)  # Position the character

# Optionally add dialogue
draw = ImageDraw.Draw(panel)
font = ImageFont.truetype("arial.ttf", 24)
draw.text((50, 50), "Hero: Let's begin the journey!", fill="white", font=font)

# Save the final comic panel
panel.save("comics/comic_panel_1.png")
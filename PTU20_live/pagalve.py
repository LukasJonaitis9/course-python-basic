from PIL import Image

image = Image.open('PTU20_live/ai_guy.webp')
new_size = (128,128)
resized = image.resize(new_size)
resized.save('PTU20_live/ai_guy.webp')
image.show()
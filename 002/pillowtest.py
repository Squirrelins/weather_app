from PIL import Image, ImageOps

# Create a new image and import
with Image.open('Flitter.png') as frogge:
    print(frogge.format, frogge.size, frogge.mode)

    # ImageOps
    frogge = ImageOps.flip(frogge)
    # Show image
    frogge.show()


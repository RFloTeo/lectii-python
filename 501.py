from PIL import Image

#deschidem imaginea, marime
poza = Image.open("bike.jpg")
dim = poza.size
# tuple latime, inaltime
print(dim[0], dim[1])
#resize
factor = 2
resized = poza.resize((factor * dim[0], factor * dim[1]))
print(resized.size)
#resized.show()
#rotate
rotated = poza.rotate(765) #90, 180, 270 pentru sfert de cerc
#grayscale
gray = poza.convert('L')
resized2 = gray.resize((factor * dim[0], factor * dim[1]))

#crop
#stanga, sus, dreapta, jos
box = (600,500,2520,1580)
cropped = poza.crop(box)
cropped.show()
print(cropped.size)

#saving
resized2.save('bike_gray.jpg')

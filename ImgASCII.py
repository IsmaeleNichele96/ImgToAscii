#Importo le librerie
from PIL import Image
import matplotlib.pyplot as plt
#do il path dell'immagine
img_path = r'C:\Users\niche\wa-git\python\ImgASCII\img\ismaPiccolo.png'
#prendo l'immagine e la mostro e schermo
img = plt.imread(img_path)
print(img.shape)
plt.imshow(img)
#prendo l'immagine e la mostro a schermo in un'altra maniera
emma= Image.open(img_path)
print("{}x{}".format(emma.width, emma.height))
#ciclo i pixel nell'immagine tramite getdata
for pixel in emma.getdata():
    print(pixel)
#trasformo l'immagine da colori in bianco e nero e la rendo più piccola usando il resize
greyscale = emma.convert("LA")
plt.imshow(greyscale)
reduced = greyscale.resize((96,96))
plt.imshow(reduced)
#questi saranno i caratteri utilizzati per riprodurre l'immagine in ASCII
chars = ["@", "#", "$","_", "|", "-", "&", "=", "£"]
pixel_tuple = reduced.getdata()[0]
print(pixel_tuple[0])
#divido il massimo+1 della scala di colori(max 255) per il numero di caratteri dati, così, in base alla scala di grigi, verranno mostrati determinati caratteri(es da 0 a 42 verrà mostrata @, da 42 a 84 verrà mostrata #, ecc)
num_intervals = int(256/len(chars))
print(num_intervals)

div = pixel_tuple[0]/num_intervals
print(chars[int(div)])

ascii_string = ""

for px in reduced.getdata():
    intervals = min(max(int(px[0] / num_intervals), 0), len(chars) - 1)
    ascii_string += chars[intervals]

print(ascii_string)

for i in range(0, len(ascii_string), reduced.width):
    print(ascii_string[i:i+reduced.width])


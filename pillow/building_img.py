from PIL import Image
import os
from pillow.basics import file_path


FOLDER_OUTPUT = "./output"

if not os.path.exists(FOLDER_OUTPUT):
    os.mkdir(FOLDER_OUTPUT)

## Criação de nova imagem => 3 parametros de entrada : molde (rgb), size (larg, alt), cor (se não passar cor cria totalmente preta) 
## A função get pixel começa com sistema de coordenada (0,0), na extremidade esquerda

# image = Image.new("RGB", (400, 300), (255, 130, 0))
class Create:

    def __init__(self):
    
        self.image = Image.open(file_path("imagem.jpeg"))
        
    
    def create (self, size):

        self.image = Image.new("RGB",(size, size),(255, 255, 255))
        self.size = size

        for x in range(size):
            for y in range(size):
                if y < x:
                    self.image.putpixel((x,y),(123, 48, 12))
    
        self.image.show()

    def save(self):
         self.image.save(f"{FOLDER_OUTPUT}/imege{self.size}.jpg", 'JPEG')
    

image = Create()
image.create(400)
image.save()

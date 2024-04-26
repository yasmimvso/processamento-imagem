from PIL import Image
import os


INPUT_FOLDER = "input"

# os.path.join(INPUT_FOLDER, "imagem.jpeg")
def file_path(file):
    return os.path.join(INPUT_FOLDER, file)

image = Image.open(file_path("imagem.jpeg"))


print(image.getpixel((300, 200))) # cada pixel tem que ser passado em escala de coordenada
                                  # é retornado uma tupla de cores
                                  # tupla: geralmente trabalhando com rpg
                                  # PNG permite reconhecer transparencia, tanto que em imagens nessa configuração é retornado uma tupla de 4 coordenadas, quanto mais perto do 0 mais transparente, quando mais perto do 255 mais opaco
image.putpixel((50, 200), (0, 0, 0)) # passar tupla da coordenada x,y e tupla da coordenada de cores
image.show()


# RGB está entre 0 e 255, representa 1 byte
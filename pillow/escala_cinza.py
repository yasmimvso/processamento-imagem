
from PIL import Image
from basics import file_path

## branco e preto são a mesma cor (ausencia de cor), variada apenas pelo tom de brilho
## O RGB não distingue essa luminosidade, tons de cinza acabam tendo valores de coordenadas redendantes

## precisamos apenas do parametro de luminancia para trabalahr com dados em escala de cinza
## para tranformar em escala de cinza, podemos levar em consideração o comportamento citado: as coodenadas tem cores similares ~ iguais

## O mais indicado seria fazer uma media ponderada, dado que temos perceções diferentes das cores azul, verde e vermelho (com maior peso para o verde)
def grayscale(image):

    width, height = image.size
    
    buff = Image.new("RGB", (width, height))

    for x in range(width):
        for y in range(height):
            pixL = image.getpixel((x,y))
            mid = int(0.3*pixL[0] + 0.59*pixL[1] + 0.11*pixL[2])
            buff.putpixel((x,y) , (mid, mid, mid))

    return buff

if __name__ == "__main__":

    image = Image.open(file_path("imagem.jpeg"))
    gray = grayscale(image)
    gray.save("../output/gray.jpeg", 'JPEG')
    gray.show()
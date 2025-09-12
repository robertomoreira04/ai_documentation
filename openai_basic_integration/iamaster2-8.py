# exemplo de chamada usando geração de imagens

from openai import OpenAI

client = OpenAI(
    api_key = 'api_key'
)

response = client.images.generate(
    model='dall-e-3',
    prompt='', #prompt para gerar a imagem
    size='1024x1024', #tamanho das imagens 
    quality='standard', #qualidade (standard, hd..)
    n=1, # número das imagens 
) 

image_url = response.data[0].url
print(image_url)


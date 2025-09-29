# traduzindo textos com deep translator 

from deep_translator import GoogleTranslator

langs_dict = GoogleTranslator().get_supported_languages(as_dict=True)

text = 'Estou estudando processamento de linguagem natural'

translated_text = GoogleTranslator(
    source = 'pt',
    target = 'en'
).translate(text)

print(translated_text)

texts = [
    'Eu sou desenvolvedor de software',
    'Estou disponível para entrevistas',
    'Manda uma mensagem no 8496277529',
         ]

translated_itens = GoogleTranslator(
    source='pt',
    target='en'
).translate_batch(texts)

print(translated_itens)
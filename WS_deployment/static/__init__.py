'''
'''
import os
import random

def generate_random_words(numero_resultados):
    '''
    '''
    # Listas de palabras
    palabras = ["camisa", "pantalon", "vestido", "tenis", "celular", "computadora", "libro", "juguete", "electrodoméstico", "mueble", "balón", "teclado", "cargador", 
                "botella", "aretes", "lentes", "funda", "reloj", "suéter"]

    # Lista de adjetivos
    adjetivos = ["nuevo", "usado", "barato", "caro", "de buena calidad", "de marca", "original", "importado"]

    # Lista para almacenar resultados
    lista = []

    for _ in range(numero_resultados):
        tipo = random.choice(["palabra", "oracion"])
        if tipo == "palabra":
            resultado = random.choice(palabras)
        else:
            palabra = random.choice(palabras)
            adjetivo = random.choice(adjetivos)
            resultado = f"u{'na' if palabra[-1] == 'a' else 'n' } {palabra} {adjetivo}"
        
        lista.append(resultado)
    
    return lista

from .PY.URL_scrapper import main as ProductAttributes
from .PY.Word_scrapper import main as WordAttributes

__all__ = [
    'ProductAttributes',
    'WordAttributes',
    'generate_random_words'
]

# =============== DEBUGGING ===============
if __name__ == '__main__':
    os.system('cls')
    
    word_scrapper  = WordAttributes(
        words_list = generate_random_words(3),
        verbose    = True
    )

    url_scrapper = ProductAttributes(
        verbose  = True
    )
    word_data = word_scrapper.get_words_into_URLs()

    for word in word_data.keys():
        url_scrapper.update_data(URL = word[''])
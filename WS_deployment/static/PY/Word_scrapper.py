import os
import random
import time
import requests
import asyncio
import threading
import multiprocessing
import aiohttp
from bs4 import BeautifulSoup

class main:
    # =============== CONSTRUCTOR ===============
    def __init__(self,words_list:list[str],verbose:bool = False,daemon:bool = False):
        '''
        '''
        # Defining the variables
        self.words_list = words_list
        self.verbose    = verbose
        self.daemon     = daemon
        self.__inform("Class initialized correctly...")

        # If class instanced as a daemon, loads soup automatically
        if self.daemon:
            self.__load_words_into_URLs()


    # =============== PRIVATE METHODS ===============
    def __inform(self,message:str):
        '''
        Method used to print messages in console depending on `verbose` flag.

        ### Args:
        * message (str): The message to be printed in console
        '''
        if self.verbose: print(message)
  
    async def __fetch_data(self,index:int,word:str,url:str,words_urls:dict):
        '''
        '''
        counter = 0
        while counter < 3:
            try:
                response = requests.get(url)

                if response.status_code in [200]:
                    data = self.__load_items_page(response.text)
                    words_urls[word] = {
                        'word'  : word,
                        'stage' : f"Codigo de respuesta: {response.status_code}",
                        'link'  : url,
                        'items_found' : data['items'],
                        'links_found' : data['links'],
                    }
                    self.__inform(f"({index}) {url} .- Codigo {response.status_code}")
                    return
                
                elif response.status_code in [404]:
                    words_urls[word] = {
                        'word' : word,
                        'stage' : f"Codigo de respuesta: {response.status_code}",
                        'link' : url,
                    }
                    self.__inform(f"({index}) {url} .- Codigo {response.status_code}")
                    return
            
            except requests.exceptions.InvalidURL as ex:
                words_urls[word] = {
                    'word' : word,
                    'stage' : f"Invalid URL",
                    'link' : url
                }
                self.__inform(f"({index}) {word} .- Invalid URL")
                return
            
            counter += 1
       
        words_urls[word] = {
                    'title' : word,
                    'stage' : 'No response from server',
                    'link' : url
                }
        
        self.__inform(f"({index}) {word} .- Tried 3 times, no response...")
            
    def __load_items_page(self,HTML_code:str):
        '''
        '''
        soup = BeautifulSoup(HTML_code,'lxml')
        items = [item.get_text() for item in soup.find_all('span',{'class':'ui-search-search-result__quantity-results'})][0]
        grid = soup.find('ol')
        links = [element.get('href') for element in grid.find_all('a')]

        return {
            "items" : items,
            "links" : links
        }
    
    def __load_words_into_URLs(self):
        '''
        '''
        execution_time = time.time()
        base_url = "https://listado.mercadolibre.com.mx/celulares#D[A:celulares]"
        replacement = "celulares"
        
        self.words_urls, threads, loops = {}, [], []

        # Requesting the urls in different threads
        for index,word in enumerate(self.words_list):
            self.words_urls[word] = False

            url_2_check = base_url.replace(replacement,word.replace(' ','-'))

            new_loop = asyncio.new_event_loop()
            loop_stopped_event = asyncio.Event()
            thread = threading.Thread(target=start_loop, args=(new_loop, loop_stopped_event))
            thread.start()
            asyncio.run_coroutine_threadsafe(self.__fetch_data(index,word,url_2_check,self.words_urls), new_loop)
            loops.append(new_loop)
            threads.append(thread)

        # Validating until all URLs are requested
        while True:
            pending = 0
            for key in self.words_urls.keys():
                if type(self.words_urls[key]) == bool: pending += 1
            if pending > 0: time.sleep(0.5)
            else: break

        # Closing opened loops and threads.
        for loop in loops:
            loop.call_soon_threadsafe(loop.stop)
        for thread in threads:
            thread.join()
        
        self.__inform(f"({len(self.words_urls)}) URLS found...")
        self.__inform(f"Execution time for validating all URL's: {time.time() - execution_time:.2f} seconds")

    # =============== PUBLIC METHODS ===============
    def get_words_into_URLs(self):
        self.__load_words_into_URLs()
        return self.words_urls

def start_loop(loop:asyncio.AbstractEventLoop, loop_stopped_event:asyncio.Event):
    """
    Starts an asyncio event loop in a separate thread.

    ### Args:
    * `loop` (asyncio.AbstractEventLoop): The asyncio event loop to run.
    * `loop_stopped_event` (asyncio.Event): An event to set when the loop is stopped.

    ### Notes:
    * Sets the provided loop as the current event loop.
    * Runs the loop forever until it is externally stopped.
    * Sets the loop_stopped_event once the loop stops running.
    """
    asyncio.set_event_loop(loop)
    loop.run_forever()
    loop_stopped_event.set()


# =============== DEBUGGING ===============
if __name__ == '__main__':
    os.system('cls')
    import pyperclip as pc
    
    def generate_random_words(numero_resultados):
        '''
        '''
        # Listas de palabras
        palabras = ["coche", "pantalon", "vestido", "tenis", "celular", "computadora", "libro", "juguete", "electrodoméstico", "mueble", "balón", "teclado", "cargador", 
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
    
    
    test = main(
        words_list = generate_random_words(15),
        verbose = True,
        # daemon  = True
    )

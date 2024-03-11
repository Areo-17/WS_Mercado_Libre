import os
import random
import time
import requests
import asyncio
import threading
from bs4 import BeautifulSoup

class main:
    # =============== CONSTRUCTOR ===============
    def __init__(self,words_list:list[str] = None,verbose:bool = False,daemon:bool = False):
        '''
        '''
        # Defining the variables
        self.words_list = words_list
        self.verbose    = verbose
        self.daemon     = daemon
        self.__inform("Class initialized correctly...")

        # If class instanced as a daemon, loads soup automatically
        if self.daemon and words_list:
            self.get_words_into_URLs()


    # =============== PRIVATE METHODS ===============
    def __inform(self,message:str):
        '''
        Method used to print messages in console depending on `verbose` flag.

        ### Args:
        * message (str): The message to be printed in console
        '''
        if self.verbose: print(message)
  
    async def __fetch_data(self, index: int, word: str, url: str, words_urls: dict):
        """
        Fetches data for a given word and URL.

        ### Args:
        * `index` (int): Index of the word in the list.
        * `word` (str): The word to search for.
        * `url` (str): The URL to fetch data from.
        * `words_urls` (dict): Dictionary to store word information.

        ### Returns:
        * None
        """

        counter = 0
        while counter < 3:
            try:
                with requests.get(url) as response:
                    if response.status_code == 200:
                        data = self.__load_items_page(response.text)
                        words_urls[word] = {
                            'word': word,
                            'stage': f"Codigo de respuesta: {response.status_code}",
                            'link': url,
                            'items_found': data['items'],
                            'links_found': data['links'],
                        }
                        self.__inform(f"({index}) {url} .- Codigo {response.status_code}")
                        return

                    elif response.status_code == 404:
                        words_urls[word] = {
                            'word': word,
                            'stage': f"Codigo de respuesta: {response.status_code}",
                            'link': url,
                        }
                        self.__inform(f"({index}) {url} .- Codigo {response.status_code}")
                        return

            except requests.exceptions.InvalidURL as ex:
                words_urls[word] = {
                    'word': word,
                    'stage': f"Invalid URL",
                    'link': url
                }
                self.__inform(f"({index}) {word} .- Invalid URL")
                return

            counter += 1

        words_urls[word] = {
            'title': word,
            'stage': 'No response from server',
            'link': url
        }
        self.__inform(f"({index}) {word} .- Tried 3 times, no response...")
            
    def __load_items_page(self,HTML_code:str):
        """
        Parses HTML code to extract relevant data.

        ### Args:
        * `HTML_code` (str): The HTML code to parse.

        ### Returns:
        * `dict`: A dictionary containing extracted data like items and links.
        """
        soup = BeautifulSoup(HTML_code,'lxml')
        items = [item.get_text() for item in soup.find_all('span',{'class':'ui-search-search-result__quantity-results'})][0]
        grid = soup.find('ol')
        links = [element.get('href') for element in grid.find_all('a')]

        return {
            "items" : items,
            "links" : links
        }
    
    async def __load_words_into_URLs(self):
        """
        Fetches data for all words in the list using asyncio.

        ### Returns:
        * `dict`: A dictionary containing information for each word and URL.
        """
        execution_time = time.time()
        base_url = "https://listado.mercadolibre.com.mx/celulares#D[A:celulares]"
        replacement = "celulares"

        self.words_urls = {}
        tasks = []
        for index, word in enumerate(self.words_list):
            self.words_urls[word] = False
            url_2_check = base_url.replace(replacement, word.replace(' ', '-'))
            tasks.append(self.__fetch_data(index, word, url_2_check, self.words_urls))

        await asyncio.gather(*tasks)
        self.__inform(f"Execution time for validating all URL's: {time.time() - execution_time:.2f} seconds")
        return self.words_urls

    # =============== PUBLIC METHODS ===============
    def get_words_into_URLs(self):
        """
        Fetches data for all words in the list using asyncio.

        ### Returns:
        * `dict`: A dictionary containing information for each word and URL.
        """
        return asyncio.run(self.__load_words_into_URLs())


# =============== DEBUGGING ===============
if __name__ == '__main__':
    os.system('cls')
    import pyperclip as pc
    
    def generate_random_words(words_limit:int = 10):
        '''
        Generates a list of random words and short sentences.

        ### Args:
        * `words_limit` (int,optional): The limit of words to generate.

        ### Returns:
        * `array` (list): The array with the random words and short sentences.

        ### Notes:
        * The words and the sentences were pre-selected, so they're not totally random.
        '''
        # Words list
        words = ["camisa", "pantalon", "vestido", "tenis", "celular", "computadora", "libro", "juguete", "electrodoméstico", "mueble", "balón", "teclado", "cargador", "botella", "aretes", "lentes", "funda", "reloj", "suéter"]

        # Adjectives list
        adjectives = ["nuevo", "usado", "barato", "caro", "de buena calidad", "de marca", "original", "importado"]

        # Results list
        array = []
        for _ in range(words_limit):
            type_search = random.choice(["word", "sentence"])
            if type_search == "word":
                result = random.choice(words)
            else:
                word = random.choice(words)
                adjective = random.choice(adjectives)
                result = f"u{'na' if word[-1] == 'a' else 'n' } {word} {adjective}"
            array.append(result)
        
        return array
    
    
    test = main(
        words_list = generate_random_words(),
        verbose = True,
        # daemon  = True
    )

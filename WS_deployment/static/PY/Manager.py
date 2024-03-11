import os
import random
import time

import asyncio
import threading

from .Word_scrapper import main as WordManager
from .URL_scrapper import main as URLScrapper

class main:
    # =============== CONSTRUCTOR ===============
    def __init__(self,verbose:bool = False):
        """
        Class to manage generating random words and fetching product attributes.

        ### Args:
        * `verbose` (bool, optional): Flag to enable verbose output. Defaults to False.
        """
        # Setting the attributes
        self.verbose = verbose

        # Setting the dependency classes
        self.word_manager = WordManager(
            verbose = self.verbose
        )

        self.url_scrapper = URLScrapper(
            verbose = self.verbose
        )

    # =============== PRIVATE METHODS ===============
    def __inform(self,message:str):
        '''
        Method used to print messages in console depending on `verbose` flag.

        ### Args:
        * message (str): The message to be printed in console
        '''
        if self.verbose: print(message)

    async def __get_item_attributes(self,url:str,data_items:dict):
        """
        Fetches attributes for a given URL.

        ### Args:
        * `url` (str): The URL to fetch data from.
        * `data_items` (dict): Dictionary to store product information.
        """
        self.url_scrapper.update_data(url)
        data_items[url] = self.url_scrapper.get_all_attributes()
        
    async def __load_attributes_from_products(self,list_of_URLs:list):
        """
        Fetches attributes for a list of product URLs using asyncio.

        ### Args:
        * `list_of_URLs` (list): List of URLs to fetch data from.

        ### Returns:
        * `dict`: Dictionary containing product attributes for each URL.
        """
        execution_time = time.time()

        data_items = {}
        tasks = []
        for url in list_of_URLs:
            data_items[url] = False
            tasks.append(self.__get_item_attributes(url, data_items))

        await asyncio.gather(*tasks)
        self.__inform(f"Execution time for processing all URLs: {time.time() - execution_time:.2f} seconds")
        return data_items

    # =============== PUBLIC METHODS ===============
    def generate_random_words(self,words_limit:int = 10):
        '''
        Generates a list of random words and short sentences.

        ### Args:
        * `words_limit` (int,optional): The limit of words to generate.

        ### Returns:
        * `array` (list): The array with the random words and short sentences.

        ### Notes:
        * The words and the sentences were pre-selected, so they're not totally random.
        '''
        words = ["camisa", "pantalon", "vestido", "tenis", "celular", "computadora", "libro", "juguete", "electrodoméstico", "mueble", "balón", "teclado", "cargador", "botella", "aretes", "lentes", "funda", "reloj", "suéter"]
        adjectives = ["nuevo", "usado", "barato", "caro", "de buena calidad", "de marca", "original", "importado"]
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
    
    def get_attributes_from_products(self,list_of_URLs:list):
        """
        Fetches attributes for a list of product URLs using asyncio.

        ### Args:
        * `list_of_URLs` (list): List of URLs to fetch data from.

        ### Returns:
        * `dict`: Dictionary containing product attributes for each URL.
        """
        return asyncio.run(self.__load_attributes_from_products(list_of_URLs))

if __name__ == '__main__':
    os.system('cls')

    test = main(
        verbose = True
    )
    
    test.word_manager.words_list = test.generate_random_words(3)

    for word in test.word_manager.get_words_into_URLs().keys():
        
        item = test.word_manager.words_urls[word]

        test.__load_attributes_from_products(item['links_found'])

        break
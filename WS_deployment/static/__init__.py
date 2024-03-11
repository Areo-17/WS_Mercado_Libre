'''
'''
import os
from .PY.Word_scrapper import main as WordManager
from .PY.URL_scrapper import main as URLScrapper
from .PY.Manager import main as Manager

__all__ = [
    'WordManager',
    'URLScrapper',
    'Manager'
]

# =============== DEBUGGING ===============
if __name__ == '__main__':
    os.system('cls')
    
    word_scrapper  = WordManager(
        words_list = Manager.generate_random_words(3),
        verbose    = True
    )

    url_scrapper = URLScrapper(
        verbose  = True
    )
    word_data = word_scrapper.get_words_into_URLs()

    for word in word_data.keys():
        url_scrapper.update_data(URL = word[''])
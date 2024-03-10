import os
import time

from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify

from static import ProductAttributes
from static import WordAttributes
from static import generate_random_words

app = Flask(__name__)
app.template_folder = 'static/HTML'

@app.route('/', methods=['GET'])
def welcome():
    return render_template('index.html')

@app.route('/ScrappingURL', methods=['POST'])
def scrape_url():
    
    # Declaring the item and their attributes
    item = ProductAttributes(
        URL     = request.form['url'],
        verbose = True,
        daemon  = True,
    )
    item_attributes = item.get_all_attributes()
    
    return render_template('scrapped_url.html',
        name        = item_attributes["name"],
        price       = item_attributes["price"],
        description = item_attributes["description"],
        images      = item_attributes["images"]
    )

@app.route('/ScrappingWord',methods=['POST'])
def scrape_word():
    words = request.form['word'].split(',')
    words = generate_random_words(3) if words[0] == '' else words

    scrapper = WordAttributes(
        words_list = words,
        daemon     = True,
        verbose    = True
    )

    return render_template('scrapped_word.html',
        words = scrapper.words_urls
    )

@app.route('/Detail',methods=['POST'])
def get_items():
    links = request.form['links'].replace("'",'').replace('[','').replace(']','').split(',')
    word = request.form['word']
    scrapper = ProductAttributes(URL = '')
    items = []
    for links in links:
        print(f"\n\nEste es el link que se consulta {links}\n\n")
        scrapper.URL = links
        items.append(scrapper.get_all_attributes())
    


    


if __name__ == '__main__':
    os.system('cls')
    app.run(debug=True)
import os

from flask import Flask
from flask import request
from flask import render_template

from flask_mysqldb import MySQL

from static import URLScrapper
from static import WordManager
from static import Manager

app = Flask(__name__)
app.template_folder = 'static/HTML'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '252378dm'
app.config['MYSQL_DB'] = 'flaskcontacts'
mysql = MySQL(app)

@app.route('/', methods=['GET'])
def welcome():
    return render_template('index.html')

@app.route('/ScrappingURL', methods=['POST'])
def scrape_url():
    # Declaring the item and their attributes
    item = URLScrapper(
        URL     = request.form['url'],
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
    manager = Manager()
    words = request.form['word'].split(',')
    words = manager.generate_random_words(3) if words[0] == '' else words
    scrapper = WordManager(
        words_list = words,
        daemon     = True,
    )
    return render_template('scrapped_word.html',
        words = scrapper.words_urls
    )

@app.route('/Detail',methods=['POST'])
def get_items():
    links = request.form['links'].replace("'",'').replace('[','').replace(']','').split(',')
    word = request.form['word']
    manager = Manager()
    items = manager.get_attributes_from_products(links)
    return render_template('word_detail.html',
        word = word,
        data = items
    )
        
    


    


if __name__ == '__main__':
    os.system('cls')
    app.run()
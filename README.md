# **MercadoLibre Web scrapper**

Hello! Welcome to the our web scrapper project.
MercadoLibre is an online shopping webpage that offers a variety of products of many categories, such as technology, clothing, supermarket, pets, etc.
The main objective of our web scrapper is to offer a web app that allows the user enter a word, wich will be browsed on MercadoLibre website, and returns the multiple products that are related with that search on the website, showing the price, name, description and images of the product.

## Where will the scrapper be developed?
The application will be developed on Python language, for this, please install [Visual Studio Code](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiF1fa1uMqEAxVLIEQIHTcjBNEQFnoECAwQAQ&url=https%3A%2F%2Fcode.visualstudio.com%2F&usg=AOvVaw15O90sm1ios8AUpw56hCml&opi=89978449)

## Cloning the repository
To clone the GitHub repository, open Git Bash, choose the path of your preference and write the command `git clone git@github.com:Areo-17/WS_Mercado_Libre.git`.

# Web scrapper development

## Adapting the work environment
First of all, create the folder in which you will be working the project, you have to create this from the file explorer of your OS. After this, open Visual Studio Code and choose the created folder.

### Creating a virtual environment
Once you have opened the folder, create a virtual environment. For this, open the terminal in Visual studio code with the command ``ctrl+` ``, or `ctrl+ñ` if you have a keyboard with the "ñ" letter.
With the opened termninal, navigate to the path of your folder (Usually, once you open the terminal it is on the path of your active folder) just as the image.
![Captura de pantalla (3419)](https://github.com/Areo-17/WS_MercadoLibre/assets/144394013/6ca9e5d6-7a3b-443b-a573-38d396c43c6f)
Now that you are on the selected path, write the following command ` python -m venv venv` on the terminal and press the  enter button. 
![Captura de pantalla (3420)](https://github.com/Areo-17/WS_MercadoLibre/assets/144394013/c500bbde-3859-45a8-bd10-37c4c8cca11d)
The execution of the previous command will create you a folder that contains your virtual environment. Inside this folder you can find 3 other folders that are "Include", "Lib", and "Scripts". Do not modify any of these folders.
![Captura de pantalla (3421)](https://github.com/Areo-17/WS_MercadoLibre/assets/144394013/f0db3b2f-c6bb-4e06-a2bb-f3302a724821)
The purpose of creating a virtual environment is to work under specific libraries (that we are going to install later) and control the versions of our app, avoiding conflicts with other versions and also indicating which libraries and their versions we are using for the project.

### Activating and deactivating the virtual environment
To work propperly in our project we have to activate the virtual environment. To achieve this, write the command `venv\Scripts\activate` on the terminal and press the enter button. Make sure that you are in the path in which the virtual environment was created.
![Captura de pantalla (3423)](https://github.com/Areo-17/WS_MercadoLibre/assets/144394013/49cea558-b4a7-4f37-8d48-7e56e3967d9d)
![Captura de pantalla (3426)](https://github.com/Areo-17/WS_MercadoLibre/assets/144394013/b75aa288-ac54-4d20-9b16-331a703c2db2)

If `(venv)` shows up to the left of your path in the terminal the virtual environment has been activated successfully. You have to keep it activated until you close the file.

To deactivate the virtual environment, write the command `venv\Scripts\deactivate` on the terminal and press the enter button. You should do this everytime you are going to stop working on your code.
![Captura de pantalla (3425)](https://github.com/Areo-17/WS_MercadoLibre/assets/144394013/96ce4d73-2880-4759-a766-68912e2e11b9)

If `(venv)` dissapears from left of your path in the terminal, then the virtual environment has been deactivated successfully.

## Installing libraries

In programming, libraries (also known as modules) are sets of predefined functions, classes and constants that provide specific functionality that can be reused by other programs. They offer a wide range of tools to perform various tasks without having to write all the code from scratch. In a few words, libraries help us to develop a more efficient code through special function (methonds).
For this project, we are going to install "bs4", "requests", and "Flask". In Python, the libraries are installed with the `pip install` command. On your active virtual environment, install the already mentioned libraries with the following commands:
```
pip install bs4
pip install lxml
pip install requests
pip install Flask
```
You have to do it one by one, take a look of the following example:
![Captura de pantalla (3427)](https://github.com/Areo-17/WS_MercadoLibre/assets/144394013/6a0a9479-dd8d-4b3e-8b30-4361046c0d25)

***NOTE: Before install them in your virtual environment, you have to install these libraries (in the same way) on your global Python. Open the cmd of your PC and install them.***
![Captura de pantalla (3428)](https://github.com/Areo-17/WS_MercadoLibre/assets/144394013/851dbf0f-e05c-4d49-b82f-965a5ca78a6a)

## Starting to code

Create a Python file by right-clicking on the venv folder and choosing the option "New File...", it will automatically create a file, name it as *"Product_scrapper.py"*.
And now we have the first Python file in which we will be working on. Let's start importing the libraries on the first three lines of code.
![Captura de pantalla (3429)](https://github.com/Areo-17/WS_MercadoLibre/assets/144394013/dfb383bb-b476-4e18-a412-4778a79a2439)

Before continuing, let's see why we are using these libraries.
**bs4:** Extracts elements of HTML web pages.
**lxml:** It offers a wide range of functions for efficient parsing, manipulation, searching and generation of XML/HTML documents.
**requests:** Send and receive HTTP requests.
**time:** Used to measure times.
**json:** Encodes and decodes JSON data.

The next step is to declare our class. A class serves as a template for defining the properties (attributes) and behaviors (methods) that objects of that class will have.
The first function will be the initialization of recurring variables.
![Captura de pantalla (3430)](https://github.com/Areo-17/WS_MercadoLibre/assets/144394013/41a9fe46-f354-4838-8587-0c45225677b4)

`Class Scrapper`: declares a new class named Scrapper.

`def __init__(self, URL: str, verbose: bool = False, daemon: bool = False)`: defines the constructor method using the __init__ special method, which is called whenever a new instance of the class is created.

`self` refers to the current object instance. This method takes three parameters: 
**URL**: A required string parameter representing the URL to be scraped.
**verbose**: An optional boolean parameter (default: False), indicating whether verbose logging messages should be printed.
**daemon**: An optional boolean parameter (default: False), determining whether the class should behave as a daemon (explained later).

The triple-quoted strings (''') before the code block define the docstring, which provides a brief description of the class and its parameters. It improves code readability and understanding.

`self.URL = URL`: Assigns the provided URL parameter to the instance attribute self.URL for storage within the object.
This is repeated for `verbose` and `daemon`, creating instance attributes associated with the respective parameters' values.

`self.__inform("Class initialized correctly...")`: This line calls a private method (`__inform`) within the class, potentially to print a message indicating successful class initialization. The 
double underscores (__) before the method name convention in Python make this method private, meaning it can only be accessed directly within the class and not from external code.

`if self.daemon`: checks if the daemon parameter is set to True. If so, the code block within the if statement executes:

`self.load_soup()`: This line calls another method, load_soup, within the class, to load the content from the URL and parse it using a web scraping library like BeautifulSoup (not shown in this code snippet).

Let's continue with the private and public methods that were mentioned in the previous explanation.
![Captura de pantalla (3431)](https://github.com/Areo-17/WS_MercadoLibre/assets/144394013/b485aebf-6fce-4c65-bfa8-a073fb429083)

`def __inform(self, message: str)`: declares a private method named __inform.

`message: str` is a required parameter of type str, representing the message to be printed.

`if self.verbose`: checks if the instance attribute self.verbose is set to True. If True, the code inside the if block executes: `print(message)` prints the provided message to the console.

`def load_soup(self)`: declares a public method named load_soup.

`execution_time = time.time()`: measures the current time using the time.time() function and stores it in the execution_time variable.

`response = requests.get(self.URL)` sends a GET request to the self.URL attribute (an URL) using the requests library and stores the response object in response.

`if response.status_code == 200`: checks if the response status code is 200 (indicating success). If True, the code inside the if block executes:

`html = response.text`: extracts the text content from the response and stores it in html.

`self.soup = BeautifulSoup(html, 'lxml')` parses the html content using the BeautifulSoup library and the lxml parser, and sets the result as the soup attribute of the object.

`else:` (if the status code isn't 200):

`self.soup = None` sets the soup attribute to None to indicate that no soup (parsed content) was created.

`self.__inform(f"Execution time for generating soup: {time.time() - execution_time}")` calls the private  `__inform` method and prints a message to the console (if verbose is True) showing the time taken to generate the soup.

The following step is to start to do the functions for the products characteristics that we are going to extract:

### Product name

![Captura de pantalla (3432)](https://github.com/Areo-17/WS_MercadoLibre/assets/144394013/74293519-fa36-4e61-b580-2b4126b6f353)

`#name function extracts the name of the product.` This is a line comment and does not affect the code's execution. It describes the purpose of the following function.

`def name(self)`: defines a function named name within the class.

`attributes1 = self.soup.find('div', class_= 'ui-pdp-container__col col-2 mr-32')` searches within the soup attribute, that is a BeautifulSoup object, for the first `<div>` element with the class names `'ui-pdp-container__col'`, `'col-2'`, and `'mr-32'`. This element corresponds to the product information section based on the CSS selectors of the HTML code of MercadoLibre. The result is stored in the variable `attributes1`.

`nm = attributes1.find('h1', class_ = 'ui-pdp-title')` searches within the previously found element, attributes1, for the first `<h1>` element with the class name `'ui-pdp-title'`. This the product name element. The result is stored in the variable `nm`.

`if nm`: checks if the nm variable contains a value (meaning the product name element was found). If True, the code block within the if statement executes:

`self.nametxt = nm.get_text()` extracts the text content of the product name element and assigns it to the nametxt attribute of the object.

`else:` (if the product name element wasn't found) then it executes:

`print('The product name was not found.')` which prints an error message to the console.

### Product price

![Captura de pantalla (3433)](https://github.com/Areo-17/WS_MercadoLibre/assets/144394013/78ef0995-2233-4dee-a4dc-72aef8b7d8c7)

 `def price(self)`: defines a function named price within the class.

`attributes2 = self.soup.find('div', class_= 'ui-pdp-container__col col-2 mr-32')` searches within the soup attribute for the first `<div>` element with the same class names as in the previous code block. This is because the price might also be within that area. The result is stored in the variable `attributes2`.

`pr = attributes2.find('span', class_ = 'andes-money-amount__fraction')` searches within the previously found element (attributes2) for the first `<span>` element with the class name `'andes-money-amount__fraction'`. This class name indicates the price portion. The result is stored in the variable `pr`.

`if pr`: checks if the pr variable contains a value (meaning the price element was found). If True, the code block within the if statement executes:

`self.prices = pr.get_text()` extracts the text content of the price element and assigns it to the prices attribute of the object.
`else:` (if the price element wasn't found) and the executes the following code line:

`print('The product price was not found.')` which prints an error message to the console.

### Product description

![Captura de pantalla (3437)](https://github.com/Areo-17/WS_MercadoLibre/assets/144394013/0afbb559-f02e-4a13-917b-c8fb74983720)

`#description function extracts the description of the product`: this is a line comment and does not affect to the script execution.

`def description(self)`: defines a function named description within the class (presumably the Scrapper class).

`attributes3 = self.soup.find('p', class_= 'ui-pdp-description__content')` searches within the soup attribute for the first `<p>` element with the class name `'ui-pdp-description__content'`. This class name indicates the product description section. The result is stored in the variable `attributes3`.

`if attributes3:` checks if the attributes3 variable contains a value (meaning the description element was found). If True, the code block within the if statement executes:

`self.descriptions = attributes3.get_text()` extracts the text content of the description element and assigns it to the descriptions attribute of the object.

`else:` (if the description element wasn't found), executes the following code line:

`print('The product description was not found.')` which prints an error message to the console.

### Product images

![Captura de pantalla (3438)](https://github.com/Areo-17/WS_MercadoLibre/assets/144394013/54dcd3ea-de88-4087-a0ef-a014d99fd224)

`#image function extracts all the URLs of the images of the product`. This is a comment line and describes the function's purpose and does not affect to the script execution.

`def image(self)`: defines a function named image within the class.

`img_tags = self.soup.select('div[class*="ui-pdp-gallery"] span[class*="ui-pdp-gallery"] figure[class*="ui-pdp-gallery"] img')` uses the select method on the soup attribute. This method allows selecting elements based on a CSS selector. Here, it targets:
`<div>` elements with class names containing "ui-pdp-gallery".

Within those `<div>`, it searches for `span` and figure elements also containing "ui-pdp-gallery"
Finally, it selects the img elements within these nested elements

The results are stored in the variable `img_tags`.

`self.images = []` creates an empty list named images as an attribute of the object. This list will store the image URLs.

`for im in img_tags`: iterates through each element in the img_tags list (which contains the image elements). 

For each element (im):
`img = im.get('data-zoom')` extracts the value of the attribute named "data-zoom" from the current image element (im). This attribute contains the URL of the image.
`self.images.append(img)` appends the extracted image URL to the images list.

### Gathering all the attributes of the product

![Captura de pantalla (3439)](https://github.com/Areo-17/WS_MercadoLibre/assets/144394013/5efd3cbd-1415-4f8a-911a-1152d48da963)

`#all_attributes function recieves all the extracted characteristics of the product and prints them`. This is a comment line and describes the function's purpose and does not affect to the script execution.

`def all_attributes(self)`: defines a function named all_attributes within the class.

`start_time = time.time()` measures the current time and stores it in `start_time`. This is used later to calculate the execution time of the function.

`self.name()` calls the previously defined `name` function to extract the product name.

`self.price()` calls the previously defined `price` function to extract the product price.

`self.description()` calls the previously `defined` description function to extract the product description.

`self.image()` calls the previously defined `image` function to extract the product image URLs.

`all_def = { ... }` creates a dictionary named all_def. This dictionary will hold the extracted product characteristics as key-value pairs.
The keys are strings: "name", "price", "description", and "images".
The values are retrieved from the object attributes: `self.nametxt`, `self.prices`, `self.descriptions`, and `self.images`, which are populated by the called extractor functions.

`json_result = json.dumps(all_def, indent = 2)` uses the `json.dumps` function to convert the dictionary `all_def` into a JSON string. `indent = 2` is an optional argument that adds indentation for better readability.

`end_time = time.time()` measures the current time and stores it in `end_time`.

`self.time2 = end_time - start_time` calculates the difference between the start and end times, representing the execution time, and stores it in `self.time2`.

`print(f'The execution time of the product attributes is {self.time2} seconds.')` prints a formatted message displaying the calculated execution time in seconds.

`return json_result` returns the generated JSON string containing the product information.

### Testing the script

Now it's time to test our scrapper and we can do it from the same file.

![Captura de pantalla (3441)](https://github.com/Areo-17/WS_MercadoLibre/assets/144394013/fcc036a4-d091-4cfa-ba23-7837ac647482)

`if __name__ == '__main__':` checks if the current code is being executed as the main script (not imported as a module). This ensures the testing code only runs when the script is directly executed.

`link2 = 'https://www.mercadolibre.com.mx/...'` defines a variable link2 containing the URL of a product to be scraped for testing purposes. This URL is an example and can be replaced with any valid URL you want to test.

`test2 = Scrapper( URL = link2, verbose = True, daemon = True )` creates an instance (object) of the Scrapper class.

The constructor arguments are:
`URL = link2`: Sets the URL attribute to the test product link.
`verbose = True`: Enables verbose logging messages during the scraping process.
`daemon = True`: Sets the daemon flag to True, potentially indicating the class should operate in the background (its specific behavior depends on the implementation within the class).

`result = Scrapper.all_attributes(test2)` calls the all_attributes function of the Scrapper class, passing the `test2` object instance (containing the test URL) as an argument. This function collects and formats the product attributes. The result of this function call is stored in the `result` variable.

`print(result)` prints the value stored in the result variable. Since result is assigned the JSON string generated by the `all_attributes` function, this will print the extracted product information in JSON format.

### Running the file

To run the file, write the command `venv\Product_scrapper.py` just as the following image, and press enter. Note: You should be in the virtual environment.

![Captura de pantalla (3443)](https://github.com/Areo-17/WS_MercadoLibre/assets/144394013/1ff7dfd8-348a-4750-a9de-68221ec64745)

### Results

Congrats! You have scrapped a product. An example of the result would be the following one:

![WhatsApp Image 2024-02-27 at 9 10 36 AM](https://github.com/Areo-17/WS_MercadoLibre/assets/144394013/73caae3a-db9f-4726-8fc4-4a8e45f2595b)

### Scrapper requirements

To continue with the project, let's see the requirements of our scrapper. Write the comand `pip3 freeze > requirements.txt` on your active virtual environment.

![Captura de pantalla (3445)](https://github.com/Areo-17/WS_MercadoLibre/assets/144394013/da19e761-0c1b-48aa-89f7-324b1b76ac64)

It will create a .txt file with the requirements.

![Captura de pantalla (3446)](https://github.com/Areo-17/WS_MercadoLibre/assets/144394013/277af6b2-deb6-4ab2-9b16-f2fe8b9d5692)

## Scrapper deployment

A deployment is the process of moving software from a development environment to a production environment. In other words, it is the process of making your code accessible to end users.

For this stage of the project, we need to install two important tools: [Docker](https://www.docker.com/get-started/) and [Postman](https://www.postman.com/downloads/).
Once we have downloaded and installed them, let's leave them for while and continue on Visual Studio Code.

Create a new folder named "WS_deployment". This folder has to be inside the "WS_MercadoLibre" folder, but outside the venv folder. You have to create it from your file explorer, such as you did in the WS_MercadoLibre one. Inside "WS_deployment" add a duplicate of the *"Product_scrapper.py"* and *"requirements.txt"* files. To achieve this, right click on each one of the files and select the option *"Copy"*. Then, right click on the *"WS_deployment" folder and select the option *"Paste"*.
After that, create 3 files. The first one will be named *"WS_app.py"*, the second one *"Dockerfile"* and the third one *"docker-compose.yml"*. Your folder should look like this. To create a file, right click on the *"WS_deployment"* folder and select the option *"New File..."*.

### Creating a docker container

The *"Dockerfile"* file defines a recipe for building a Docker image that contains your Flask application and its dependencies. Fill it as the following image:

![Captura de pantalla (3448)](https://github.com/Areo-17/WS_MercadoLibre/assets/144394013/c92364fa-33ea-4aff-89e5-0bd7855f8875)

`COPY requirements.txt .` copies the requirements.txt file, which lists the Python dependencies needed for your application, from the host machine (your local system) to the working directory of the Docker image.

`RUN pip install -r requirements.txt` instructs the Docker image to run the pip command to install all the Python packages listed in the copied requirements.txt file. This ensures that the necessary libraries are available within the container environment.

`COPY . .` copies all files and directories from the current directory on the host machine (excluding the already copied requirements.txt) to the working directory of the Docker image. This essentially copies your entire application codebase into the container.

`EXPOSE 6000` exposes port 6000 inside the container. This allows external processes or other containers to access the application running on that port within the container.

`CMD ["flask", "run", "--host=0.0.0.0", "--port=6000"]`defines the default command to be executed when the container starts. The arguments of this command are:
Runs the `"flask"` command.
Uses the `"run"` subcommand to start the Flask development server.
Specifies `"--host=0.0.0.0"` to make the application accessible from any machine on the network (not just the host machine).
Sets `"--port=6000"` to run the application on the same port that was exposed earlier (port 6000).

The *"docker-compose.yml"* file  defines how to run the Flask application as a service. Fill it as the following image:

![Captura de pantalla (3449)](https://github.com/Areo-17/WS_MercadoLibre/assets/144394013/8cae0279-f610-4d5c-902e-1faa58f29b2c)

`version: '3.8'` specifies the Docker Compose file format version.

`services:` defines the section for defining services within the composition.

`flask-app:` creates a service named flask-app. This service will run the Flask application.

`build: .` instructs Docker Compose to build the Docker image for this service. The image will be built from the current directory (.) using the Dockerfile (if present) also in the current directory.

`ports:` defines how to map ports between the container and the host machine. `- "6000:6000"` maps port 6000 on the host machine (your local system) to port 6000 inside the container. This means any requests sent to port 6000 on the host will be forwarded to the application running on port 6000 within the container.

`volumes:` defines how to share data between the host machine and the container.  `- .:/WS_app` mounts the current directory (.) on the host machine to the */WS_app* directory within the container. This allows any changes made to your code files on the host machine to be reflected in the running container without rebuilding the image.

`environment:` defines environment variables to be set within the container. `- FLASK_APP=WS_app.py` sets the environment variable `FLASK_APP` to the value *WS_app.py*. This variable is used by the Flask application to identify the main application script.

Now that we have filled the necessary docker files, let's build the docker!

First, open the *"Docker Desktop"* app, continue without logging in with an account and let the application finish the "Starting the Docker Engine..." process. 

When te Docker app has already initialized, open your Git Bash, navigate to the directory in which you cloned the repository, and go to the folder in which *"WS_deployment"* is. Once you are there, write the command `docker compose up`. The screen should look like this:
![Captura de pantalla (3450)](https://github.com/Areo-17/WS_MercadoLibre/assets/144394013/84b4cea3-ae3e-4307-8ed0-bbc977ff3362)

Now, the docker is up!

### Testing the app's APIs on Postman 

Open Postman, click on the Workspace button that is on the left top of the window, create a workspace, select the POST mode on the created workspace, put the http link that docker gave you, in this case is `http://127.0.0.1:6000`, and add `/Scrapping`; the example look like this `http://127.0.0.1:6000/Scrapping`. After this, click in the *"Body"* button.

![Captura de pantalla (3452)](https://github.com/Areo-17/WS_MercadoLibre/assets/144394013/e37bea00-b8af-4eb8-9b47-bc5017838a3e)

from flask import Flask, render_template, url_for   
from sitepadaria import app

if __name__ == "__main__":
    app.run(debug=True)


#Para acessar o ambiente virtual
#Acessar cmd    
#cd C:\Users\vitor\Documents\Python\Site-Padaria
#python -m venv venv
#venv\Scripts\activate 
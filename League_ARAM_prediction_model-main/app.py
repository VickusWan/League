from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from db.tables import db, poke, champinfo, aram_data

load_dotenv()
database_url = os.getenv("DATABASE_URL")
print("Database URL:", database_url)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    champ_data = champinfo.query.with_entities(champinfo.champ_name, champinfo.image).all()
    return render_template('index.html', data=champ_data)

@app.route('/submit', methods=['POST'])
def handle_submit():
    selected_value = request.form
    print(selected_value)
    
    png_files = selected_value.getlist('dynamicDropdown')
    summonerName = selected_value.getlist('summonername')
    print(png_files)
    print('what is this', summonerName)
    
    champ_data = champinfo.query.with_entities(champinfo.champ_name, champinfo.image).all()
    return render_template('index.html', data=champ_data)

if __name__ == "__main__":
    app.run(debug=True)
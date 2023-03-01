from flask import Flask, render_template
from dotenv import load_dotenv

import os

app = Flask(__name__)
load_dotenv()

@app.route('/')
def index():
    app_id = os.getenv('APP_ID')
    redirect_id = os.getenv('REDIRECT_URI')
    return render_template('index.html', app_id=app_id, redirect_id=redirect_id)

app.run(port=5000, host='0.0.0.0', debug=True)
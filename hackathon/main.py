from flask import Flask, render_template, request
import os
from func import main

app = Flask(__name__)
os.system('icacls image_state /grant Administrateur:(D,WDAC)')
@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')


@app.route('/score', methods = ['POST'])
def source():
    file = request.files.get('file')
    file.save('image_state.png')
    data = main('image_state.png')
    return render_template('score.html', data = data)


if __name__ == "__main__":
    app.run()

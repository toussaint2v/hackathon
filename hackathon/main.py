from flask import Flask, render_template, request, send_file
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
    print(data[1][1])
    return render_template('score.html', data = data, size = len(data))

@app.route('/score/images/')
def getImages():
    print(request.args)
    id = request.args.get('id')

    return send_file(f'C:\\Users\\alexa\\PycharmProjects\\hackathon\\images_traitee\\{id}.png')

if __name__ == "__main__":
    app.run()

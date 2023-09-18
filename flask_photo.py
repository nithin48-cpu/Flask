from flask import Flask, render_template, request
import os

app = Flask(__name__)

pic_folder = os.path.join('static')

app.config['UPLOAD_FOLDER'] = pic_folder


@app.route("/")
@app.route("/index")
def homepage():
    pic = os.path.join(app.config['UPLOAD_FOLDER'], 'collage.jpg')
    return render_template('index.html',picture=pic)


if __name__ == "__main__":
    app.run(debug=True)

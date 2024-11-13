from flask import request, Flask, jsonify, render_template, url_for
import firebase


app = Flask(__name__)


@app.route('/login')
def login():
    with open("login.html", "r", encoding="utf-8") as file:
        text = file.readlines()
        return "".join(text)


@app.route('/donation')
def donation():
    with open("donation.html", "r", encoding="utf-8") as file:
        text = file.readlines()
        return "".join(text)


@app.route('/index')
def index():
    with open("index.html", "r", encoding="utf-8") as file:
        text = file.readlines()
        return "".join(text)


@app.route('/hospital')
def hospital():
    with open("hospital.html", "r", encoding="utf-8") as file:
        text = file.readlines()
        return "".join(text)


@app.route('/blogs')
def blogs():
    collection_name = "blogs"      # Replace with your collection name
    data = firebase.fetch_data(collection_name)
    return render_template('blog.html', data=data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

from flask import Flask, render_template
import requests

response = requests.get("https://api.npoint.io/29553edabcf2b6d4a0b7")
data = response.json()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=data)


@app.route('/blog/<num>')
def blog(num):
    return render_template("post.html", post=data[int(num)-1])


if __name__ == "__main__":
    app.run(debug=True)

from urllib import request
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")  

@app.route("/flowers", methods=["GET"])
def flower():
    flowers = [
    {'id': 1, 'name': 'rose', 'colour': 'white', 'water': True},
    {'id': 2, 'name': 'orchid', 'colour': 'purple', 'water': False},
    {'id': 3, 'name': 'tulip', 'colour': 'red', 'water': True},
    {'id': 4, 'name': 'cactus', 'colour': 'green', 'water': False},
    {'id': 5, 'name': 'bluebell', 'colour': 'blue', 'water': True},
    {'id': 6, 'name': 'sunflower', 'colour': 'yellow', 'water': True},
    {'id': 7, 'name': 'marigold', 'colour': 'gold', 'water': True}
    ]   
    return render_template("flowers.html", page_title="Flower List", flowers=flowers)

@app.route("/flowers/new", methods=["GET", "POST"])
def new_flower():
    if request.method == 'GET':
        return 'This works for post request'
    else:
        data = request.get_json()
        if data["color"] != "invisible":
            return "Yes, that seems a legitimate flower", 201
        else:
             return "Absolutly not", 400

if __name__ == '__main__':
    app.run(debug = True)
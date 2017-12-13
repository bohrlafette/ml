from flask import Flask, request, jsonify
import main as engine

app = Flask(__name__)


@app.route("/predict", methods = ["POST"])
def predict():
    json = request.json

    predictionUser = engine.user(
        json.get("name"),
        json.get("gender"),
        json.get("numChildren", 0),
        json.get("ownsHouse", 0),
        json.get("yearBorn"),
        json.get("numCats", 0),
        json.get("numDogs", 0),
        json.get("numHorses", 0)
    ) 
    return jsonify(engine.predict(predictionUser))

app.run()
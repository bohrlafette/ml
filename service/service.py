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

@app.route("/predict", methods = ["GET"])
def predictGet():
    return "try POST :)"

@app.route("/interaction", methods = ["POST"])
def interaction():
    json = request.json

    engine.interact(constructUser(json), constructInteraction(json))


def constructUser(json):
    return engine.user(
        json.get("name"),
        json.get("gender"),
        json.get("numChildren", 0),
        json.get("ownsHouse", 0),
        json.get("yearBorn"),
        json.get("numCats", 0),
        json.get("numDogs", 0),
        json.get("numHorses", 0)
    )

def constructInteraction(json):
    return [
        json.get("haft", 0),
        json.get("foerder", 0),
        json.get("zahn", 0),
        json.get("pferd", 0),
        json.get("hund", 0),
        json.get("hausrat", 0),
        json.get("kfz", 0)
    ]

app.run()
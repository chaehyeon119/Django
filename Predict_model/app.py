from typing import Dict
from flask import Flask, jsonify, request
from flask.templating import render_template
import ml

app = Flask(__name__)

# 템플릿 자동 리로딩
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    expected: Dict[str, int] = {}
    for name, f in request.files.items():
        expected[name] = ml.predict(f)
    return jsonify({"expected": expected})

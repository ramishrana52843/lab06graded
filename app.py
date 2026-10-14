import os
import random
from flask import Flask, request, jsonify

REG_NO = os.environ.get("REG_NO", "FA23-BAI-XXX")
_seed = os.environ.get("SEED", "0")
SEED = int(_seed) if _seed.isdigit() else _seed

random.seed(SEED)
a1 = random.uniform(-5, 5)
a2 = random.uniform(-5, 5)
a3 = random.uniform(-5, 5)
b = random.uniform(-10, 10)

app = Flask(__name__)


@app.route("/predict", methods=["GET", "POST"])
def predict():
    data = request.values
    try:
        x1 = float(data["x1"])
        x2 = float(data["x2"])
        x3 = float(data["x3"])
    except KeyError as e:
        return jsonify(error=f"missing parameter {e.args[0]}"), 400
    except ValueError:
        return jsonify(error="x1, x2, x3 must be some numbers"), 400

    y = a1 * x1 + a2 * x2 + a3 * x3 + b
    return app.response_class(
        response=__import__("json").dumps(
            {"registration number": REG_NO, "prediction": round(y, 2)}
        ),
        mimetype="application/json",
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

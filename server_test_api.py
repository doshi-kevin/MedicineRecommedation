from flask import Flask, request, jsonify
from nlp_symptom_parser import extract_symptoms
from model_selector import ModelSelector

app = Flask(__name__)
selector = ModelSelector()

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data.get("symptoms", "")
    symptoms = extract_symptoms(text)

    # fake predictions for demonstration
    fake_predictions = {
        "naive_bayes": "Fever",
        "svc": "Migraine",
        "random_forest": "Fever"
    }

    final_disease = selector.choose_best(fake_predictions)

    return jsonify({
        "input_text": text,
        "extracted_symptoms": symptoms,
        "chosen_disease": final_disease
    })

if __name__ == "__main__":
    app.run(debug=True)

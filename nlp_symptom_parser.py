import re

SYMPTOMS = [
    "fever", "headache", "cough", "fatigue", "nausea",
    "vomiting", "chills", "back pain", "dizziness"
]

def extract_symptoms(text: str):
    text = text.lower()
    found = []
    for symptom in SYMPTOMS:
        if symptom in text:
            found.append(symptom)

    # fallback small heuristic
    if not found and "pain" in text:
        found.append("body pain")

    return list(set(found))

if __name__ == "__main__":
    sample = "I have been coughing with heavy headache and nausea."
    print(extract_symptoms(sample))

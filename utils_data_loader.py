import pandas as pd
import os

def load_symptom_data(path="data/symptom_dataset.csv"):
    """Load symptom → disease dataset."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"Dataset not found: {path}")
    df = pd.read_csv(path)
    print(f"[INFO] Loaded dataset with {df.shape[0]} rows & {df.shape[1]} columns")
    return df

def merge_datasets(symptoms, precautions, meds):
    """Merge three datasets into a single knowledge table."""
    df = symptoms.merge(precautions, on='Disease', how='left')
    df = df.merge(meds, on='Disease', how='left')
    return df

if __name__ == "__main__":
    try:
        s = load_symptom_data()
    except Exception as e:
        print("[ERROR]", e)

import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import os

def run_model_evaluation():
    print("--- Phase 4.3: Executing Model Evaluation & Metrics Audit ---")

    # 1. Load the Model and the Testing Data
    try:
        model = joblib.load('models/lead_scoring_model.pkl')
        X_test = pd.read_pickle('data/model_data/X_test.pkl')
        y_test = pd.read_pickle('data/model_data/y_test.pkl')
    except FileNotFoundError:
        print("Error: Required files missing. Please run 4.1 and 4.2 first.")
        return

    # 2. Generate Predictions
    print("Generating predictions on the unseen Test Set...")
    y_pred = model.predict(X_test)

    # 3. Calculate Core Metrics
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    print("\n--- PERFORMANCE METRICS ---")
    print(f"Accuracy (Overall Correctness): {acc:.2%}")
    print(f"Precision (Minimize Wasted Effort): {prec:.2%}")
    print(f"Recall (Minimize Missed Opportunities): {rec:.2%}")
    print(f"F1-Score (Model Balance): {f1:.4f}")

    # 4. Detailed Classification Report
    print("\nDetailed Classification Report:")
    print(classification_report(y_test, y_pred))

    # 5. Plot Confusion Matrix
    print("Generating Confusion Matrix Visual...")
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=['Non-Lead', 'High-Propensity'], 
                yticklabels=['Non-Lead', 'High-Propensity'])
    
    plt.title('Telco-Optima Confusion Matrix: Lead Scoring Accuracy', fontweight='bold')
    plt.ylabel('Actual Subscriber Status')
    plt.xlabel('AI Predicted Status')
    
    # Save the plot for the Master's documentation
    os.makedirs('reports', exist_ok=True)
    plt.savefig('reports/confusion_matrix.png')
    print("\nSUCCESS: Evaluation complete. Matrix saved in 'reports/confusion_matrix.png'")

    # 6. Business Translation
    print("\n--- BUSINESS TRANSLATION ---")
    efficiency = (1 - (cm[0,1] / len(y_test))) * 100
    print(f"Strategic Impact: The sales team can now avoid {cm[0,1]} false leads.")
    print(f"Operational Efficiency: {efficiency:.1f}% reduction in manual targeting errors.")

if __name__ == "__main__":
    run_model_evaluation()
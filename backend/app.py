from flask import Flask, jsonify, request
from flask_cors import CORS
import joblib
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

# Load the trained model
model_path = os.path.join(os.path.dirname(__file__), 'cost_prediction_model.pkl')
try:
    pipeline = joblib.load(model_path)
    model_loaded = True
except FileNotFoundError:
    model_loaded = False
    print("Warning: Model file not found at", model_path)


@app.route('/simple', methods=['POST'])
def simple():
    return jsonify({
        "message": "Hello from Flask!",
        "status": "Success"
    })


@app.route('/predict', methods=['POST'])
def predict():
    """
    Endpoint to predict project cost
    Expected JSON input:
    {
        "project_type": "AI/ML Solution",
        "client_industry": "E-commerce",
        "estimated_timeline_months": 5,
        "team_allocation": 6,
        "complexity_score": 3,
        "revision_count": 3
    }
    """
    try:
        if not model_loaded:
            return jsonify({
                "success": False,
                "error": "Model not loaded. Please train the model first."
            }), 500

        data = request.get_json()

        # Validate required fields
        required_fields = [
            'project_type',
            'client_industry',
            'estimated_timeline_months',
            'team_allocation',
            'complexity_score',
            'revision_count'
        ]

        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({
                "success": False,
                "error": f"Missing fields: {', '.join(missing_fields)}"
            }), 400

        # Create DataFrame with the input
        input_df = pd.DataFrame({
            'project_type': [data['project_type']],
            'client_industry': [data['client_industry']],
            'estimated_timeline_months': [int(data['estimated_timeline_months'])],
            'team_allocation': [int(data['team_allocation'])],
            'complexity_score': [int(data['complexity_score'])],
            'revision_count': [int(data['revision_count'])]
        })

        # Make prediction
        predicted_cost = pipeline.predict(input_df)[0]

        return jsonify({
            "success": True,
            "predicted_cost": round(predicted_cost, 2),
            "message": f"Predicted cost for the project: ₹{round(predicted_cost, 2)}"
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


if __name__ == '__main__':
    app.run(debug=True)
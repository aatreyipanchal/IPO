from flask import Flask, jsonify
import pandas as pd
import os

app = Flask(__name__)

# Define a relative CSV file path (place your CSV in the same directory as app.py)
CSV_FILE_PATH = os.path.join(os.path.dirname(__file__), "IPO_DETAILS.csv")

@app.route('/data', methods=['GET'])
def get_data():
    try:
        # Check if the file exists
        if not os.path.exists(CSV_FILE_PATH):
            return jsonify({"error": "CSV file not found"}), 404

        # Read CSV into DataFrame
        df = pd.read_csv(CSV_FILE_PATH)

        # Convert DataFrame to JSON (handling NaN values as None)
        json_data = df.to_dict(orient='records')

        return jsonify(json_data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

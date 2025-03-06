from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Define the CSV file path
CSV_FILE_PATH = r"C:\Users\DELL\Downloads\IPO_DETAILS - IPO.csv"

@app.route('/data', methods=['GET'])
def get_data():
    try:
        # Read CSV into DataFrame
        df = pd.read_csv(CSV_FILE_PATH)

        # Convert DataFrame to JSON (handling NaN values as None)
        json_data = df.to_dict(orient='records')

        return jsonify(json_data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
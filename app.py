import pandas as pd
import requests
from flask import Flask, jsonify

app = Flask(__name__)

#https://drive.google.com/file/d/1pHQPfWgkwyeq-7pG1fkIz2qTmpbTGDDI/view?usp=sharing
# Google Drive File ID
FILE_ID = "1pHQPfWgkwyeq-7pG1fkIz2qTmpbTGDDI"

# Function to download CSV from Google Drive
def download_csv_from_drive(file_id):
    url = f"https://drive.google.com/uc?id={file_id}"
    response = requests.get(url)

    if response.status_code == 200:
        with open("IPO_DETAILS - IPO.csv", "wb") as f:
            f.write(response.content)
        return "IPO_DETAILS - IPO.csv"
    else:
        return None

@app.route('/data', methods=['GET'])
def get_data():
    try:
        csv_path = download_csv_from_drive(FILE_ID)
        
        if not csv_path:
            return jsonify({"error": "Failed to download CSV from Google Drive"}), 500

        df = pd.read_csv(csv_path)
        json_data = df.to_dict(orient='records')

        return jsonify(json_data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

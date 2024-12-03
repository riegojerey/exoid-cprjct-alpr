from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# File to store the plates
PLATES_FILE = "/data/watched_plates.json"

# Ensure file exists
if not os.path.exists(PLATES_FILE):
    with open(PLATES_FILE, "w") as f:
        json.dump([], f)

@app.route('/plates', methods=['GET', 'POST', 'DELETE'])
def manage_plates():
    if request.method == 'GET':
        with open(PLATES_FILE, 'r') as f:
            plates = json.load(f)
        return jsonify(plates)
    
    if request.method == 'POST':
        new_plate = request.json.get('plate')
        with open(PLATES_FILE, 'r+') as f:
            plates = json.load(f)
            if new_plate not in plates:
                plates.append(new_plate)
                f.seek(0)
                json.dump(plates, f)
        return jsonify({"message": "Plate added"}), 201
    
    if request.method == 'DELETE':
        plate_to_remove = request.json.get('plate')
        with open(PLATES_FILE, 'r+') as f:
            plates = json.load(f)
            plates = [p for p in plates if p != plate_to_remove]
            f.seek(0)
            f.truncate()
            json.dump(plates, f)
        return jsonify({"message": "Plate removed"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

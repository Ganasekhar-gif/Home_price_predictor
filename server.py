from flask import Flask, request, jsonify

import util

app = Flask(__name__)



@app.route('/hello')
def hello():
    return 'hi'


@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    return response


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        # Check if data is provided
        if not request.is_json:
            return jsonify({'error': 'Request must be JSON'}), 400

        data = request.get_json()

        # Check if all required fields are present
        required_fields = ['total_sqft', 'location', 'bhk', 'bath']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({'error': f'Missing required fields: {", ".join(missing_fields)}'}), 400

        # Extract the data and perform validation
        total_sqft = float(data['total_sqft'])
        location = data['location']
        bhk = int(data['bhk'])
        bath = int(data['bath'])

        # Get the estimated price
        estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)

        return jsonify({'estimated_price': estimated_price})

    except Exception as e:
        # Return detailed error message
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()  # Load saved artifacts (e.g., models, scalers)
    app.run(debug=True)

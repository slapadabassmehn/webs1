from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Make a request to the Sleeper API
    response = requests.get('https://api.sleeper.app/v1/league/1048388540935016448/users')
    # Convert the response to JSON
    data = response.json()
    # Pass the data to the template for rendering
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)

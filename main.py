import connexion
from flask_cors import CORS


app = connexion.App(__name__, port=5000, specification_dir="swagger")
CORS(app.app, methods=['POST', 'GET'], allow_headers=['Content-Type'])

app.add_api('api.yaml')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

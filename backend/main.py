from api.quotes.views import quotes
from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    app.register_blueprint(quotes)

    CORS(app, resources={r"/*": {"origins": "*"}})

    return app


app = create_app()


if __name__ == '__main__':
    app.run(debug=True)

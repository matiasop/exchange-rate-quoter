from api.quotes.views import quotes
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.register_blueprint(quotes)

    return app


app = create_app()


if __name__ == '__main__':
    app.run(debug=True)
    app.run(debug=True)
    app.run(debug=True)
    app.run(debug=True)
    app.run(debug=True)

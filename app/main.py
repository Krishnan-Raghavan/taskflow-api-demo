from flask import Flask

from app.routes import bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(bp)
    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5000)

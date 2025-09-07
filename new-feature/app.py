from flask import Flask, request, jsonify


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/hello")
    def hello():
        name = request.args.get("name", default="World", type=str)
        return f"Hello, {name}!"

    return app


app = create_app()


if __name__ == "__main__":
    # デフォルト: http://127.0.0.1:5000
    app.run(host="0.0.0.0", port=5000, debug=True)


__author__ = "imdreamrunner"
__email__ = "imdreamrunner@gmail.com"


if __name__ == "__main__":
    from app import app
    app.run(host="0.0.0.0", port=5000, debug=True)
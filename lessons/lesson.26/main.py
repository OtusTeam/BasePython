__all__ = ("app",)

from app import app

if __name__ == "__main__":
    app.run(
        # host="localhost",
        # port=5000,
        debug=True,
    )

from app import app

app.config.update(
    DEBUG=True,
)


if __name__ == "__main__":
    app.run(debug=True)

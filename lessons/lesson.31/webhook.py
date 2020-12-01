from flask import Flask

app = Flask(__name__)


@app.route("/deploy-42", methods=["POST"])
def run_deploy():
    print("run deploy")
    # git pull
    # service nginx restart
    return "ok"


if __name__ == "__main__":
    app.run(debug=True, port=3000)

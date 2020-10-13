from flask import Flask, request, render_template

from views import product_app

app = Flask(__name__)
app.register_blueprint(product_app, url_prefix="/products")


@app.route("/", methods=["GET", "POST"])
def index():
    name = "World"
    if request.method == "POST":
        name = request.form.get('name', 'World')
    return render_template("index.html", name=name)


# app.add_url_rule("/", "index", index)
# app.add_url_rule("/", view_func=index)

@app.route("/hello/")
@app.route("/hello/<string:name>/")
def hello(name=None):
    if name is None:
        name = "World"
    return f"<h1>Hello {name}!</h1>"


# @app.route('/post/<string:post_id>/')
# def alternative_show_post(post_id):
#     post_id > 0
#     return 'Post (str) %r' % post_id


@app.route('/post/<int:post_id>/')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post int %d' % post_id

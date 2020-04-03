from flask import Flask, render_template

app = Flask(__name__)
print(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


# To run the flask server in debug mode
if __name__ == '__main__':
    app.run(debug=True)

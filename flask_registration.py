from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
@app.route("/registration")
def homepage():
    return render_template('registration.html')


@app.route("/conformation", methods=['POST', 'GET'])
def conform():
    if request.method == "POST":
        n = request.form.get("name")
        c = request.form.get("city")
        p = request.form.get("phone number")
        return render_template("conformation.html", name=n, city=c, number=p)


if __name__ == "__main__":
    app.run(debug=True)

from flask import * #pylint: disable=unused-wildcard-import

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("/index.html")

app.run()
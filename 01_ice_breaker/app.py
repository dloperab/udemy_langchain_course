from flask import Flask, render_template, request, jsonify
from ice_breaker import ice_break

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    name = request.form["name"]
    profile_info, profile_pic_url = ice_break(name=name)

    return jsonify(
        {
            "summary": profile_info.summary,
            "interests": profile_info.topics_of_interest,
            "facts": profile_info.facts,
            "ice_breakers": profile_info.ice_breakers,
            "picture_url": profile_pic_url,
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

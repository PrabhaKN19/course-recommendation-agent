from flask import Flask, render_template, request
from agent import get_course_recommendation

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend():

    # Get user input from the form
    name = request.form["name"]
    skills = request.form["skills"]
    goal = request.form["goal"]

    # Call AI Agent
    ai_response = get_course_recommendation(
        name,
        skills,
        goal
    )

    # Display result
    return render_template(
        "result.html",
        name=name,
        goal=goal,
        result=ai_response
    )


if __name__ == "__main__":
    app.run(debug=True)
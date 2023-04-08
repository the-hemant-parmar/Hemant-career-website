from flask import Flask, render_template, jsonify

app = Flask(__name__)

Skills = [{
  'id': 1,
  'title': 'Python',
  'source': 'School, Youtube, projects',
  'proficiency': 'Intermediate',
}, {
  'id': 2,
  'title': 'Web dev',
  'source': 'Youtube, projects',
  'proficiency': 'Intermediate',
}, {
  'id': 3,
  'title': 'mySQL',
  'source': 'School, Youtube, projects',
  'proficiency': 'Begginer',
}]


@app.route("/")
def hello_world():
  return render_template("home.html", skills=Skills)


@app.route("/api/skills")
def list_skills():
  return jsonify(Skills)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

from flask import Flask, render_template, request
import psycopg2
import psycopg2.extras

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

conn = psycopg2.connect(dbname="resume", user="conzty01")
#conn = psycopg2.connect(os.environ["DATABASE_URL"])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/projects")
def projects():
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute("SELECT * FROM projects;")

    return render_template("projects.html", projectList=cur.fetchall())

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)

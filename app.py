from flask import Flask, render_template, request
from cleaner import find_old_files, delete_files

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])

def index():
    folder = ""
    days = ""

    if request.method == "POST":
        folder = request.form.get("folder", "")
        days = int(request.form.get("days", ""))

    old_files = find_old_files(folder, days)
    '''delete_files(old_files)'''

    return render_template("index.html", folder=folder, days=days)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request
from cleaner import find_old_files, delete_files
from pathlib import Path

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])

def index():
    folder = ""
    days = ""
    files = []

    if request.method == "POST":
        folder = request.form.get("folder", "")
        days_str = request.form.get("days", "")

        try:
            days_int = int(days_str)
            if folder:
                files = find_old_files(Path(folder), days_int)
            days = days_str
        except ValueError:
            error = "Days must be a number."
        except Exception as e:
            error = str(e)

    return render_template("index.html", folder=folder, days=days, files=files, error=error)

if __name__ == "__main__":
    app.run(debug=True)
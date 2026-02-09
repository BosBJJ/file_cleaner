from flask import Flask, render_template, request
from cleaner import find_old_files, delete_files
from pathlib import Path

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])

def index():
    folder = ""
    days = ""
    files = []
    error = ""
    message = ""

    if request.method == "POST":
        folder = request.form.get("folder", "")
        days_str = request.form.get("days", "")
        action = request.form.get("action", "scan")

        try:
            days_int = int(days_str)
            days = days_str
            
            if not folder:
                raise Exception("Input is not a valid folder")
            
            files = find_old_files(Path(folder), days_int)

            if action == "delete":
                delete_files(files)
                message = f"Deleted {len(files)} files."
                files = []



        except ValueError:
            error = "Days must be a number."
        except Exception as e:
            error = str(e)

    return render_template("index.html", folder=folder, days=days, files=files, error=error, message=message)

if __name__ == "__main__":
    app.run(debug=True)
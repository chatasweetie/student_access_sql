from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)

@app.route("/student_access")
def get_student_form():
    """Show form for searching for a student or creating a new student."""

    return render_template("student_access.html")


@app.route("/student", methods=['GET'])
def get_student():
    """Show information about a student."""
    github =request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    project_data = hackbright.get_title_grade_by_github(github)
    html = render_template("student_info.html",
                            first=first,
                            last=last,
                            github=github,
                            projectdata=project_data)
    return html

@app.route("/student", methods=['POST'])
def make_student():
    """Show information about a student."""
    first = request.form.get('first')
    last = request.form.get('last')
    github = request.form.get('github')
    hackbright.make_new_student(first, last, github)
    html = render_template("student_info.html",
                            first=first,
                            last=last,
                            github=github)
    return html




if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)

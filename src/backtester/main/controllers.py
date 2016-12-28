from flask import Blueprint, current_app, render_template

main = Blueprint('main', __name__, template_folder='templates')

@main.route('//')
def display_index():
    return render_template("index.html")
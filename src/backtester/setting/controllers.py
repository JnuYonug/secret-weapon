from flask import Blueprint, render_template, flash
from flask import current_app, redirect, request, url_for
from flask_security.decorators import login_required

from backtester.setting.forms.new_algorithm_forms import CreateAlgorithmForm

setting = Blueprint('setting', __name__, template_folder='templates')

@setting.route('/')
@login_required
def display_index():
    return render_template("setting_index.html")

@setting.route('/edit/<algorithm_name>')
@login_required
def display_edit(algorithm_name):
    return render_template("setting_edit_algorithm.html", algorithm=algorithm_name)

@setting.route('/new_algorithm/', methods=['GET', 'POST'])
def display_new_algorithm():
    form = CreateAlgorithmForm(request.form)
    if request.method == 'POST' and form.validate():

        pass

    return render_template('setting_new_algorithm.html', form=form)

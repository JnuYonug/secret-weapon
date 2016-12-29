from flask import Blueprint, render_template, flash
from flask import current_app, redirect, request, url_for
from flask_security.decorators import login_required
from flask_security import current_user

from sqlalchemy import exc

from backtester.setting.forms.new_algorithm_forms import CreateAlgorithmForm

from backtester.data.models import db, Algorithm

setting = Blueprint('setting', __name__, template_folder='templates')

@setting.route('/')
@login_required
def display_index():
    algorithms = [algorithm for algorithm in Algorithm.query.all()]
    current_app.logger.info('Displaying all algorithms.')

    return render_template("setting_index.html", algorithms=algorithms)

@setting.route('/edit/<algorithm_id>')
@login_required
def display_edit(algorithm_id):
    algorithm = Algorithm.query.filter_by(id=algorithm_id).first()
    return render_template("setting_edit_algorithm.html", algorithm=algorithm)

@setting.route('/new_algorithm/', methods=['GET', 'POST'])
def display_new_algorithm():
    form = CreateAlgorithmForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        current_app.logger.info('Adding a new algorithm %s.', (name))
        algorithm = Algorithm(name, current_user.id)
        try:
            db.session.add(algorithm)
            db.session.commit()
            flash('Algorithm successfully created.')
        except exc.SQLAlchemyError as e:
            flash('Algorithm was not created.')
            current_app.logger.error(e)

    return render_template('setting_new_algorithm.html', form=form)

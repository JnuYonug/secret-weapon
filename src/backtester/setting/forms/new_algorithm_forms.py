from wtforms import Form, TextField, validators

class CreateAlgorithmForm(Form):
    name = TextField('Algorithm Name', [validators.Length(min=5, max=70)])

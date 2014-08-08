from flask_wtf import Form
from wtforms import FloatField
from wtforms.validators import DataRequired

class RpsSimForm(Form):
    #Required is going away in WTForms 3.0, so the IDE suggested to change it
    sameField = FloatField('sameField', validators = [DataRequired()], default = 0)
    strongerField = FloatField('strongerField', validators = [DataRequired()], default = 0)
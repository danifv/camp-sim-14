from flask_wtf import Form
from wtforms import FloatField
from wtforms import IntegerField
from wtforms.validators import DataRequired

class TestSimForm(Form):
    #Required is going away in WTForms 3.0, so the IDE suggested to change it
    aField = FloatField('aField', validators = [DataRequired()])
    mField = FloatField('mField', validators = [DataRequired()])
    xMinField = FloatField('xMinField', validators = [DataRequired()])
    xMaxField = FloatField('xMaxField', validators = [DataRequired()])
    iterations = IntegerField('iterations', validators = [DataRequired()])
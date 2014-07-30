from flask_wtf import Form
from wtforms import FloatField
from wtforms.validators import Required

class TestSimForm(Form):
    aField = FloatField('aField', validators = [Required()])
    mField = FloatField('mField', validators = [Required()])
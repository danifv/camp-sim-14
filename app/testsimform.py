from flask_wtf import Form
from wtforms import IntegerField
from wtforms.validators import Required

class TestSimForm(Form):
    aField = IntegerField('aField', validators = [Required()])
    mField = IntegerField('mField', validators = [Required()])
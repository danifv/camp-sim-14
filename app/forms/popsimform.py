from flask_wtf import Form
from wtforms import IntegerField
from wtforms.validators import DataRequired

class PopSimForm(Form):
    #Required is going away in WTForms 3.0, so the IDE suggested to change it
    huntStartField = IntegerField('huntStartField', validators = [DataRequired()], default = 0)
    numberOfHuntersField = IntegerField('numberOfHuntersField', validators = [DataRequired()], default = 0)
    huntRabbitsField = IntegerField('huntRabbitsField', validators = [DataRequired()], default = 0)
    huntFoxesField = IntegerField('huntFoxesField', validators = [DataRequired()], default = 0)
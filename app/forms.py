from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class TagForm(Form):
    tag = StringField('tag', validators=[DataRequired()])

class NewPhoto(Form):
    tag = StringField('tag', validators=[DataRequired()])

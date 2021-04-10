from flask_wtf import FlaskForm
from wtforms import TextArea
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired

class UploadForm(FlaskForm):
	desc = TextArea('Description',[DataRequired()])
	photo = FileField('Picture',validators = [FileRequired(),FileAllowed(['jpg','png'],'imagesonly')])
	
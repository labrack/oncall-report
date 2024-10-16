from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, BooleanField, FileField, SubmitField
from wtforms.validators import DataRequired, URL

class TicketForm(FlaskForm):
    url = StringField('Ticket URL', validators=[DataRequired(), URL()])
    status = SelectField('Status', choices=[('ongoing', 'Ongoing'), ('closed', 'Closed'), ('rejected', 'Rejected')], validators=[DataRequired()])
    submit = SubmitField('Add Ticket')

class AlertForm(FlaskForm):
    alert_file = StringField('Alert Spreadsheet File', validators=[DataRequired()])
    submit = SubmitField('Add Alert')

class IncidentForm(FlaskForm):
    description = TextAreaField('Incident Description', validators=[DataRequired()])
    relevant = BooleanField('Relevant to Team')
    submit = SubmitField('Add Incident')

class NoteForm(FlaskForm):
    content = TextAreaField('Note Content', validators=[DataRequired()])
    submit = SubmitField('Add Note')

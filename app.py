from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import TicketForm, AlertForm, IncidentForm, NoteForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/dbname'  # Update for MySQL
db = SQLAlchemy(app)

# Models for storing the data
class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

class Alert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    alert_file = db.Column(db.String(200), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

class Incident(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(500), nullable=False)
    relevant = db.Column(db.Boolean, nullable=False, default=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_ticket', methods=['GET', 'POST'])
def add_ticket():
    form = TicketForm()
    if form.validate_on_submit():
        ticket = Ticket(url=form.url.data, status=form.status.data)
        db.session.add(ticket)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_ticket.html', form=form)

@app.route('/add_alert', methods=['GET', 'POST'])
def add_alert():
    form = AlertForm()
    if form.validate_on_submit():
        alert = Alert(alert_file=form.alert_file.data)
        db.session.add(alert)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_alert.html', form=form)

@app.route('/add_incident', methods=['GET', 'POST'])
def add_incident():
    form = IncidentForm()
    if form.validate_on_submit():
        incident = Incident(description=form.description.data, relevant=form.relevant.data)
        db.session.add(incident)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_incident.html', form=form)

@app.route('/add_note', methods=['GET', 'POST'])
def add_note():
    form = NoteForm()
    if form.validate_on_submit():
        note = Note(content=form.content.data)
        db.session.add(note)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_note.html', form=form)

@app.route('/report')
def report():
    tickets = Ticket.query.all()
    alerts = Alert.query.all()
    incidents = Incident.query.filter_by(relevant=True).all()
    notes = Note.query.all()
    return render_template('report.html', tickets=tickets, alerts=alerts, incidents=incidents, notes=notes)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

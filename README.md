
# On-Call Report Flask App

This Flask application is designed to help network SREs create a report for their on-call rotation. The report tracks tickets, alerts, incidents, and notes throughout the week, and generates a summary report at the end of the shift.

## Features
- **Add Tickets**: Add URLs of tickets opened during your on-call shift along with their status.
- **Track Alerts**: Upload alert files (spreadsheet links).
- **Record Incidents**: Log incidents and mark them as relevant to the team.
- **Add Notes**: Capture any other relevant information or notes for the report.
- **Generate Report**: View a weekly report summarizing the tickets, alerts, incidents, and notes.

## Prerequisites
- Python 3.7 or higher
- MySQL or MariaDB installed and running

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/labrack/oncall-report.git
cd oncall-report
```

### 2. Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up MySQL Database

1. Log in to your MySQL instance:
    ```bash
    mysql -u your_username -p
    ```

2. Create a new database:
    ```sql
    CREATE DATABASE oncall_report;
    ```

3. (Optional) Create a new user and grant privileges:
    ```sql
    CREATE USER 'flaskuser'@'localhost' IDENTIFIED BY 'your_password';
    GRANT ALL PRIVILEGES ON oncall_report.* TO 'flaskuser'@'localhost';
    FLUSH PRIVILEGES;
    ```

4. Update the Flask app configuration in `app.py`:
    ```python
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flaskuser:your_password@localhost/oncall_report'
    ```

### 5. Initialize the Database
After setting up MySQL and configuring the connection string, initialize the database tables by running the following commands:

```bash
python
>>> from app import app, db
>>>
>>> with app.app_context():
...     db.create_all()
...
>>> exit()
```

### 6. Run the Application
Start the Flask development server:
```bash
python app.py
```

Visit the app at [http://localhost:5000](http://localhost:5000).

## Usage

- **Add Ticket**: Navigate to `/add_ticket` to add a new ticket with its status.
- **Add Alert**: Navigate to `/add_alert` to upload an alert file (or its path).
- **Add Incident**: Navigate to `/add_incident` to log incidents.
- **Add Note**: Navigate to `/add_note` to log any other notes.
- **Generate Report**: Visit `/report` to view the weekly summary report.

## License
This project is licensed under the Unlicense. See the [LICENSE](LICENSE) file for more details.

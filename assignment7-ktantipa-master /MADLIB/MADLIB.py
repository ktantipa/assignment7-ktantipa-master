import os
from flask import Flask, render_template, g, request, redirect
from sqlite3 import dbapi2 as sqlite3

##### APP SETUP #####
app = Flask(__name__)
app.config.from_object(__name__)

##### DB SETUP #####

# Setup the database credentials
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'RUMPELSTILTSKIN.db'),
    DEBUG=True,
    SECRET_KEY='ABCDEF',
    USERNAME='admin',
    PASSWORD='password'
))

# Connect to the DB
def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

# Wrap the helper function so we only open the DB once
def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

# Create the database (we do this via command line!!!)
def init_db():
    """Initializes the database."""
    db = get_db()
    with app.open_resource(os.path.join(app.root_path, 'schema.sql'), mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

# Command to create the database via command line
# You call it from command line: flask initdb
@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    init_db()
    print('Initialized the database.')

# Close the database when the request ends
@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

##### ROUTES #####

@app.route('/initdb')
@app.route('/horseman')
def InitDB() :
    init_db()
    db = get_db()
    db.execute('INSERT INTO users (id, business_name, business_type, market_type, job_to_be_done, revenue_model) VALUES (0, "", "", "", "", "")')
    db.commit()
    return redirect('/get_horseman');

@app.route('/get_horseman')
def GET_Example() :
    db = get_db()
    cur = db.execute('SELECT business_name, business_type, market_type, job_to_be_done, revenue_model FROM users ORDER BY id DESC')
    the_users = cur.fetchall()
    return render_template('madlib.html', entries=the_users)

if __name__ == "__main__":
   app.run()

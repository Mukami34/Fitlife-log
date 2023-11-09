# fitlife_log.py
import os
import click
from lib.database import init_db, run_migrations, Session
from lib.models import User, Workout, Exercise

DB_URL = os.environ.get('DB_URL', 'sqlite:///fitlife_log.db')

@click.group()
def fitlife_log():
    """FitLife Log CLI"""
    pass

@fitlife_log.command()
def initdb():
    """Initialize the database"""
    init_db()
    click.echo("Database initialized.")

@fitlife_log.command()
def migrate():
    """Run Alembic migrations"""
    run_migrations()
    click.echo("Database migrated.")

@fitlife_log.command()
@click.option('--username', prompt=True, help='User username')
@click.option('--email', prompt=True, help='User email')
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True, help='User password')
def createuser(username, email, password):
    """Create a new user"""
    session = Session()
    user = User(username=username, email=email, password=password)
    session.add(user)
    session.commit()
    click.echo(f"User {username} created.")

@fitlife_log.command()
@click.option('--date', prompt=True, help='Workout date')
@click.option('--user_id', prompt=True, help='User ID')
def createworkout(date, user_id):
    """Create a new workout"""
    session = Session()
    workout = Workout(date=date, user_id=user_id)
    session.add(workout)
    session.commit()
    click.echo(f"Workout created on {date}.")

@fitlife_log.command()
@click.option('--name', prompt=True, help='Exercise name')
@click.option('--description', prompt=True, help='Exercise description')
@click.option('--sets', prompt=True, help='Number of sets')
@click.option('--reps', prompt=True, help='Number of reps')
@click.option('--weight', prompt=True, help='Exercise weight')
@click.option('--workout_id', prompt=True, help='Workout ID')
def createexercise(name, description, sets, reps, weight, workout_id):
    """Create a new exercise"""
    session = Session()
    exercise = Exercise(name=name, description=description, sets=sets, reps=reps, weight=weight, workout_id=workout_id)
    session.add(exercise)
    session.commit()
    click.echo(f"Exercise {name} created.")
    
@fitlife_log.command()
@click.option('--username', prompt=True, help='User username')
@click.option('--email', prompt=True, help='User email')
def updateuser(username, email):
    """Update an existing user's email"""
    session = Session()
    user = session.query(User).filter_by(username=username).first()
    
    if user:
        user.email = email
        session.commit()
        click.echo(f"User {username}'s email updated to {email}.")
    else:
        click.echo(f"User {username} not found.")

    
if __name__ == '__main__':
    fitlife_log()
    




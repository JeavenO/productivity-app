"""
CLI commands for Flask app.
"""

import click
from flask.cli import with_appcontext
from services.db import db
from models.user import User
from models.note import Note

@click.command("seed")
@with_appcontext
def seed():
    """Drop, recreate, and seed the database with fixed users and notes."""
    db.drop_all()
    db.create_all()

    # Users
    alice = User(username="alice")
    alice.set_password("password123")
    bob = User(username="bob")
    bob.set_password("password123")

    db.session.add_all([alice, bob])
    db.session.commit()

    # Notes
    note1 = Note(title="Shopping List", content="Milk, Bread, Eggs", user_id=alice.id)
    note2 = Note(title="Todo", content="Finish homework, Call mom", user_id=alice.id)
    note3 = Note(title="Workout Plan", content="Run 5km, Pushups", user_id=bob.id)
    note4 = Note(title="Books to Read", content="1984, Brave New World", user_id=bob.id)

    db.session.add_all([note1, note2, note3, note4])
    db.session.commit()

    click.echo("Database seeded with users (alice, bob) and sample notes.")

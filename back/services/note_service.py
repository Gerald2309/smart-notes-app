from ..models.note import Note
from ..extensions import db

def get_all_notes():
    return Note.query.all()

def get_note_by_id(note_id):
    return Note.query.get(note_id)

def create_note(data):
    note = Note(
        title=data.get('title'),
        content=data.get('content')
    )
    db.session.add(note)
    db.session.commit()
    return note

def update_note(note_id, data):
    note = Note.query.get(note_id)
    if note:
        note.title = data.get('title', note.title)
        note.content = data.get('content', note.content)
        db.session.commit()
    return note

def delete_note(note_id):
    note = Note.query.get(note_id)
    if note:
        db.session.delete(note)
        db.session.commit()
    return note
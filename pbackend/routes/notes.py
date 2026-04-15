"""
Notes CRUD routes with pagination, protected by JWT.
"""

from flask import Blueprint, request, jsonify
from models.note import Note
from services.db import db
from flask_jwt_extended import jwt_required, get_jwt_identity

notes_bp = Blueprint("notes", __name__)

@notes_bp.route("/", methods=["GET"])
@jwt_required()
def get_notes():
    user_id = get_jwt_identity()
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 5, type=int)

    notes = Note.query.filter_by(user_id=user_id).paginate(page=page, per_page=per_page)
    return jsonify({
        "notes": [{"id": n.id, "title": n.title, "content": n.content} for n in notes.items],
        "total": notes.total,
        "pages": notes.pages,
        "current_page": notes.page
    })

@notes_bp.route("/", methods=["POST"])
@jwt_required()
def create_note():
    user_id = get_jwt_identity()
    data = request.get_json()
    note = Note(title=data["title"], content=data["content"], user_id=user_id)
    db.session.add(note)
    db.session.commit()
    return jsonify({"message": "Note created", "id": note.id}), 201

@notes_bp.route("/<int:note_id>", methods=["PATCH"])
@jwt_required()
def update_note(note_id):
    user_id = get_jwt_identity()
    note = Note.query.filter_by(id=note_id, user_id=user_id).first_or_404()
    data = request.get_json()
    note.title = data.get("title", note.title)
    note.content = data.get("content", note.content)
    db.session.commit()
    return jsonify({"message": "Note updated"}), 200

@notes_bp.route("/<int:note_id>", methods=["DELETE"])
@jwt_required()
def delete_note(note_id):
    user_id = get_jwt_identity()
    note = Note.query.filter_by(id=note_id, user_id=user_id).first_or_404()
    db.session.delete(note)
    db.session.commit()
    return jsonify({"message": "Note deleted"}), 200

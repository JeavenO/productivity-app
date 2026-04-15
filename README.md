# Productivity App - Full Stack Setup Guide

This README documents the full setup and testing process for the Productivity App project, which includes a Flask backend secured with JWT and a React frontend client.

## Project Structure

productivity-app/
├── pbackend/   # Flask backend
│   ├── app.py
│   ├── cli.py
│   ├── seed.py
│   └── ...
└── pfrontend/  # Frontend repo
    └── flask-c10-summative-lab-sessions-and-jwt/
        ├── client-with-jwt/
        └── client-with-sessions/

## Backend Setup (pbackend)

1. Install dependencies

pipenv install

2. Run migrations

pipenv run flask --app app:create_app db upgrade

3. Seed the database

pipenv run flask --app app:create_app seed

This creates users alice and bob with password password123 and sample notes.

4. Start the backend server

pipenv run flask --app app:create_app run

Backend runs at http://127.0.0.1:5000.

## Frontend Setup (pfrontend)

1. Navigate to JWT client

cd pfrontend/flask-c10-summative-lab-sessions-and-jwt/client-with-jwt

2. Install dependencies

npm install

3. Configure backend URL

Create or edit .env file:

REACT_APP_API_URL=http://127.0.0.1:5000

4. Start the frontend

npm start

Frontend runs at http://localhost:3000.

## Testing with Postman

Auth Flow

Signup: POST /auth/signup with { "username": "charlie", "password": "password123" }

Login: POST /auth/login with { "username": "alice", "password": "password123" }

Copy JWT token from response.

Protected Routes

Get current user: GET /auth/me with Authorization: Bearer <token>

Get notes: GET /notes/ with Authorization: Bearer <token>

Create note: POST /notes/ with JSON body and token

Update note: PATCH /notes/<id> with JSON body and token

Delete note: DELETE /notes/<id> with token

Expected status codes: 200 OK, 201 Created, 204 No Content, 401 Unauthorized.

## Testing with Frontend

Start backend (flask run) and frontend (npm start).

Log in as alice or bob with password password123.

View seeded notes in the UI.

Create, update, and delete notes through the interface.

## Notes

Use client-with-jwt only, since backend uses JWT.

Add Flask-CORS to backend if frontend requests are blocked:

from flask_cors import CORS
CORS(app)

## Summary

Backend: Flask + JWT, seeded users and notes.

Frontend: React JWT client.

Tested with Postman and frontend UI.

Full CRUD cycle confirmed with JWT protection.
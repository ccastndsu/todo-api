# To-Do API Backend

This is a simple backend REST API for a to-do application, built with FastAPI and PostgreSQL.

## Getting Started

1. Clone the repository (if you haven't already).
2. Navigate to the `todo-api` directory.
3. Run `docker-compose up --build` to start the API and Postgres database.
4. Access the API docs at `http://localhost:8000/docs`.

## Endpoints
- `GET /todos/` - List all to-dos
- `POST /todos/` - Create a new to-do
- `GET /todos/{id}` - Get a to-do by ID
- `PUT /todos/{id}` - Update a to-do
- `DELETE /todos/{id}` - Delete a to-do

## Requirements
- Docker & Docker Compose

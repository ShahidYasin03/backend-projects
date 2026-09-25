# Backend Projects

Practice projects for learning backend development.

## Structure

```text
backend-projects/
|-- README.md
|-- .gitignore
`-- projects/
	|-- fastAPI-student-db/
	|-- flask+API+frontend-connection/
	|-- url-shortener/
	`-- pythonSQL/
```

Each folder inside `projects/` is an independent practice project. New projects
should be added as a new folder there, with their own source files,
dependencies, configuration, and README when needed.

## Existing projects

- `fastAPI-student-db`: student management API using FastAPI, PostgreSQL, and psycopg2
- `flask+API+frontend-connection`: Flask API connected to a simple frontend
- `url-shortener`: FastAPI URL shortener using PostgreSQL and Base62 short codes
- `pythonSQL`: CLI student management project using Python and PostgreSQL

## URL shortener

The URL shortener is located in `projects/url-shortener/`. It supports:

- Creating short URLs from long URLs
- Redirecting from a short code to the original URL
- Viewing URL details, creation time, and click count

### Run locally

From the project directory, create a `.env` file with a PostgreSQL connection
string:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/database_name
```

Install dependencies and start the development server:

```powershell
cd projects/url-shortener
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The API is available at `http://127.0.0.1:8000`. Interactive documentation is
available at `/docs`.

### Endpoints

| Method | Path                 | Purpose                              |
| ------ | -------------------- | ------------------------------------ |
| `POST` | `/urls`              | Create a short URL                   |
| `GET`  | `/{short_code}`      | Redirect to the original URL         |
| `GET`  | `/urls/{short_code}` | View URL information and click count |

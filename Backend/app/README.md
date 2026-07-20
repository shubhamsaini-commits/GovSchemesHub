# SchemeHub Backend

Flask REST API backend for SchemeHub — a platform for publishing and discovering government/public welfare schemes.

## Stack

- Python 3.11+
- Flask
- Flask-SQLAlchemy / Flask-Migrate
- MySQL (PyMySQL driver)
- Flask-JWT-Extended
- Flask-Bcrypt
- Flask-CORS
- python-dotenv

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

cp .env.example .env
# edit .env with your DB credentials and secrets

flask db init
flask db migrate -m "initial migration"
flask db upgrade

python run.py
```

## API Endpoints

### Auth
| Method | Endpoint | Description |
|---|---|---|
| POST | /api/auth/register | Register a new user |
| POST | /api/auth/login | Login and receive tokens |
| POST | /api/auth/refresh | Refresh access token |
| POST | /api/auth/logout | Revoke current access token |
| GET | /api/auth/profile | Get current user profile |

### Schemes
| Method | Endpoint | Description |
|---|---|---|
| POST | /api/schemes | Create a scheme |
| GET | /api/schemes | List schemes (paginated, filterable) |
| GET | /api/schemes/:id | Get a single scheme |
| PUT | /api/schemes/:id | Update a scheme |
| DELETE | /api/schemes/:id | Delete a scheme |
| POST | /api/schemes/:id/upload | Upload a document for a scheme |

### Health
| Method | Endpoint | Description |
|---|---|---|
| GET | /api/health | Health check |

## Running Tests

```bash
pytest
```

## Project Structure

```
SchemeHub/
├── run.py
├── requirements.txt
├── .env.example
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── extensions.py
│   ├── routes/
│   ├── controllers/
│   ├── services/
│   ├── models/
│   ├── utils/
│   ├── middleware/
│   ├── uploads/
│   └── logs/
├── tests/
├── migrations/
└── instance/
```

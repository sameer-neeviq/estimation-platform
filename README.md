# Estimation Platform

A FastAPI-based estimation platform for project cost and time estimation.

## Project Structure

```
estimation-platform/
├── .gitignore
├── README.md
├── Dockerfile
├── requirements.txt
├── docker-compose.dev.yml
├── Makefile
├── alembic.ini
├── app/
│   ├── main.py
│   ├── models/
│   ├── routers/
│   ├── schemas/
│   ├── services/
│   ├── core/
│   │   └── config.py
│   ├── db/
│   │   ├── database.py
│   │   └── base.py
│   └── __init__.py
├── alembic/
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
├── tests/
│   ├── conftest.py
│   ├── test_main.py
│   └── __init__.py
└── venv/   (ignored)
```

## Getting Started

### Prerequisites

- Python 3.11+
- Docker and Docker Compose
- PostgreSQL (for production)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd estimation-platform
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
make install
# or
pip install -r requirements.txt
```

### Development

1. Start the development environment:
```bash
make dev-up
```

2. The API will be available at:
   - API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs
   - Alternative docs: http://localhost:8000/redoc

3. Stop the development environment:
```bash
make dev-down
```

### Testing

Run tests:
```bash
make test
```

### Database Migrations

Generate a new migration:
```bash
make migrate msg="your migration message"
```

Apply migrations:
```bash
make upgrade
```

## Available Commands

- `make help` - Show available commands
- `make install` - Install dependencies
- `make dev-up` - Start development environment
- `make dev-down` - Stop development environment
- `make test` - Run tests
- `make lint` - Run linting
- `make format` - Format code
- `make clean` - Clean up containers and volumes
- `make migrate` - Generate new migration
- `make upgrade` - Apply migrations

## Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/estimation_platform
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
ENVIRONMENT=development
```

## API Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check
- `GET /docs` - API documentation (Swagger UI)
- `GET /redoc` - Alternative API documentation

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for your changes
5. Run tests and ensure they pass
6. Submit a pull request
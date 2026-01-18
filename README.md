# KPI System - Departmental Performance Management

A comprehensive, scalable system for managing Key Performance Indicators (KPIs) for the Software Engineering Department.

## Features

- **Automated KPI Calculation**: Compute department performance metrics automatically
- **Real-time Analytics**: Dashboard with real-time performance data
- **Automated Reporting**: Generate comprehensive reports in PDF and Excel formats
- **RESTful API**: Complete API for external integrations
- **Data Integration**: Connect with GitHub, LMS, surveys, and academic systems
- **Scalable Architecture**: Built with FastAPI, PostgreSQL, and Redis

## Tech Stack

- **Backend**: Python 3.11+, FastAPI
- **Database**: PostgreSQL with Redis caching
- **Task Queue**: Celery with Redis broker
- **Authentication**: JWT tokens with bcrypt hashing
- **Deployment**: Docker & Docker Compose (optional)

## Prerequisites

- Python 3.11+ (Python 3.13 supported)
- PostgreSQL 12+
- Redis 6+ (optional, for caching and task queue)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-org/kpi-system.git
cd kpi-system
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate

# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Copy the example environment file and update with your settings:

```bash
cp .env.example .env
```

Edit the `.env` file with your database credentials:

```env
# Database Configuration
DB_NAME=kpi_db
PGUSER=postgres
PGPASSWORD=postgres
PGHOST=127.0.0.1
PGPORT=5432

# JWT Configuration
SECRET_KEY=your-secret-key-change-in-production
JWT_SECRET_KEY=your-jwt-secret-key-change-in-production
```

### 5. Set Up PostgreSQL Database

Make sure PostgreSQL is running and create the database:

```bash
# Connect to PostgreSQL
psql -U postgres

# Create database
CREATE DATABASE kpi_db;

# Exit psql
\q
```

### 6. Run Database Migrations

Apply the database migrations to create all tables:

```bash
alembic upgrade head
```

### 7. Run the Development Server

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`
- **API Documentation (Swagger)**: `http://localhost:8000/api/v1/docs`
- **ReDoc**: `http://localhost:8000/api/v1/redoc`

## Database Migrations

This project uses Alembic for database migrations.

```bash
# Apply all pending migrations
alembic upgrade head

# Create a new migration after changing models
alembic revision --autogenerate -m "Description of changes"

# Rollback the last migration
alembic downgrade -1

# View migration history
alembic history

# View current migration version
alembic current
```

## Quick Start Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Apply database migrations
alembic upgrade head

# Run development server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Run tests
pytest tests/ -v

# Format code
black app/ tests/ scripts/
isort app/ tests/ scripts/
```

## Using Make Commands (Optional)

If you have `make` installed:

```bash
make help          # Show all available commands
make dev           # Run development server
make test          # Run tests with coverage
make lint          # Run code linting
make format        # Format code with black and isort
make migrate       # Run database migrations
make init-db       # Initialize database
make seed          # Seed sample data
```

## Project Structure

```
kpi-system/
├── app/                    # Main application package
│   ├── core/              # Core modules (config, security, exceptions)
│   ├── api/               # API endpoints
│   ├── models/            # SQLAlchemy ORM models
│   ├── schemas/           # Pydantic request/response models
│   ├── services/          # Business logic
│   ├── crud/              # Database operations
│   ├── db/                # Database configuration
│   └── main.py            # FastAPI application entry point
├── tests/                  # Test suite
├── scripts/               # Utility scripts
├── docker/                # Docker configuration
├── docs/                  # Documentation
└── README.md              # This file
```

## API Documentation

### Authentication

All API endpoints require JWT authentication. Include the token in the Authorization header:

```
Authorization: Bearer <your_token>
```

### Available Endpoints

- `GET /api/v1/health` - Health check
- `GET /api/v1/` - API information
- More endpoints coming in Phase 2

## Development

### Code Style

The project uses:
- **Black** for code formatting
- **isort** for import sorting
- **Flake8** for linting
- **mypy** for type checking

Format your code before committing:

```bash
make format
make lint
```

### Testing

Run tests with:

```bash
make test
```

### Database Migrations

Create a new migration:

```bash
alembic revision --autogenerate -m "description"
```

Apply migrations:

```bash
make migrate
```

## Environment Variables

Configure these in your `.env` file:

| Variable | Description | Default |
|----------|-------------|---------|
| `DB_NAME` | PostgreSQL database name | `kpi_db` |
| `PGUSER` | PostgreSQL username | `postgres` |
| `PGPASSWORD` | PostgreSQL password | `postgres` |
| `PGHOST` | PostgreSQL host | `127.0.0.1` |
| `PGPORT` | PostgreSQL port | `5432` |
| `SECRET_KEY` | Application secret key | - |
| `JWT_SECRET_KEY` | Secret key for JWT signing | - |
| `REDIS_URL` | Redis connection string | `redis://localhost:6379/0` |
| `GITHUB_TOKEN` | GitHub API token (optional) | - |

## Deployment

### Using Docker (Optional)

Deploy using Docker Compose:

```bash
docker-compose -f docker/docker-compose.yml up -d
```

For production:

```bash
docker-compose -f docker/docker-compose.prod.yml up -d
```

## Contributing

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Make your changes
3. Format code: `make format`
4. Run tests: `make test`
5. Commit: `git commit -am "Add your feature"`
6. Push: `git push origin feature/your-feature`
7. Create a Pull Request

## License

MIT License - See LICENSE file for details

## Support

For support, please open an issue on GitHub or contact the development team.

---

**Version**: 1.0.0  
**Last Updated**: January 2026

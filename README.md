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
- **Deployment**: Docker & Docker Compose

## Prerequisites

- Python 3.11+
- PostgreSQL 12+
- Redis 6+
- Docker & Docker Compose (optional)

## Installation

### Local Development

```bash
# Clone repository
git clone https://github.com/your-org/kpi-system.git
cd kpi-system

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
make install

# Copy environment file
cp .env.example .env

# Start Docker services
make docker-up

# Initialize database
make init-db
make migrate

# Seed sample data (optional)
make seed

# Run development server
make dev
```

The API will be available at `http://localhost:8000`
- API Documentation: `http://localhost:8000/api/v1/docs`
- ReDoc: `http://localhost:8000/api/v1/redoc`

## Available Commands

```bash
make help          # Show all available commands
make dev           # Run development server
make test          # Run tests with coverage
make lint          # Run code linting
make format        # Format code with black and isort
make docker-up     # Start Docker services
make docker-down   # Stop Docker services
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

See `.env.example` for all available configuration options.

Key variables:
- `DATABASE_URL`: PostgreSQL connection string
- `REDIS_URL`: Redis connection string
- `JWT_SECRET_KEY`: Secret key for JWT signing
- `GITHUB_TOKEN`: GitHub API token (optional)

## Deployment

### Docker

Deploy using Docker Compose:

```bash
make docker-up
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
**Last Updated**: January 2024

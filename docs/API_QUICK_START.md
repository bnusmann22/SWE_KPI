# KPI System API - Quick Start Guide

## Getting Started

### Prerequisites
- Python 3.11+
- PostgreSQL 12+
- Redis 6+

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/your-org/kpi-system.git
cd kpi-system
```

2. **Set up virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt -r requirements-dev.txt
```

4. **Configure environment**
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. **Start services**
```bash
docker-compose -f docker/docker-compose.yml up -d
```

6. **Initialize database**
```bash
python scripts/init_db.py
python scripts/seed_data.py
```

7. **Run development server**
```bash
uvicorn app.main:app --reload
```

API will be available at `http://localhost:8000`

## API Endpoints

### Health Check
```
GET /health
```

### Authentication

#### Register
```bash
POST /api/v1/auth/register
Content-Type: application/json

{
  "email": "user@example.com",
  "username": "username",
  "password": "password123",
  "full_name": "John Doe"
}
```

#### Login
```bash
POST /api/v1/auth/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "password123"
}

Response:
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "token_type": "bearer"
}
```

### Students

#### Create Student
```bash
POST /api/v1/students
Content-Type: application/json
Authorization: Bearer {token}

{
  "matric_number": "CSC/2021/001",
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@student.edu",
  "department_id": 1,
  "level": 300,
  "github_username": "johndoe"
}
```

#### Get Student
```bash
GET /api/v1/students/{student_id}
Authorization: Bearer {token}
```

#### List Students
```bash
GET /api/v1/students?skip=0&limit=10&department_id=1
Authorization: Bearer {token}
```

#### Update Student
```bash
PUT /api/v1/students/{student_id}
Content-Type: application/json
Authorization: Bearer {token}

{
  "github_username": "newgithubusername"
}
```

#### Delete Student
```bash
DELETE /api/v1/students/{student_id}
Authorization: Bearer {token}
```

## Documentation

- **Swagger UI**: http://localhost:8000/api/v1/docs
- **ReDoc**: http://localhost:8000/api/v1/redoc

## Development Workflow

### Running Tests
```bash
make test
```

### Code Formatting
```bash
make format
```

### Linting
```bash
make lint
```

### Database Migrations
```bash
alembic revision --autogenerate -m "description"
alembic upgrade head
```

## Common Issues

### Database Connection Error
- Ensure PostgreSQL is running: `docker-compose up -d postgres`
- Check DATABASE_URL in .env file
- Verify credentials match docker-compose.yml

### Redis Connection Error
- Ensure Redis is running: `docker-compose up -d redis`
- Check REDIS_URL in .env file

### Port Already in Use
- Change port in docker-compose.yml or .env
- Or kill process using the port

## Support

For issues or questions, please open a GitHub issue or contact the development team.

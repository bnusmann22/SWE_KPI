# Development Guide

## Project Structure

```
kpi-system/
├── app/                    # Main application
│   ├── api/               # API endpoints
│   ├── core/              # Core modules
│   ├── crud/              # Database operations
│   ├── db/                # Database configuration
│   ├── models/            # ORM models
│   ├── schemas/           # Request/response schemas
│   ├── services/          # Business logic
│   ├── tasks/             # Celery tasks
│   ├── utils/             # Utility functions
│   └── main.py            # FastAPI app
├── tests/                 # Test suite
├── scripts/               # Utility scripts
├── docker/                # Docker configuration
└── docs/                  # Documentation
```

## Code Style

We follow PEP 8 with the following tools:
- **black** - Code formatting
- **isort** - Import sorting
- **flake8** - Linting
- **mypy** - Type checking

### Format Code
```bash
make format
```

### Run Linter
```bash
make lint
```

## Testing

### Run All Tests
```bash
make test
```

### Run Specific Test
```bash
pytest tests/unit/test_security.py -v
```

### Run with Coverage
```bash
pytest --cov=app --cov-report=html tests/
```

### Test Markers
```bash
pytest -m unit
pytest -m integration
```

## Adding New Endpoints

1. Create schema in `app/schemas/`
2. Create CRUD operations in `app/crud/`
3. Create endpoint in `app/api/v1/endpoints/`
4. Include router in `app/api/v1/router.py`
5. Write tests in `tests/`

Example:
```python
# app/schemas/example.py
class ExampleCreate(BaseModel):
    name: str

# app/crud/example.py
from app.crud.base import CRUDBase
from app.models.example import Example

crud_example = CRUDBase(Example)

# app/api/v1/endpoints/example.py
from fastapi import APIRouter
from app.crud.example import crud_example

router = APIRouter(prefix="/examples")

@router.post("", response_model=ExampleResponse)
async def create_example(data: ExampleCreate, db: Session = Depends(get_db)):
    return crud_example.create(db=db, obj_in=data.model_dump())
```

## Database Migrations

### Create Migration
```bash
alembic revision --autogenerate -m "Add new_field to users"
```

### Apply Migrations
```bash
alembic upgrade head
```

### Rollback
```bash
alembic downgrade -1
```

## Debugging

Enable debug mode in `.env`:
```
DEBUG=true
LOG_LEVEL=DEBUG
```

Use logging in code:
```python
from app.core.logging import get_logger

logger = get_logger(__name__)
logger.debug("Debug message")
logger.info("Info message")
logger.error("Error message")
```

## Git Workflow

1. Create feature branch: `git checkout -b feature/your-feature`
2. Make changes and commit: `git commit -am "description"`
3. Push: `git push origin feature/your-feature`
4. Create Pull Request
5. Wait for review and approval
6. Merge to main

## Performance Tips

1. Use database indexes on frequently queried columns
2. Implement caching for expensive operations
3. Use connection pooling for database
4. Profile code with `pytest-benchmark`
5. Monitor with Sentry or DataDog

## Security

- Never commit `.env` file
- Use environment variables for secrets
- Implement rate limiting
- Validate all inputs
- Use parameterized queries
- Keep dependencies updated

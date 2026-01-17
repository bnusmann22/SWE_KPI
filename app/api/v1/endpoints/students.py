"""Student endpoints."""

from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.crud.student import crud_student
from app.db.session import get_db
from app.schemas.student import StudentCreate, StudentUpdate, StudentResponse
from app.schemas.common import PaginationParams, PaginatedResponse

router = APIRouter(prefix="/students")


@router.post("", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
async def create_student(
    data: StudentCreate,
    db: Session = Depends(get_db),
):
    """
    Create a new student record.

    Args:
        data: Student data
        db: Database session

    Returns:
        Created student
    """
    # Check if matric number already exists
    existing = crud_student.get_by_matric(db=db, matric_number=data.matric_number)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Matric number already exists",
        )

    student = crud_student.create(db=db, obj_in=data.model_dump())
    return student


@router.get("/{student_id}", response_model=StudentResponse)
async def get_student(
    student_id: int,
    db: Session = Depends(get_db),
):
    """
    Get a student by ID.

    Args:
        student_id: Student ID
        db: Database session

    Returns:
        Student data
    """
    student = crud_student.get(db=db, id=student_id)
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )
    return student


@router.get("", response_model=PaginatedResponse)
async def list_students(
    skip: int = 0,
    limit: int = 10,
    department_id: Optional[int] = None,
    db: Session = Depends(get_db),
):
    """
    List all students with pagination.

    Args:
        skip: Number of records to skip
        limit: Number of records to return
        department_id: Filter by department
        db: Database session

    Returns:
        Paginated student list
    """
    query = db.query(crud_student.model)

    if department_id:
        query = query.filter(crud_student.model.department_id == department_id)

    total = query.count()
    students = query.offset(skip).limit(limit).all()

    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "items": students,
    }


@router.put("/{student_id}", response_model=StudentResponse)
async def update_student(
    student_id: int,
    data: StudentUpdate,
    db: Session = Depends(get_db),
):
    """
    Update a student record.

    Args:
        student_id: Student ID
        data: Update data
        db: Database session

    Returns:
        Updated student
    """
    student = crud_student.get(db=db, id=student_id)
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )

    update_data = data.model_dump(exclude_unset=True)
    student = crud_student.update(db=db, db_obj=student, obj_in=update_data)
    return student


@router.delete("/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_student(
    student_id: int,
    db: Session = Depends(get_db),
):
    """
    Delete a student record.

    Args:
        student_id: Student ID
        db: Database session
    """
    student = crud_student.get(db=db, id=student_id)
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )

    crud_student.remove(db=db, id=student_id)

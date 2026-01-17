"""Authentication schemas."""

from pydantic import BaseModel, EmailStr, Field


class TokenResponse(BaseModel):
    """JWT token response."""

    access_token: str = Field(..., description="JWT access token")
    refresh_token: str = Field(..., description="JWT refresh token")
    token_type: str = Field(default="bearer", description="Token type")


class LoginRequest(BaseModel):
    """Login request body."""

    email: EmailStr = Field(..., description="User email")
    password: str = Field(..., min_length=6, description="User password")


class RegisterRequest(BaseModel):
    """User registration request."""

    email: EmailStr = Field(..., description="User email")
    username: str = Field(..., min_length=3, max_length=100, description="Username")
    password: str = Field(..., min_length=8, description="User password")
    full_name: str = Field(None, max_length=255, description="Full name")


class UserResponse(BaseModel):
    """User response schema."""

    id: int
    email: str
    username: str
    full_name: str | None
    is_active: bool
    is_superuser: bool

    class Config:
        from_attributes = True

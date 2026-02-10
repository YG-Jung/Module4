from datetime import datetime
from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    """회원가입 요청 스키마"""
    email: EmailStr
    username: str
    password: str = Field(..., min_length=8, description="비밀번호 (최소 8자)")


class UserResponse(BaseModel):
    """사용자 응답 스키마 (비밀번호 제외)"""
    id: int
    email: str
    username: str
    created_at: datetime
    updated_at: datetime | None

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    """로그인 요청 스키마"""
    email: EmailStr
    password: str

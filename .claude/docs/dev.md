# 개발 진행 현황

## Feature 1: User 모델 및 인증 스키마 개선

### 작업 개요
사용자 인증 시스템의 기초가 되는 User 모델과 스키마를 login_todo.md 요구사항에 맞춰 개선합니다.

### 필요한 수정사항

#### 1. User 모델 (`backend/app/models/user.py`)
- **작업**: username에 unique 제약조건 추가
- **변경**: `Column(String(100), nullable=False)` → `Column(String(100), unique=True, nullable=False, index=True)`
- **이유**: 사용자명 중복 방지 및 조회 성능 향상

#### 2. UserCreate 스키마 (`backend/app/schemas/user.py`)
- **작업**: password 필드에 최소 길이 검증 추가
- **변경**: `password: str` → `password: str = Field(..., min_length=8, description="비밀번호 (최소 8자)")`
- **이유**: 비밀번호 보안 강화 및 API 문서 자동 업데이트

#### 3. UserResponse 스키마 (`backend/app/schemas/user.py`)
- **작업**: updated_at 필드 추가
- **변경**: `updated_at: datetime | None` 필드 추가
- **이유**: 사용자 정보 수정 시간 추적

### 검증 방법
1. 백엔드 서버 실행: `cd backend && .venv\Scripts\activate && uvicorn app.main:app --reload`
2. http://localhost:8000/docs 에서 API 문서 확인
3. 데이터베이스 테이블의 UNIQUE 제약조건 확인

### 다음 단계
- Feature 2: 비밀번호 해싱 및 보안 유틸리티
- Feature 3: JWT 토큰 생성 및 검증

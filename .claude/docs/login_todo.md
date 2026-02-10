# Login 기능 개발 계획

## 개요
사용자 인증 시스템 구현 (회원가입, 로그인, 로그아웃, 인증 상태 관리)

---

## Feature 1: User 모델 및 인증 스키마 설계

### BE
- [ ] User 모델 생성 (`backend/app/models/user.py`)
  - id, email, username, hashed_password, created_at, updated_at
- [ ] User 관련 Pydantic 스키마 생성 (`backend/app/schemas/user.py`)
  - UserCreate, UserResponse, UserLogin
- [ ] 데이터베이스 마이그레이션 (User 테이블 생성)

### FE
- [ ] 해당 없음

### Kernel
- [ ] 해당 없음

---

## Feature 2: 비밀번호 해싱 및 보안 유틸리티

### BE
- [ ] 비밀번호 해싱 유틸리티 함수 구현 (`backend/app/utils/security.py`)
  - bcrypt 또는 passlib 사용
  - `hash_password()`, `verify_password()` 함수
- [ ] 환경변수 설정 (`.env`)
  - SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

### FE
- [ ] 해당 없음

### Kernel
- [ ] 해당 없음

---

## Feature 3: JWT 토큰 생성 및 검증

### BE
- [ ] JWT 토큰 생성 함수 구현 (`backend/app/utils/security.py`)
  - `create_access_token()` 함수
  - python-jose 라이브러리 사용
- [ ] JWT 토큰 검증 함수 구현
  - `decode_access_token()` 함수
- [ ] 토큰 의존성 함수 (`get_current_user()`)
  - FastAPI Depends로 활용

### FE
- [ ] 해당 없음

### Kernel
- [ ] 해당 없음

---

## Feature 4: 회원가입 API

### BE
- [ ] 회원가입 엔드포인트 구현 (`backend/app/routers/auth.py`)
  - POST `/api/auth/register`
  - 이메일 중복 체크
  - 비밀번호 해싱 후 저장
- [ ] 유효성 검증 (이메일 형식, 비밀번호 길이 등)

### FE
- [ ] 회원가입 페이지 생성 (`frontend/src/app/register/page.tsx`)
  - 이메일, 사용자명, 비밀번호 입력 폼
  - 폼 유효성 검증 (클라이언트 측)
- [ ] 회원가입 API 호출 함수 (`frontend/src/lib/api/auth.ts`)

### Kernel
- [ ] 해당 없음

---

## Feature 5: 로그인 API

### BE
- [ ] 로그인 엔드포인트 구현 (`backend/app/routers/auth.py`)
  - POST `/api/auth/login`
  - 사용자 인증 (이메일/비밀번호 검증)
  - JWT 토큰 발급 및 반환
- [ ] 로그인 실패 처리 (401 Unauthorized)

### FE
- [ ] 로그인 페이지 생성 (`frontend/src/app/login/page.tsx`)
  - 이메일, 비밀번호 입력 폼
- [ ] 로그인 API 호출 함수 (`frontend/src/lib/api/auth.ts`)
- [ ] 로그인 성공 시 토큰 저장 (localStorage 또는 cookie)

### Kernel
- [ ] 해당 없음

---

## Feature 6: 인증 미들웨어 및 보호된 라우트

### BE
- [ ] 인증 필수 엔드포인트 보호
  - `get_current_user` 의존성 적용
- [ ] 현재 사용자 정보 조회 엔드포인트
  - GET `/api/auth/me`
- [ ] 에러 핸들링 (토큰 만료, 유효하지 않은 토큰)

### FE
- [ ] 해당 없음 (Feature 7에서 처리)

### Kernel
- [ ] 해당 없음

---

## Feature 7: 프론트엔드 인증 상태 관리

### BE
- [ ] 해당 없음

### FE
- [ ] 인증 컨텍스트 생성 (`frontend/src/contexts/AuthContext.tsx`)
  - 로그인 상태, 사용자 정보 관리
  - login, logout, checkAuth 함수
- [ ] 토큰 자동 갱신 로직 (옵션)
- [ ] API 요청 시 토큰 자동 포함 (Axios interceptor 또는 fetch wrapper)
  - `frontend/src/lib/api/client.ts`

### Kernel
- [ ] 해당 없음

---

## Feature 8: 로그아웃 기능

### BE
- [ ] 로그아웃 엔드포인트 (옵션)
  - POST `/api/auth/logout`
  - 토큰 블랙리스트 처리 (필요 시)

### FE
- [ ] 로그아웃 버튼 추가 (헤더/네비게이션)
- [ ] 로그아웃 처리
  - 토큰 삭제 (localStorage/cookie)
  - 인증 상태 초기화
  - 로그인 페이지로 리다이렉트

### Kernel
- [ ] 해당 없음

---

## Feature 9: 보호된 페이지 라우팅

### BE
- [ ] 해당 없음

### FE
- [ ] 인증 라우트 가드 생성 (`frontend/src/components/AuthGuard.tsx`)
  - 미인증 사용자 로그인 페이지로 리다이렉트
- [ ] 보호된 페이지에 AuthGuard 적용
  - 예: 대시보드, 프로필 페이지 등
- [ ] 인증 여부에 따른 네비게이션 UI 변경
  - 로그인/회원가입 버튼 vs 로그아웃/프로필 버튼

### Kernel
- [ ] 해당 없음

---

## Feature 10: 사용자 프로필 관리

### BE
- [ ] 프로필 조회 엔드포인트
  - GET `/api/users/me`
- [ ] 프로필 수정 엔드포인트
  - PUT `/api/users/me`
  - username, email 변경 (인증 필수)
- [ ] 비밀번호 변경 엔드포인트
  - POST `/api/users/change-password`

### FE
- [ ] 프로필 페이지 생성 (`frontend/src/app/profile/page.tsx`)
  - 사용자 정보 표시
  - 프로필 수정 폼
- [ ] 프로필 수정 API 호출
- [ ] 비밀번호 변경 UI

### Kernel
- [ ] 해당 없음

---

## 추가 고려사항

### 보안
- [ ] CORS 설정 확인
- [ ] HTTPS 적용 (프로덕션)
- [ ] Rate limiting (로그인 시도 제한)
- [ ] SQL Injection 방지 (SQLAlchemy ORM 사용으로 기본 방어)

### 테스트
- [ ] BE: 인증 API 유닛 테스트
- [ ] FE: 로그인/회원가입 폼 테스트

### 문서화
- [ ] API 문서 업데이트 (Swagger)
- [ ] README에 인증 플로우 설명 추가

---

## 개발 우선순위

1. Feature 1, 2, 3 (기반 작업)
2. Feature 4, 5 (회원가입/로그인 핵심 기능)
3. Feature 6, 7, 8 (인증 미들웨어 및 상태 관리)
4. Feature 9 (보호된 라우팅)
5. Feature 10 (프로필 관리)

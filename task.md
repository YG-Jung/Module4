# Task List

## 로그인 기능 개발

### 완료된 작업
- [x] Feature 1: User 모델 및 인증 스키마 설계 (2026-02-10)
  - User 모델 개선 (username unique, index 추가)
  - UserCreate 스키마 개선 (password 최소 8자 검증)
  - UserResponse 스키마 개선 (updated_at 필드 추가)

### 진행 중
- [ ] Feature 2: 비밀번호 해싱 및 보안 유틸리티
- [ ] Feature 3: JWT 토큰 생성 및 검증

### 대기 중
- [ ] Feature 4: 회원가입 API
- [ ] Feature 5: 로그인 API
- [ ] Feature 6: 인증 미들웨어 및 보호된 라우트
- [ ] Feature 7: 프론트엔드 인증 상태 관리
- [ ] Feature 8: 로그아웃 기능
- [ ] Feature 9: 보호된 페이지 라우팅
- [ ] Feature 10: 사용자 프로필 관리

## 우선순위
1. Feature 2, 3 (기반 작업) - 인증 유틸리티 구현
2. Feature 4, 5 (핵심 기능) - 회원가입/로그인 API
3. Feature 6, 7, 8 (인증 시스템) - 미들웨어 및 상태 관리
4. Feature 9, 10 (추가 기능) - 라우팅 및 프로필

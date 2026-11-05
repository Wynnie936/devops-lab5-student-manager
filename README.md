# Student Manager

Ứng dụng quản lý sinh viên — DevOps Lab 5

**Version 1.1.0** — Phát triển bởi Nhóm A & Nhóm B

## Tính năng
- Quản lý thông tin sinh viên (Student Model)
- Thêm sinh viên mới (add_student)
- Tìm kiếm sinh viên theo tên hoặc mã (search_student)
- Unit test (`python -m unittest discover tests`)
- Pre-commit hook kiểm tra cú pháp Python

## Cài đặt & Chạy

```bash
git clone https://github.com/Wynnie936/devops-lab5-student-manager.git
cd devops-lab5-student-manager
python src/main.py

# Bật pre-commit hook (chạy 1 lần sau khi clone)
git config core.hooksPath .githooks

# Chạy unit test
python -m unittest discover tests
```

## Phiên bản (Releases)
| Tag | Nội dung |
|-----|----------|
| [v1.0.0](https://github.com/Wynnie936/devops-lab5-student-manager/releases/tag/v1.0.0) | Hoàn thành 7 bước Lab 5: add_student, search_student, README |
| [v1.1.0](https://github.com/Wynnie936/devops-lab5-student-manager/releases/tag/v1.1.0) | Bài tập mở rộng: pre-commit hook, .gitignore, unit test, branch protection |

So sánh 2 phiên bản: [v1.0.0...v1.1.0](https://github.com/Wynnie936/devops-lab5-student-manager/compare/v1.0.0...v1.1.0) — chi tiết trong [CHANGELOG.md](CHANGELOG.md)

## Quy ước làm việc
- **Git Flow:** `main` (release) ← `develop` ← `feature/*`
- **Conventional Commits:** `feat:`, `fix:`, `docs:`, `refactor:`, `test:`
- **Branch protection:** không push trực tiếp vào `main`, bắt buộc PR + 1 review

## Công nghệ
- Python 3.x
- Git & GitHub (Git Flow)

## Tác giả
- Nhóm A & Nhóm B — DevOps Course, Bài 5

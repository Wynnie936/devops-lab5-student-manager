# Changelog

Mọi thay đổi đáng chú ý của dự án được ghi tại đây.
Định dạng theo [Keep a Changelog](https://keepachangelog.com/vi/1.1.0/), đánh số theo [Semantic Versioning](https://semver.org/lang/vi/).

## [1.1.0] — 2026-11-05
### Added
- Pre-commit hook (`.githooks/pre-commit`) kiểm tra cú pháp Python trước khi commit
- Unit test cho `add_student()` và `search_student()` (`tests/test_main.py`)
- Hiển thị phiên bản ứng dụng ở đầu chương trình
- `.env.example` — mẫu biến môi trường
### Fixed
- `.gitignore` bỏ qua thêm các file private: `.env.*`, `*.key`, `*.pem`, `secrets/`, `credentials.json`
### Security
- Nhánh `main` được bảo vệ (branch protection): bắt buộc Pull Request + 1 review

## [1.0.0] — 2026-11-04
### Added
- Lớp `Student` (model sinh viên)
- `add_student()` — thêm sinh viên, chặn trùng mã (PR #1)
- `search_student()` — tìm theo tên/mã, không phân biệt hoa thường (PR #2)
- README hoàn chỉnh; giải quyết merge conflict README giữa Team A & Team B

[1.1.0]: https://github.com/Wynnie936/devops-lab5-student-manager/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/Wynnie936/devops-lab5-student-manager/releases/tag/v1.0.0

"""
Input
Người dùng nhập số lượng phiếu đăng ký cần xử lý.
Mỗi phiếu đăng ký là một chuỗi gồm 4 phần:
Họ tên học viên
Tên khóa học
Mã học viên
Email
Các phần được phân tách bằng dấu |.

Output
Hiển thị thông tin đã chuẩn hóa:
Họ tên viết hoa chữ cái đầu.
Tên khóa học viết hoa chữ cái đầu.
Mã học viên viết hoa toàn bộ.
Email viết thường toàn bộ.
In mã xác nhận theo định dạng:

Đề xuất giải pháp
Dùng input() để nhập số lượng phiếu đăng ký.
Kiểm tra số lượng phải lớn hơn 0.
Dùng vòng lặp for để nhập từng phiếu đăng ký.
Dùng split("|") để tách dữ liệu thành 4 phần.
Kiểm tra số phần tử sau khi tách:
Nếu khác 4 → báo lỗi và bỏ qua.
Dùng strip() để xóa khoảng trắng dư.
Dùng:
title() để chuẩn hóa họ tên và tên khóa học.
upper() để chuẩn hóa mã học viên.
lower() để chuẩn hóa email.
Kiểm tra email:
Nếu email không chứa @ → báo lỗi.
Kiểm tra mã học viên:
Nếu độ dài nhỏ hơn 5 ký tự → báo lỗi.
Dùng nối chuỗi để tạo mã xác nhận.


* Thiết kế thuật toán
---------------------
Bắt đầu

Nhập số lượng phiếu đăng ký

Nếu số lượng <= 0:
    In "Số lượng phiếu đăng ký không hợp lệ"
    Kết thúc chương trình

Lặp theo số lượng phiếu:

    Nhập chuỗi đăng ký

    Tách dữ liệu bằng "|"

    Nếu không đủ 4 phần:
        In "Dữ liệu đăng ký không hợp lệ"
        Bỏ qua phiếu hiện tại

    Chuẩn hóa dữ liệu:
        Họ tên -> title()
        Tên khóa học -> title()
        Mã học viên -> upper()
        Email -> lower()

    Nếu email không chứa "@":
        In "Email không hợp lệ"
        Bỏ qua phiếu hiện tại

    Nếu mã học viên có độ dài < 5:
        In "Mã học viên không hợp lệ"
        Bỏ qua phiếu hiện tại

    Tạo mã xác nhận:
        Mã học viên + "-" + tên khóa học viết hoa

    In thông tin đã chuẩn hóa

Kết thúc
"""



number_of_forms = int(input("Nhập số lượng phiếu đăng ký: "))

# Edge Case 1
if number_of_forms <= 0:
    print("Số lượng phiếu đăng ký không hợp lệ")
else:

    for i in range(number_of_forms):

        print(f"\nNhập phiếu đăng ký thứ {i + 1}:")

        registration = input(
            "Họ tên | Khóa học | Mã học viên | Email: "
        )

        # Tách dữ liệu
        parts = registration.split("|")

        # Edge Case 2
        if len(parts) != 4:
            print("Dữ liệu đăng ký không hợp lệ. Bỏ qua phiếu này")
            continue

        # Chuẩn hóa dữ liệu
        student_name = parts[0].strip().title()
        course_name = parts[1].strip().title()
        student_code = parts[2].strip().upper()
        email = parts[3].strip().lower()

        # Edge Case 3
        if "@" not in email:
            print("Email không hợp lệ. Bỏ qua phiếu này")
            continue

        # Edge Case 4
        if len(student_code) < 5:
            print("Mã học viên không hợp lệ. Bỏ qua phiếu này")
            continue

        # Tạo mã xác nhận
        confirmation_code = (
            student_code
            + "_"
            + course_name.upper().replace(" ", "-")
        )

        # In kết quả
        print("\n===== PHIẾU ĐĂNG KÝ ĐÃ CHUẨN HÓA =====")
        print("Học viên:", student_name)
        print("Khóa học:", course_name)
        print("Mã học viên:", student_code)
        print("Email:", email)
        print("Mã xác nhận:", confirmation_code)

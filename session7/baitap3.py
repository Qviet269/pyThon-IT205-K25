"""
1. Phân tích
- Input
raw_data: chuỗi chứa thông tin nhiều nhân viên.
Mỗi nhân viên gồm:
Mã nhân viên
Họ tên
Số điện thoại
Phòng ban
Các nhân viên được phân tách bằng dấu |
Các trường dữ liệu được phân tách bằng dấu :

- Output
Hiển thị dữ liệu đã chuẩn hóa:
Mã nhân viên viết hoa
Họ tên viết hoa chữ cái đầu
Phòng ban viết hoa
Số điện thoại hợp lệ được che 6 số đầu
Số điện thoại sai định dạng hiển thị "Invalid Format"

- Đề xuất giải pháp
Dùng split("|") để tách từng nhân viên.
Dùng vòng lặp for để duyệt từng nhân viên.
Dùng split(":") để tách thông tin nhân viên.
Dùng strip() để xóa khoảng trắng dư.
Dùng upper() để viết hoa mã nhân viên và phòng ban.
Dùng title() để chuẩn hóa họ tên.
Dùng replace("-", "") để xóa dấu - trong số điện thoại.
Dùng isdigit() để kiểm tra số điện thoại hợp lệ.
Dùng slicing: phone[-4:]


* Thiết kế thuật toán
-----------------------

Bắt đầu

Khai báo raw_data

Hiển thị menu

Nếu chọn xem dữ liệu:
    In raw_data

Nếu chọn chuẩn hóa dữ liệu:
    Tách nhân viên bằng "|"

    Duyệt từng nhân viên:
        Xóa khoảng trắng
        Tách dữ liệu bằng ":"

        Chuẩn hóa:
            emp_id -> upper()
            fullname -> title()
            department -> upper()

        Xử lý phone:
            Xóa dấu "-"
            Nếu phone hợp lệ:
                Che 6 số đầu
            Ngược lại:
                Gán "Invalid Format"

        In thông tin

Nếu chọn tìm kiếm:
    Nhập mã nhân viên
    Duyệt danh sách nhân viên
    Nếu tìm thấy:
        In thông tin

Nếu chọn thoát:
    Kết thúc chương trình

Kết thúc

"""


# 2. triển khai code
# sửa lại
raw_data = " eMP-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT "

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ NHÂN SỰ =====")
    print("1. Hiển thị dữ liệu gốc")
    print("2. Chuẩn hóa dữ liệu và in báo cáo")
    print("3. Tìm kiếm nhân viên theo ID")
    print("4. Thoát chương trình")

    choice = input('Chọn chức năng: ')

    if choice == "1":
        print(raw_data)
        
    elif choice == "2":
        employees = raw_data.split("|")

        for e in employees:
            info = e.strip().split(";")

            e_id = info[0].strip().upper()
            fullname = info[1].strip().title()
            phone = info[2].strip().replace("-", "")
            department = info[3].strip().upper()

            # Khắc phục lỗi hiển thị khi sai định dạng số điện thoại
            if phone.isdigit():
                phone_display = f"****** {phone[-4:]}"
            else:
                phone_display = "Invalid Format"

            print(f"""
ID            : {e_id}
Họ tên        : {fullname}
Số điện thoại : {phone_display}
Phòng ban     : {department}
""")
            
    elif choice == "3":
        # Chuẩn hóa mã nhập vào (Xóa khoảng trắng, chuyển thành chữ hoa)
        search_id = input("Nhập mã nhân viên cần tìm: ").strip().upper()
        
        employees = raw_data.split("|")
        found = False  # Biến cờ hiệu để kiểm tra trạng thái tìm thấy

        for e in employees:
            info = e.strip().split(";")

            e_id = info[0].strip().upper()
            fullname = info[1].strip().title()
            phone = info[2].strip().replace("-", "")
            department = info[3].strip().upper()
            
            if search_id == e_id:
                found = True
                if phone.isdigit():
                    phone_display = f"****** {phone[-4:]}"
                else:
                    phone_display = "Invalid Format"
                    
                print(f"""
Kết quả tìm thấy:
ID            : {e_id}
Họ tên        : {fullname}
Số điện thoại : {phone_display}
Phòng ban     : {department}
""")
                break  # Dừng vòng lặp khi đã tìm thấy nhân viên
                
        # Thông báo khi không tìm thấy nhân viên
        if not found:
            print(f"Không tìm thấy nhân viên có mã: {search_id}")
            
    elif choice == "4":
        print("Thoát chương trình")
        break

    else:
        print('Lựa chọn không hợp lệ!')
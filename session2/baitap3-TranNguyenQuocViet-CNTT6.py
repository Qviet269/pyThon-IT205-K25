"""
1. Phân tích và thiết kế giải pháp

Input/Output:

Đầu vào: name (dữ liệu chuỗi), age (dữ liệu số nguyên).

Đầu ra: Câu cảnh báo lỗi (nếu dữ liệu sai) hoặc Phiếu khám bệnh chứa Tên, Tuổi, Luồng khám (nếu dữ liệu đúng).

Đề xuất giải pháp: Dùng cấu trúc điều kiện lồng nhau. 
Lớp ngoài cùng làm nhiệm vụ "gác cổng" để bắt các lỗi (Edge cases). 
Chỉ khi dữ liệu sạch (không rỗng, tuổi từ 0-150) thì mới cho phép chạy vào lớp trong để phân luồng và in phiếu.

Luồng thực thi: Nhập Tên -> Kiểm tra tên rỗng -> Nhập Tuổi -> Kiểm tra tuổi hợp lệ -> Dùng if-elif-else chia 3 nhóm tuổi -> In phiếu.
"""



# 2 triển khai code
fullname_patient = input('Nhạp họ và tên bênh nhân: ');

if fullname_patient == "":
    print('Tên bệnh nhân bỏ trống hoặc chỉ toàn khoảng trắng');
else:
    age = int(input('Nhập tuổi của bệnh nhân: '));
    if age < 0 or age > 150:
        print('Tuổi bệnh nhân không hợp lý');
    else:
        if age < 6:
            result = 'ƯU TIÊN: Bệnh nhi - chuyển thắng vào phòng khám nhi.';
        elif age > 80:
            result ='ƯU TIÊN: Người cao tuổi - Hỗ trợ xe lăn, chuyển phòng khám lão khoa.';
        else: 
            result = 'KHÁM THƯỜNG: Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh.';

print('/n --- Phiếu khám bênh điện tử ---');
print(f'Tên bệnh nhân: {fullname_patient}');
print(f'Tuổi: {age}');
print(f'Kết quả phân luồng: {result}')

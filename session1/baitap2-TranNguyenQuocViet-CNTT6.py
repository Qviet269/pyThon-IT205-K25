
"""
(1) PHÂN TÍCH LỖI:
- Trace code: Nhập tên -> Nhập cân nặng -> In thông tin đã nhập -> In kiểu dữ liệu của cân nặng.
- Đặc điểm hàm input(): Hàm này mặc định luôn đọc dữ liệu người dùng nhập vào dưới dạng chuỗi ký tự (string - class 'str').
- Nguyên nhân: Do chưa ép kiểu. Dù ca nhập số (vd: 65.5) thì hàm input() vẫn coi đó là một đoạn text ("65.5"). Do đó, biến weight đang lưu một chuỗi chứ không phải một con số để tính toán.
"""

# Phần sửa lỗi viết lại mã nguồn đúng nhất

print('--- Hệ thống nhập chỉ số sinh tồn ---');

name_patient = input('Nhập tên bênh nhân: ');
weight = input('Nhạp cân nặng bệnh nhân: ');

weight = float(weight);

print("\n--- Kiếm tra dữ liệu lưu trữ ---");
print("Bệnh nhân: ", name_patient);
print("Cân nặng đã nhập: ", weight);

# phần trưởng nhóm kiếm tra
print("Cảnh báo - Kiểu dữ liệu đang lưu là: ", type(weight));
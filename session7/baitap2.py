"""
1. phân tích
- Vì chuỗi trong Python là immutable (không thể sửa trực tiếp), 
chỉ tạo ra chuỗi mới đã xóa khoảng trắng, nhưng không thay đổi chuỗi cũ.
- Chuỗi giao dịch được phân tách bằng ký tự: |
- Vì chuỗi giao dịch không dùng dấu - để phân tách dữ liệu, mà dùng dấu |.
- Sau khi tách bằng sai delimiter, dữ liệu trong parts bị lệch vì dấu - làm tách sai mã khóa học PYTHON-01, 
khiến list chỉ còn 2 phần tử thay vì 4 phần tử đúng cấu trúc ban đầu.
- Vì sau khi split("|"), mỗi phần vẫn còn khoảng trắng dư hai bên.
- Vì dữ liệu ban đầu của amount là chuỗi, còn định dạng tiền tệ cần xử lý trên kiểu số.
"""

# 2. sửa lỗi
transaction = " nguyEN vAn a | PYTHON-01 | 15000000 | paid "

transaction = transaction.strip()

parts = transaction.split("|")

# print(parts)
# print(transaction)

student_name = parts[0].strip().title()
course_code = parts[1].strip()
amount = int(parts[2].strip())
status = parts[3].strip().upper()

print(f'Học viên: {student_name}')
print(f'Khóa học: {course_code}')
print(f'Số tiền: {amount:,} VND')
print(f'Trạng thái: {status}')
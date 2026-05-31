"""
1. phân tích
- Vì strip() không sửa trực tiếp biến cũ, nó chỉ tạo ra kết quả mới.
- Vì trong chương trình hiện tại: student_name.title()
có tạo ra "Nguyen Van A" nhưng không lưu lại vào biến student_name, khi in ra sẽ không đổi.
- Vì student_code.upper() chỉ tạo ra chuỗi mới viết hoa, nhưng chương trình không gán lại cho biến student_code.
Nên giá trị của student_code vẫn giữ nguyên như cũ.
- Vì email.lower() chỉ tạo ra email mới viết thường, nhưng chương trình không gán lại cho biến email, nên giá trị email cũ vẫn giữ nguyên.
- Cần gán lại kết quả cho biến.
    student_name = student_name.title()
    email = email.lower()
    student_code = student_code.upper()
"""

# phần 2: sửa lỗi
student_name = " ngUYen vAn a "
student_code = " rk-001-python "
email = " student01@gmail.com "

student_name = student_name.strip().title()
student_code = student_code.strip().upper()
email = email.strip().lower()

print(f'Họ tên: {student_name}')
print(f'Mã học viên; {student_code}')
print(f'Email: {email}')
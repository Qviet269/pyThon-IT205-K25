"""
(1) PHÂN TÍCH LỖI

- Dò luồng thực thi (Trace code):
  + Vòng lặp 1: total_budget đặt lại bằng 0 -> Nhập 5.000.000 
  -> total_budget = 0 + 5.000.000 = 5.000.000.
  + Vòng lặp 2: total_budget BỊ ĐẶT LẠI BẰNG 0 -> Nhập 4.000.000 
  -> total_budget = 0 + 4.000.000 = 4.000.000.
  + Vòng lặp 3: total_budget BỊ ĐẶT LẠI BẰNG 0 -> Nhập 6.000.000 
  -> total_budget = 0 + 6.000.000 = 6.000.000.
  Kết thúc vòng lặp, in ra giá trị cuối cùng là 6.000.000 VNĐ.

- Tại sao biến total_budget không cộng dồn:
  Do biến total_budget bị khai báo và gán bằng 0 nằm BÊN TRONG vòng lặp `for`. 
  Mỗi khi vòng lặp chuyển sang nhân viên tiếp theo, 
  biến này lập tức bị "reset" về 0, làm mất sạch dữ liệu của những người đã nhập trước đó.

- Lỗi logic kinh điển:
  Đặt biến tích lũy (cộng dồn) sai vị trí phạm vi (Scope). 
  Biến dùng để tích lũy giá trị qua từng vòng lặp bắt buộc phải được khởi tạo bên NGOÀI vòng lặp.
"""

# (2) SỬA LỖI

print("--- PHẦN MỀM TÍNH TỔNG QUỸ LƯƠNG ---")

# ĐÃ FIX: Đưa biến khởi tạo tổng tiền ra NGOÀI vòng lặp để giữ lại giá trị cộng dồn
total_budget = 0

# Vòng lặp chạy 3 lần để nhập lương cho 3 nhân viên
for employee_number in range(1, 4):
    print(f"Đang xử lý nhân viên số {employee_number}")
    
    # Nhập mức lương của từng người
    salary = int(input("Nhập mức lương (VNĐ): "))
    
    # Thực hiện thao tác cộng dồn liên tục vào chiếc hộp tổng
    total_budget = total_budget + salary

# Sau khi nhập xong toàn bộ mới in tổng tiền ra màn hình
print("-> KẾT QUẢ: TỔNG NGÂN SÁCH CẦN CHUẨN BỊ LÀ:", total_budget, "VNĐ")
"""
(1) PHÂN TÍCH & ĐỀ XUẤT GIẢI PHÁP

- Phân tích Input/Output:
  + Input: Số lượng nhân sự mới nhập từ bàn phím (Kiểu dữ liệu mong đợi: Số nguyên - int).
  + Xử lý bẫy: Cần bọc lệnh ép kiểu bằng try-except để tránh crash chương trình khi nhập chữ hoặc ký tự đặc biệt.
  + Output: Cảnh báo lỗi bắt nhập lại nếu số vừa nhập <= 0 HOẶC Câu thông báo "Ghi nhận thành công" khi số nhập vào hợp lệ (> 0).

- Đề xuất 2 giải pháp để tạo vòng lặp bắt nhập lại (Validation Loop):
  + Giải pháp 1: Sử dụng vòng lặp `while True` kết hợp lệnh ngắt cấu trúc `break`.
  + Giải pháp 2: Sử dụng vòng lặp `while` kết hợp với một biến cờ hiệu (Flag variable, ví dụ: valid = False).

- Bảng so sánh hai giải pháp:
  -------------------------------------------------------------------------------------------------------
  | Tiêu chí                                | Giải pháp 1 (while True + break) | Giải pháp 2 (Dùng biến cờ hiệu) |
  -------------------------------------------------------------------------------------------------------
  | Độ ngắn gọn của code                    | Cao (Ít tốn dòng code, gọn)      | Thấp (Phải khai báo biến phụ)   |
  | Mức độ dễ hiểu đối với người đọc        | Rất dễ hiểu (Gần gũi tự nhiên)   | Khó hơn (Phải theo dõi biến cờ) |
  -------------------------------------------------------------------------------------------------------

- Chốt lựa chọn:
  + Quyết định: Chọn Giải pháp 1 (while True + break).
  + Lý do: Giải pháp này mô tả chính xác tư duy logic tự nhiên: "Cứ bắt lặp vô hạn (True) để hỏi, 
  cho đến khi nào dữ liệu nhập vào đạt chuẩn thì đập vỡ vòng lặp (break) để đi tiếp". 
  Code viết ra tối giản, mạch lạc và cực kỳ phổ biến trong Python.
"""

while True:

        # Nhập dữ liệu đầu vào 
        quantity = int(input("Vui lòng nhập số lượng nhân sự mới trong tháng này: "))
        
        # Kiểm tra điều kiện lỗi: Số âm hoặc bằng 0
        if quantity <= 0:
            print("[LỖI] Số lượng không hợp lệ! Vui lòng nhập một con số lớn hơn 0.\n")
            continue  # Quay lại đầu vòng lặp để yêu cầu nhập lại
            
        # Điều kiện đúng: Số dương > 0
        print(f"[THÀNH CÔNG] Đã ghi nhận yêu cầu cấp phát tài sản cho {quantity} nhân sự mới!")
        break  # Dừng vòng lặp và thoát ra ngoài
        
print("---- CHƯƠNG TRÌNH KẾT THÚC ----");
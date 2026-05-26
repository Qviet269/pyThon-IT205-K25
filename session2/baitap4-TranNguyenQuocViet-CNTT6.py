

"""
(1) PHÂN TÍCH & ĐỀ XUẤT GIẢI PHÁP

- Phân tích Input/Output:
  + Input: Các biến age, bp, sugar (Kiểu dữ liệu: Số nguyên - int).
  + Output: Chuỗi văn bản thông báo kết quả (Đủ điều kiện / Từ chối / Lỗi dữ liệu).

- Đề xuất 2 giải pháp:
  + Giải pháp 1: Gộp điều kiện (Flat Logic).
  + Giải pháp 2: Điều kiện lồng nhau (Nested If).

- Bảng so sánh hai giải pháp:
  -------------------------------------------------------------------------------------------------------
  | Tiêu chí                                | Giải pháp 1 (Flat Logic)   | Giải pháp 2 (Nested If)      |
  -------------------------------------------------------------------------------------------------------
  | Độ ngắn gọn của code                    | Cao (Code ngắn gọn)        | Thấp (Tốn nhiều dòng code)   |
  | Độ phức tạp khi đọc code (thụt lề)      | Thấp (Không thụt lề nhiều) | Cao (Thụt lề lồng nhiều tầng)|
  | Trải nghiệm người dùng & Giá trị y khoa | Kém (Báo lỗi chung chung)  | Tốt (Báo lỗi chi tiết)       |
  -------------------------------------------------------------------------------------------------------

- Chốt lựa chọn:
  + Quyết định: Chọn Giải pháp 2 (Điều kiện lồng nhau).
  + Lý do và trade-off: Trong hệ thống y khoa, việc cung cấp nguyên nhân từ chối chính xác là bắt buộc để bác sĩ có hướng xử lý. 
  Chấp nhận đánh đổi (trade-off) cấu trúc code phức tạp và dài hơn để mang lại thông báo lỗi chi tiết, nâng cao giá trị y khoa thực tế.
"""

# triển khai code
age = int(input('Nhập tuổi bênh nhân: '));
bp = int(input('Nhập huyết áp tâm thu: '));
sugar = int(input('Nhập đường huyết: '));

if age < 0 or bp < 0 or sugar < 0:
    print('Dữ liệu nhập vào không hợp lệ');
else:
    if age < 75:
        if 90 >= bp <= 140:
            if sugar < 150:
                print('Đủ điều kiện phẫu thuật');
            
            else:print('từ chối phẫu thuật vì đường huyết vượt mức yêu cầu')
        else:print('từ chối phẫu thuật vì huyết áp quá mức phi lý');
    else: print('từ chối phẫu thuật vì quá tuổi');
        

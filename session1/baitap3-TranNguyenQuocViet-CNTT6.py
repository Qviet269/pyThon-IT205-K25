"""
* Phân tích Input/Output:
  - Input: Cần lấy 3 thông tin (Họ tên, Mã bệnh án, Khoa/Phòng). 
  Tất cả đều là văn bản bình thường nên kiểu dữ liệu là chuỗi (String). Không cần ép kiểu.
  - Output: In ra màn hình 1 dòng văn bản duy nhất chứa cả 3 thông tin trên theo đúng định dạng yêu cầu.

* Đề xuất giải pháp:
  - Dùng hàm `input()` để hiển thị thông báo và thu thập dữ liệu người dùng gõ vào.
  - Dùng hàm `print()` kết hợp tuyệt chiêu `f-string` (mà đệ vừa chỉ ca) 
  để chèn thẳng các biến vào chuỗi đầu ra một cách ngắn gọn, không cần dùng dấu cộng (+) để nối chuỗi lằng nhằng.

* Thiết kế thuật toán (Mã giả - Pseudocode):
  Bước 1: Khai báo biến `ho_ten` và gán bằng giá trị người dùng nhập từ bàn phím.
  Bước 2: Khai báo biến `ma_ba` và gán bằng giá trị người dùng nhập.
  Bước 3: Khai báo biến `khoa_phong` và gán bằng giá trị người dùng nhập.
  Bước 4: Dùng lệnh print f-string in ra màn hình cấu trúc: 
    Bệnh nhân: {ho_ten} - Mã BA: {ma_ba} - Chuyển tới: {khoa_phong}
"""

name_patient = input('Nhập họ và tên bệnh nhân: ');
id_medical = input('Nhập mã bệnh án: ');
clinic = input('Nhập khoa/phòng khám chỉ định: ');

print('\n------Phiếu khám bênh điện tử-----');
print(f'Bệnh Nhân: {name_patient} - Mã BA: {id_medical} - Chuyển tới: {clinic}');
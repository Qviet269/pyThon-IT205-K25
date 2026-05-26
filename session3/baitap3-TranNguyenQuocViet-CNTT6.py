
"""
(1) PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP

- Phân tích Input/Output:
  + Input: 
     staff_id (Mã nhân viên): Kiểu chuỗi (String).
     fullname_staff (Họ và tên): Kiểu chuỗi (String).
     department (Phòng ban): Kiểu chuỗi (String).
  + Output: Cảnh báo lỗi dừng tạo hồ sơ HOẶC Phiếu Hồ sơ Điện tử in ra màn hình.

- Đề xuất giải pháp:
  Sử dụng vòng lặp `for` với `range(1, 4)` để lặp chính xác 3 lần cho 3 nhân sự. 
  Trong mỗi lượt lặp, dùng hàm `.
  strip()` để làm sạch khoảng trắng thừa ở hai đầu dữ liệu nhập vào của Mã nhân viên và Họ tên.
    Dùng cấu trúc điều kiện `if-else` phối hợp với toán tử `or` để kiểm tra: nếu một trong hai trường này bị rỗng (`""`), hệ thống lập tức báo lỗi và dùng lệnh `continue` để bỏ qua lượt này, chuyển ngay sang người kế tiếp.

- Mô tả luồng chương trình (Thuật toán):
  Bắt đầu vòng lặp (1 đến 3) -> Nhập Mã, Tên, Phòng ban -> Làm sạch khoảng trắng bằng .
  strip() -> Kiểm tra: Nếu (Mã rỗng) HOẶC (Tên rỗng) -> Đúng: In cảnh báo lỗi -> Gọi lệnh `continue` 
  để nhảy sang lượt lặp tiếp theo -> Sai: In Phiếu Hồ sơ Điện tử thành công -> Kết thúc 3 lượt: In thông báo hoàn thành.
"""

for staff_number in range(1,4):
    print(f'Nhân viên thứ {staff_number}');

    staff_id = input('nhập mã nhân viên: ');
    fullname_staff = input('Nhập tên nhân viên: ');
    department = input('Nhập phòng ban công tác: ');

    

    if staff_id == "" or fullname_staff == "":
        print('[Cảnh báo] dữ liệu tên hoặc mã không hợp lệ! hủy bỏ tạo hồ sơ cho nhân viên này.');
        continue;

    print('\n-----------------------------');
    print('    Phiếu Hồ sơ điện tử      ');
    print('-----------------------------');
    print(f' Mã Nhân viên: {staff_id}');
    print(f' Tên Nhân viên: {fullname_staff}');
    print(f' Phòng công tác: {department}');
    print('-----------------------------');

print("\n[HỆ THỐNG] Đã hoàn tất quá trình duyệt và lập hồ sơ cho 3 nhân viên!")
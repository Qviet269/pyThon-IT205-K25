"""
(1) PHÂN TÍCH LỖI

- Dò luồng thực thi (Trace code):
  + Vòng lặp 1 (Nhân viên 1): total_budget đặt lại bằng 0 -> Nhập 5.000.000 -> total_budget = 0 + 5.000.000 = 5.000.000.
  + Vòng lặp 2 (Nhân viên 2): total_budget BỊ ĐẶT LẠI BẰNG 0 -> Nhập 4.000.000 -> total_budget = 0 + 4.000.000 = 4.000.000.
  + Vòng lặp 3 (Nhân viên 3): total_budget BỊ ĐẶT LẠI BẰNG 0 -> Nhập 6.000.000 -> total_budget = 0 + 6.000.000 = 6.000.000.
  Kết thúc vòng lặp, in ra giá trị cuối cùng là 6.000.000 VNĐ.

- Tại sao biến total_budget không cộng dồn:
  Do biến total_budget bị khai báo và gán bằng 0 nằm BÊN TRONG vòng lặp `for`. Mỗi khi vòng lặp chuyển sang nhân viên tiếp theo, biến này lập tức bị "reset" về 0, làm mất sạch dữ liệu của những người đã nhập trước đó.

- Lỗi logic kinh điển:
  Đặt biến tích lũy (cộng dồn) sai vị trí phạm vi (Scope). Biến dùng để tích lũy giá trị qua từng vòng lặp bắt buộc phải được khởi tạo bên NGOÀI vòng lặp.
"""

print('--- Hệ Thống gửi email thưởng tết ---');

for employee_number in range(1,4):
    print(f'--- Đang xử lý nhân viên số {employee_number} ---');

    working_day =int(input('Nhập số ngày ông trong tháng: '));


    if working_day == 0:
        print('Cảnh Báo: Nhân viên nghỉ cả tháng. Không xét thưởng.');
        continue;

    bonus_amount = working_day * 2000000;
    print(f'-> Đã gửi email: chúc mừng nhận được {bonus_amount} VND tiền thưởng!');
    print('------------------------------\n');
    print('Đã hoàn tất quá trình duyệt thưởng cho 3 nhan viên !');
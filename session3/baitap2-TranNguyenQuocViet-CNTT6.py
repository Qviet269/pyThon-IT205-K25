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
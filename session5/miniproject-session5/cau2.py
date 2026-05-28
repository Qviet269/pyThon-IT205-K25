total_error = 0;

flag = True;

while True:

    user = int(input('Nhập số lượng hàng lỗi ngày của từng quầy: '));

    if user == -1:
        break;
    if user != -1:
        total_error += user
print(f'Tổng số hàng lỗi thu hồi trong ngày là {total_error}');

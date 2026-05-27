total_money = int(input('Nhập tổng số tiền ban đầu: '));

if total_money > 5000000:
    small = total_money * 0.1;
    bull = total_money * 0.9;

    print('\n ----- Hóa đơn thanh toán rikkei store ---');
    print(f'Số tiền được giảm giá: {small}');
    print(f'Tổng số tiền khách hàng phải trả: {bull}')
else:
    bull = total_money;



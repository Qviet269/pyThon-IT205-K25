# code đã sửa


total_money = int(input('Nhập tổng số tiền ban đầu: '))

if total_money >= 500000:
    small = total_money * 0.1
    bull = total_money * 0.9

    print('\n----- Hóa đơn thanh toán Rikkei Store ---')
    print(f'Số tiền được giảm giá: {small:,.0f} VND')
    print(f'Tổng số tiền khách hàng phải trả: {bull:,.0f} VND')
else:
    bull = total_money
    
    print('\n----- Hóa đơn thanh toán Rikkei Store ---')
    print('Đơn hàng không đủ điều kiện áp dụng mức giảm giá.')
    print(f'Tổng số tiền khách hàng phải trả: {bull:,.0f} VND')



#code đã sửa

count = 0
total = 0

for i in range(1, 8):
    # Lấy dữ liệu người dùng nhập và lưu vào biến doanh_thu
    doanh_thu = int(input(f'Nhập doanh thu ngày {i}: '))
    
    # Cộng dồn số tiền doanh_thu vào tổng
    total += doanh_thu

    # Kiểm tra điều kiện dựa trên số tiền doanh_thu thực tế
    if doanh_thu >= 5000000:
        count += 1

result = total / 7

print ('\n--- Báo cáo doanh thu tuần Rekkei Store ---')
print (f'Tổng doanh thu cả tuần: {total:,.0f} VND')
print (f'Doanh thu trung bình mỗi ngày: {result:,.0f} VND')
print (f'Số ngày đạt tiêu thụ mục tiêu (>= 5,000,000 VND): {count} ngày')

count = 0;
total = 0;
for i in range(1, 8):
    print(f'Nhập doanh thu ngày {i}: ');
    total += i;

    if i >= 5000000:
        count += 1;

result = total / 7;

print ('--- Báo cáo doanh thu tuần rekkei store ---');
print (f'Tổng doanh thu cả tuần: {total} VND');
print (f'Doanh thu trung bình mỗi ngày: {result:.2f} VNĐ');
print (f'Số ngày đạt tiêu thu mục tiêu (>=5000000 VND): {count} ngày');

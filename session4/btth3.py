n = int(input('Nhập số lượng: '));

max = None;
min = None;

for i in range(1, n + 1):
    value = int(input(f'Nhập giá trị hóa đơn thứ {i}: '));

    if max is None and min is None:
        max = value;
        min = value;
    else:
        if value > max:
            max = value;
        
        if value < min:
            min = value;

if n > 0:
    print('--- Kết quá kiểm toán rikkei sotre ---');
    print(f'Hóa đơn có giá trị cao nhất: {max} VND');
    print(f'Hóa đơn có giá trị cao nhất: {min} VND');
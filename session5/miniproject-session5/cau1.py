input_quantity = int(input('Nhập số lượng tồn kho: '));

if input_quantity >= 50:
    print('Tình trang: Hàng đầy kho');
elif input_quantity >= 10 and input_quantity < 50:
    print('Tình trang: Mức an toàn ');
else:
    print('Tình trạng: Sắp hết hàng, cần báo cáo nhập thêm');
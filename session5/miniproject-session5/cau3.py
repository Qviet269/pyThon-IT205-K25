inventory = 100;

while True:

    player = int(input('Nhập số lượng muốn xuất: '));
    
    if player < 0:
        print("Báo lỗi: Không được nhập số âm, vui lòng nhập lại!");

    if player > inventory: 
        print('Kho không đủ hàng, vui lòng nhập lại');
    
    if player > 0 and player <= 100:
        value = inventory - player;
        print('=> Xuất kho thành công!');
        print(f'Tồn kho còn lại: {value}');
        break;

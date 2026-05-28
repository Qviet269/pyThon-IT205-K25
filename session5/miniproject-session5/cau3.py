inventory = 100;

while True:

    player = int(input('Nhập số lượng muốn xuất: '));
    
    if player < 0:
        print("Báo lỗi: Không được nhập số âm, vui lòng nhập lại!");

    elif player > inventory: 
        print('Kho không đủ hàng, vui lòng nhập lại');
    
    else:
        value = inventory - player;
        print('=> Xuất kho thành công!');
        print(f'Tồn kho còn lại: {value}');
        break;

MAX_CHANGE = 5
SECRET_NUMBER = 27


for i in range(1, MAX_CHANGE + 1):
    choice_turn = int(input(f'Lớn đoán {i} - Nhập số của bạn: '));
    
    if choice_turn == SECRET_NUMBER:
        print( '=> Chúc mừng! bạn đã đoán chính xác mã số may mắn');
    elif choice_turn < SECRET_NUMBER:
        print( '=> Gợi ý: Số của bạn nhỏ hơn mã số may mắn!');
    else: print( '=> Gợi ý: Số của bạn lớn hơn mã số may mắn!');

    if i >= MAX_CHANGE:
        print('Đã hết lượt đoán!');


print('---- Trò chơi kết thúc ----');


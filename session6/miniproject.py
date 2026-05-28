laptop = 0;
phone = 0;
tablet = 0;

while True:
    
    print("----MENU-----");
    print('1.Xem báo cáo tồn kho.');
    print('2.Nhập kho.');
    print('3.Xuất kho.');
    print('4.Cảnh báo hàng tồn kho.');
    print('5.Thoát chương trình.');

    choice = int(input('Nhập lựa chọn: '));

    if choice == 1:
        print('\n---- Báo cáo tồn kho ----');
        print(f'số lượng hiện tại LapTop {laptop}');
        print(f'Laptop {laptop}: ', end = "");
        for i in range(laptop):
            print('*', end = '');
        print();

        print(f'số lượng hiện tại phone {phone}');
        print(f'phone {phone}: ', end = "");
        for i in range(phone):
            print('*', end = '');
        print();

        print(f'số lượng hiện tại tablet {tablet}');
        print(f'tablet {tablet}: ', end = "");
        for i in range(tablet):
            print('*', end = '');
        print();
        

    elif choice == 2:
        print('\n---- Nhập kho -----');
        print('1.laptop, 2.phone, 3.table');
        mini_choice = int("Hãy chọn 1 trong 3 mặt bằng số (1_3): ");

        if mini_choice == 1:
            laptop += mini_choice; 
        elif mini_choice == 2:
            phone += mini_choice; 
        elif mini_choice == 3:
            
        

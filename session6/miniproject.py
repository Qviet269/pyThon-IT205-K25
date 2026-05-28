laptop = 0;
phone = 0;
table = 0;

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

        print(f'số lượng hiện tại tablet {table}');
        print(f'tablet {table}: ', end = "");
        for i in range(table):
            print('*', end = '');
        print();
        

    elif choice == 2:
        print('\n---- Nhập kho -----');
        print('1.laptop, 2.phone, 3.table');
        mini_choice = int(input("Hãy chọn 1 trong 3 mặt hàng bằng số (1_3): "));

        if mini_choice in [1, 2, 3]:

            while True:
                quantity = int(input('Nhập số lượng muốn thêm: '));
                if quantity < 0:
                    print("Số lượng không hợp lệ, vui lòng nhập lại!");
                else:
                    break;
            
            if mini_choice == 1:
                laptop += quantity; 
            elif mini_choice == 2:
                phone += quantity; 
            elif mini_choice == 3:
                table += quantity; 
            print('Thêm thành công!');
        else:
            print('Mặt hàng muốn thêm không có')

    elif choice == 3:
        print('\n---- Xuất kho -----');
        print('1.laptop, 2.phone, 3.table');
        mini_choice = int(input("Hãy chọn 1 trong 3 mặt hàng bằng số (1_3): "));

        if mini_choice in [1, 2, 3]:

            while True:
                quantity = int(input('Nhập số lượng muốn xuất: '));
                if quantity < 0:
                    print("Số lượng không hợp lệ, vui lòng nhập lại!");
                else:
                    break;
            
            if mini_choice == 1:
                if quantity > laptop:
                    print('không đủ hàng');
                else:
                    laptop -= quantity;
                    print('Xuất thành công!');
            
            elif mini_choice == 2:
                if quantity > phone:
                    print('không đủ hàng');
                else:
                    phone -= quantity;
                    print('Xuất thành công!');
            
            elif mini_choice == 3:
                if quantity > table:
                    print('không đủ hàng');
                else:
                    table -= quantity;
                    print('Xuất thành công!');
        else:
            print('Mặt hàng muốn xuất không có')

    elif choice == 4:
        print("----Cảnh báo hàng tồn kho thấp ---");
        if laptop < 10:
            print(f'Cảnh báo! mặt hàng laptop sắp hết (Chỉ còn {laptop} sản phẩm)');
        if phone < 10:
            print(f'Cảnh báo! mặt hàng phone sắp hết (Chỉ còn {phone} sản phẩm)');
        if table < 10:
            print(f'Cảnh báo! mặt hàng table sắp hết (Chỉ còn {table} sản phẩm)');

    elif choice == 5:
        print('Đã thoát')
        break;

    else:
        print('Lựa chọn không hợp lệ');
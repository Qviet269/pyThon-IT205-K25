cart_items = [
    ["P001", "Dien thoai 15", 1, 25000000],
    ["P002", "Op lung Silicon", 2, 150000]
]

while True:
    print("""
======================================================
        SHOPEE CART MANAGEMENT SYSTEM
======================================================
    1. Xem chi tiết giỏ hàng và tính tổng tiền
    2. Thêm sản phẩm mới / Cộng dồn số lượng
    3. Cập nhật số lượng của một sản phẩm
    4. Xóa sản phẩm khỏi giỏ hàng 
    5. Thoát chương trinh
======================================================
""")
    choice = input('Mời bạn chọn chức năng (1-5): ')
    match choice:
        case "1":
 
            print('--- CHI TIẾT GIỎ HÀNG ---')
            print('STT | mÃ SP | Tên Sản phẩm              | SL | Đơn Giá       | Thành tiền')
            print ('----------------------------------------------------------------------------')

            for i, v in enumerate( cart_items, 0):
                print(f"{i+1} | {cart_items[i][0]} | {cart_items[i][1]}              | {cart_items[i][2]} | {cart_items[i][3]}đ        | {cart_items[i][3] * cart_items[i][2]}đ")
            print ('----------------------------------------------------------------------------')

        case "2":
            pro_id = input('Mã sản phẩm mới: ')
            pro_name = input('Tên sản phẩm mới : ')
            pro_quantity = int(input('Số lượng: '))
            pro_price = int(input('Nhập đơn giá; '))
            flag = False
            for i in range(len(cart_items)):
                if cart_items[i][0] == pro_id:
                    print('Mã sản phẩm này đã tồn tại, cập nhật lại!')
                    cart_items[i][2] += pro_quantity
                    flag = True
                    break
            if flag:
                cart_items.append([pro_id, pro_name, pro_quantity, pro_price])

            
        case "3":
            new_pro_id = input('Mã sản phẩm mới: ')
            new_pro_quantity = int(input('Số lượng: '))
            flag = False

            for i in range(len(cart_items)):
                if cart_items[i][0] == new_pro_id:
                    cart_items[i][2] += new_pro_quantity
                    print('Đã cập nhật!')
                    flag = True
                    break
            if flag:
                print('Không tìm thấy!')

        case '4':
            print()
        case "5":
            print('Thoát chương trình')
            break
        case _:
            print('Lựa chọn không hợp lệ')
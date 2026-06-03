cart_items = [
        ["P001", "Dien thoai iPhone 15", 1, 25000000],
        ["P002", "Op lung Silicon", 2, 150000]
]


while True:
    print("Shopee cart management system")
    print("""1. Xem chi tiết giỏ hàng & Tính tổng tiền
2. Thêm sản phẩm mới % Cộng dồn số lượng
3. Cập nhật số lượng của 1 sản phẩm
4. Xóa sản phẩm khỏi giỏi hàng
5. Thoát chương trình
        """)
    choice = input("Nhập vào lựa chọn của bạn: ")
    match choice:
        case "1":
            print("-Chi tiết giỏ hàng-")
            print("STT | Mã SP | Tên sản phẩm           | SL | Đơn giá          | Thành tiền        |")
            print("----------------------------------------------------------------------------------")
            
            for index, value in enumerate(cart_items, start=0):
                print(f"{index + 1} | {cart_items[index][0]} | {cart_items[index][1]} | {cart_items[index][2]} | {cart_items[index][3]}| {cart_items[index][2] * cart_items[index][3]}|")
        case "2":
            product_id = input("Mã sản phẩm: ")
            product_name = input("Tên sản phẩm: ")
            product_quantity = int(input("Nhập số lượng: "))
            product_price = float(input("Nhập đơn giá: "))
            flag = False
            for i in range(len(cart_items)):
                if (cart_items[i][0] ==  product_id):
                    print("Mã sản phẩm này đã tồn tại, tiến hành cập nhật!")
                    cart_items[i][2] += product_quantity
                    flag = True
                    break
            if (flag == False):
                cart_items.append([product_id, product_name, product_quantity, product_price])
        case "3":
            new_product_id = input("Mã sản phẩm mới: ")
            new_product_quantity = int(input("Nhập số lượng: "))
            flag = False
            for i in range(len(cart_items)):
                if (cart_items[i][0] ==  new_product_id):
                    cart_items[i][2] = new_product_quantity
                    print("Đã cập nhật!")
                    flag = True
                    break
            if (flag == False):
                print("Không tìm thấy !")
        case "4":
            delete_id = input("Nhập vào mã sản phẩm muốn xóa: ")
            flag = False
            for i in range(len(cart_items)):
                if(cart_items[i][0] == delete_id):
                    cart_items.pop(i)
                    print("Xóa sản phẩm thành công!")
                    flag = True
                    break
            if(flag == False):
                print("Không tìm thấy sản phẩm!")

        case "5":
            print("Thoát chương trình!")
            break
        case _:
            print("Lựa chọn không hợp lệ!")
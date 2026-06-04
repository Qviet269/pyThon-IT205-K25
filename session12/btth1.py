cart_items = [
        {
        "id": "P001", 
        "name": "Dien thoai iPhone 15",
        "number": 1,
        "price": 25000000
        },
        {
        "id": "P002",
        "name": "Op lung Silicon", 
        "number": 2, 
        "price": 150000
        }
]
while True:
    print("""
====================================================
        SHOPEE CART MANAGEMENT SYSTEM
====================================================
    1. Xem chi tiết giỏ hàng & tính tổng tiền
    2. Thêm sản phẩm mới / Cộng dồn số lượng
    3. Cập nhật số lượng của một sản phẩm
    4. Xóa sản phẩm khỏi giỏ hàng
    5. Thoát chương trình
""")
    choice = input("Mời bạn chọn chức năng (1-5): ")

    match choice:
        case "1":
            total_SL = 0
            total_price = 0

            print("----Chi tiết giỏ hàng ----")
            print(f"{'STT':^5}|{'Mã SP':^10}|{'Tên Sẩn phẩm':^25}|{'SL':^5}|{'Đơn giá':^15}|{'Thành tiền':^15}")
            print("-----------------------------------------------------------------------------------")
            for i, v in enumerate(cart_items,1):
                print(f"{i:^5}|{v["id"]:^10}|{v["name"]:^25}|{v["number"]:^5}|{v["price"]:^15}|{(v["price"]*v["number"]):^15}")
                total_SL += v["number"]
                total_price += (v["price"]*v["number"])
            print("-----------------------------------------------------------------------------------")
            print(f"=> Tổng số lượng sản phẩm trong gió: {total_SL}")
            print(f"=> Tổng tiền thanh toán: {total_price}")
        case "2":
            
            new_id = input('Nhập mã sản phẩm mới: ').strip()
            new_name = input('Nhập tên sản phẩm mới : ')
            while True:
                new_number = input('Nhập số lượng mới: ')
                if new_number.isdigit():
                    new_number = int(new_number)
                    break
                else:
                    print("Bạn nhập không hợp lệ")
            
            new_price = input('Nhập đơn giá mới: ')
            found = False
            for i, v in enumerate(cart_items):
                if new_id == v.get('id'):
                    found = True
                    v['number'] += new_number
                    break
            if found == False:
                new_product = {
                    'id': new_id,
                    'name': new_name,
                    'number': new_number,
                    'price': int(new_price)
                }
                cart_items.append(new_product)
                print('Đã them thành công!')
        case "3":
            update_id = input('Nhập mã sản phẩm mới: ').strip()
            while True:
                update_number = input('Nhập số lượng mới: ')
                if update_number.isdigit():
                    update_number = int(update_number)
                    break
                else:
                    print("Bạn nhập không hợp lệ")

            found = False
            for i, v in enumerate(cart_items):
                if update_id == v.get('id'):
                    found = True
                    v['number'] += update_number
                    break
            if found == False:
                print("Không tồn tại")
        case "4":
            del_product_id = input("Nhập mã muốn xóa")
            found = False
            for i, v in enumerate(cart_items):
                if del_product_id == v["id"]:
                    found = True
                    del cart_items[i]
                    print("Đã xóa")
                    break
            if found == False:
                print('Không tìm thấy')
        case "5":
            print("Thoát chương trình!")
            break
        case _:
            print("Lựa chọn không hợp lệ!")
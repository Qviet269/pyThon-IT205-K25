def menu():
    print("""
================ List Bill ======================
    1. Hiển thị sanh sách hóa đơn
    2. Lập hóa đơn mới tại quần
    3. Cập nhật thông tin hóa đơn
    4. Hủy hóa đơn lỗi
    5. Tìm kiếm hóa đơn
    6. Tổng kê phân loại doanh thu
    7. Phân loại hóa đơn tự động
    8. Thoát chương trình
=================================================
""")

def show_bill (bill_list):
    if not bill_list:
        print("Danh sách hóa đơn rỗng!")
        return
    print(f"{'Mã đơn':<10}| {'Tên sản phẩm':<25}| {'Đơn giá':<15}| {'Số lượng':<10}| {'giảm giá':<15}| {'Tổng tiền':<15}| {'Phân loại':<10}")
    for i, v in enumerate(bill_list):
        print(f"{v.get("Bill_id"):<10}| {v.get("name_product"):<25}| {v.get("price_product"):<15}| {v.get("quantity"):<10}| {v.get("number_money"):<15}| {v.get("total_money"):<15}| {v.get("classify"):<10}")
    return

def validate_input(prompt: str, type_input: str = "str"):
    while True:
        user_input = input(prompt)
        if not user_input:
            print("dữ liệu không được để trống!")
            continue

        if type_input == "int":
            try:
                value = int(user_input)
                if value < 0:
                    print("Dữ liệu phải lớn hơn 0 hoặc bằng 0")
                    continue
                return value
            except:
                print("Dữ liệu không hợp lệ!")
                continue

        if type_input == "quan":
            try:
                value = int(user_input)
                if value <= 0:
                    print("Số lượng sản phẩm phải là số nguyên lơn hơn 0 (tổi thiếu là 1)")
                    continue
                return value
            except:
                print("Dữ liệu không hợp lệ!")
                continue

        return user_input
    
def add_bill (bill_list):
    if not bill_list:
        print("Danh sách hóa đơn rỗng!")
        return
    
    while True:
        input_id = validate_input("Nhập mã bill hàng muốn thêm: ")
        for i, v in enumerate(bill_list):
            if input_id.upper() == v.get("Bill_id").upper():
                print("Mã đơn đã tồn tại!, vui lòng nhập lại")
                break
        else:
            break
    input_name = validate_input("Nhập tên sản phẩm: ")
    price_product = validate_input("Nhập đơn giá sản phẩm mới: ", "int")
    quantity = validate_input("Nhập số lượng sản phẩm mới: ", "quan")
    total = price_product * quantity
    while True:
        number_money = validate_input("Nhập Số tiền giảm giá: ", "int")
        if number_money > total:
            print("Không được vượt quá giá trị trước thuế sản phẩm")
            continue
        break

    total_money = (total - number_money) * 1.1

    classify = classify_bill (total_money)

    new_bill = {
        "Bill_id": input_id,
        "name_product": input_name,
        "price_product": price_product,
        "quantity": quantity,
        "number_money": number_money,
        "total_money": total_money,
        "classify": classify
    }
    bill_list.append(new_bill)
    print("Bạn đã thêm thành công!")
    return

def classify_bill (total_money):

    if total_money < 1000000:
        return "Nhỏ"
    elif 1000000 < total_money < 5000000:
        return "VỪa"
    elif 5000000 < total_money < 15000000:
        return "Lớn"
    else:
        return "Cao cấp"
    
def update_bill (bill_list):
    if not bill_list:
        print("Danh sách hóa đơn rỗng!")
        return
    
    input_id = validate_input("Nhập mã đơn cần cập nhật: ")
    for i, v in enumerate(bill_list):
        if input_id.upper() == v.get("Bill_id").upper():
            print(f"Bạn đã tìm thấy vui mã {input_id} hãy cập nhật lại thông tin")
            v["price_product"] = validate_input("Nhập đơn giá: ", "int")
            v["quantity"] = validate_input("Nhập số lượng: ", "quan")
            total = v["price_product"] * v["quantity"]
            while True:
                v["number_money"] = validate_input("Nhập Số tiền giảm giá: ", "int")
                if v["number_money"] > total:
                    print("Không được vượt quá giá trị trước thuế sản phẩm")
                    continue          
                break
            v["total_money"] = (total - v["number_money"]) * 1.1
            v["classify"] = classify_bill (v.get("total_money"))
            return
    else:
        print("Không tìm thấy mã đơn!")
        return
def delete_bill (bill_list):
    if not bill_list:
        print("Danh sách hóa đơn rỗng!")
        return
    
    input_id = validate_input("Nhập mã đơn cần hủy: ")
    for i, v in enumerate(bill_list):
        if input_id.upper() == v.get("Bill_id"):
            print("Bạn có chắc chắn muốn hủy và xóa đơn hàng này không? (Y/N)")
            mini_choice = validate_input("")
            if mini_choice.upper() == "Y":
                bill_list.pop(i)
                print("Bạn đã xóa thành công!")
                return
            else:
                print("Bạn đã thoát thành công!")
                return
    else:
        print("Không tìm thấy mã đơn!")
        return
    
def search_bill (bill_list):
    if not bill_list:
        print("Danh sách hóa đơn rỗng!")
        return
    
    search = validate_input("Nhập mã đơn hoặc tên sản phẩm cần tìm: ")
    flag = False
    for i, v in enumerate(bill_list):
        if search.upper() == v.get("Bill_id").upper() or search.title() in v.get("name_product").title():
            flag = True
            print("bạn đã tìm thành công !")
            print(f"{v.get("Bill_id"):<10}| {v.get("name_product"):<25}| {v.get("price_product"):<15}| {v.get("quantity"):<10}| {v.get("number_money"):<15}| {v.get("total_money"):<15}| {v.get("classify"):<10}")
    if not flag:
        print("Không tìm thấy mã đơn!")
        return
    
def statistical_bill (bill_list):
    if not bill_list:
        print("Danh sách hóa đơn rỗng!")
        return
    
    classify_big = 0
    classify_small = 0
    classify_fit = 0
    classify_vip = 0

    for i, v in enumerate(bill_list):
        if v.get("classify") == "Lớn":
            classify_big += 1
        elif v.get("classify") == "Nhỏ":
            classify_small += 1
        elif v.get("classify") == "Vừa":  
            classify_fit += 1
        else:
            classify_vip += 1

    print (f"Lớn: {classify_big}")
    print (f"Nhỏ: {classify_small}")
    print (f"Vừa: {classify_fit}")
    print (f"Cao cấp: {classify_vip}")

def auto_bill_list (bill_list):
    if not bill_list:
        print("Danh sách hóa đơn rỗng!")
        return
    
    for i, v in enumerate(bill_list):
        total = v["price_product"] * v["quantity"]
        v["total_money"] = (total - v["number_money"]) * 1.1
        v["classify"] = classify_bill (v.get("total_money"))
        print ("Tự động cập nhật!")
        return
def main():
    bill_list = [
        {
            "Bill_id": "HD001",
            "name_product": "ban pham co Corsair",
            "price_product": 1800000,
            "quantity": 2,
            "number_money": 200000,
            "total_money": 3740000,
            "classify": "Lớn"
        }
    ]
    while True:
        menu()
        
        choice = input("Mời bạn nhập lựa chọn (1-8): ").strip()
        match choice:
            case "1":
                print("------ Hiển thị danh sách ------")
                show_bill (bill_list)
            case "2":
                print("----- Lập hóa đơn -----")
                add_bill (bill_list)
            case "3":
                print("-------- Cập nhật thông tin -----")
                update_bill (bill_list)
            case "4":
                print("------ Hủy đơn lỗi -------")
                delete_bill (bill_list)
            case "5":
                print("------ Tìm kiếm hóa đơn")
                search_bill (bill_list)
            case "6":
                print("-------- Thống kê ------")
                statistical_bill (bill_list)
            case "7":
                print("------- Phân loại ------")
                auto_bill_list (bill_list)
            case "8":
                print("Bạn đã thoát chương trình!")
                break
            case _:
                print("Lựa chọn không hợp lệ!")
main()
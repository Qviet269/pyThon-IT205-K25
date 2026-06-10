def menu():
    print("""
===========================================
        QUẢN LÝ KHO HÀNG - GROGERY STORE
===========================================
    1. Xem danh sách hàng tồn kho
    2. Nhập thêm hàng hóa mới
    3. Cập nhật lượng tồn kho
    4. Thoát chương trình
""")

def show_inventory (inventory):
    if not inventory:
        print("Kho hàng hiện đang trống!")
        return
    print(f"{'ID':<5}| {'Tên hàng hóa':<15}| {'Số lương tồn':<5}")
    print("-----------------------------------------------")
    for i, v in enumerate(inventory):
        print(f"{v.get("id"):<5}| {v.get("name"):<15}| {v.get("quantity"):<5}")

    print("------------------------------------------------")

def validate_input(prompt:str, type_input: str = "str"):
    while True:
        users_input = input(prompt)

        if not users_input:
            print("Dữ liệu không được trống!")
            continue

        if type_input == "int":
            try:
                value = int(users_input)
                if value < 0:
                    print("Số truyền vào khống được âm, phải là 1 số nguyên!")
                    continue
                return value
            except ValueError:
                print("Dữ liệu không hợp lệ!")
                continue
        return users_input

def add_inventory (inventory):
    if not inventory:
        print("Kho hàng hiện đang trống!")
        return
    while True:
        input_id = validate_input("Nhập ID cần thêm: ")
        for i, v in enumerate(inventory):
            if input_id.upper() == v.get("id").upper():
                print("Mã hàng đã tồn tại! vui lòng nhập lại")
                break
        else:
            break
    input_name = validate_input("Nhập tên hàng: ")
    input_quantity = validate_input("Nhập số lượng: ", "int")

    new = {
        'id': input_id, 'name': input_name, 'quantity': input_quantity
    }

    inventory.append(new)
    print("Thêm hàng hóa vào kho thành công!")
    return

def update_inventory (inventory):
    if not inventory:
        print("Kho hàng hiện đang trống!")
        return
    input_id = validate_input("Nhập mã hàng cần cập nhật: ")
    for i, v in enumerate(inventory):
        if input_id.upper() == v.get("id").upper():
            input_quantity = validate_input("Nhập số lượng cần cập nhật: ", "int")
            v["quantity"] = input_quantity
            print("Cập nhật số lượng thành công!")
            return
    else:
        print(f"Không tìm thấy hàng hóa có mã {input_id}")
        return

def main():
    inventory = [
    {'id': 'G01', 'name': 'Gạo tẻ', 'quantity': 50},
    {'id': 'G02', 'name': 'Mì tôm', 'quantity': 120}
]

    while True:
        menu()

        choice = input("Mời bạn nhập lựa chọn (1-4): ")

        match choice:
            case "1":
                print("---- DANH SÁCH HÀNG TỒN KHO ----")
                show_inventory (inventory)
            case "2":
                print('---- NHẬP HÀNG HÓA MỚI -----')
                add_inventory (inventory)
            case "3":
                print("---- Cập nhật số lượng tồn kho ----")
                update_inventory (inventory)
            case "4":
                print("Cảm on bạn đã sử dụng phần mềm!")
                print("[Chương trình kết thúc]")
                break
            case _:
                print("Lựa chọn không hợp lệ")
main()
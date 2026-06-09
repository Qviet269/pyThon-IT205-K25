def menu():
    print("""
=================== BUS LIST ==================
    1. Hiển thị danh sách chuyển xe
    2. Khơi báo chuyển xe mới
    3. Cập nhật đặt vé
    4. Hủy chuyến xe khỏi lịch
    5. Tìm kiếm chuyến xe
    6. Thống kê trạng thái xe
    7. Phân loại trạng thái tự động
    8. Thoát chương trình
================================================
""")

def show_bus_list(bus_list):
    if not bus_list:
        print("Danh không được rỗng!")
        return
    print(f"{'Mã CX':<5}| {'Tuyến đường':<25}| {'Giá vé':<15}| {'Ghế trống':<10}| {'Tổng số ghế':<15}| {'Doanh thu hiện tại':<25}| {'Trạng thái lấp đầy':<15}")
    for i, b in enumerate(bus_list):
        print(f"{b.get('bus_id'):<5}| {b.get('route'):<25}| {b.get('price_ticket'):<15}| {b.get('empty_seats'):<10}| {b.get('total_seats'):<15}| {b.get('current_revenue'):<25}| {b.get('status'):<15}")

def get_validate_input(prompt: str, input_type: str = "str"):
        while True:
            users_input = input(prompt).strip()
            if not users_input:
                print("Dữ liệu không được để trống! vui lòng nhập lại")
                continue

            if input_type == 'int':
                try:
                    Value = int(users_input)
                    if Value <= 0:
                        print("Dữ liệu không được âm và = 0!")
                        continue
                    return Value
                except ValueError:
                    print("Dữ liệu không hợp lệ! nhập lại")
                    continue
            return users_input

def declaration_bus (bus_list):
    
    while True:
        input_id = get_validate_input("Nhập mã CX mới: ")
        for i, v in enumerate(bus_list):
            if input_id.lower() == v.get("bus_id").lower():
                print("Mã không được trùng! vui lòng nhập lại")
                break
        else:
            break
    input_route = get_validate_input("Nhập tuyến đường mới: ")
    price_input = get_validate_input("Nhập giá vé mới: ", "int")
    total_seats = get_validate_input("Nhập tổng số ghế: ", "int")

    empty_seats = total_seats
    number_of_seats = total_seats - empty_seats
    current_revenue = price_input * number_of_seats

    empty_rate  = empty_seats / total_seats

    if empty_seats  == 0:
        status = "Hết vé"
    elif empty_rate < 0.15:
        status = "Hút khách"
    elif 0.15 <= empty_rate  <= 0.8:
        status = "Bình thường"
    else:
        status = "Ế khách"

    new_bus = {
        "bus_id": input_id, 
        "route": input_route, 
        "price_ticket": price_input, 
        "empty_seats": empty_seats, 
        "total_seats": total_seats, 
        "current_revenue": current_revenue, 
        "status": status
    }

    bus_list.append(new_bus)

def update_ticket (bus_list):
    if not bus_list:
        print("Danh sách chuyến xe đang rỗng!")
        return
    
    while True:
        input_id = get_validate_input("Nhập mã CX Cần cập nhật: ")
        for i, v in enumerate(bus_list):
            if input_id.lower() == v.get("bus_id").lower():

                quantity_ticket = get_validate_input("Nhập so lượng vé đặt: ", "int")

                if quantity_ticket <= v.get("empty_seats"):
                    v["empty_seats"] -= quantity_ticket

                    number_of_seats = v.get("total_seats") - v.get("empty_seats")
                    v["current_revenue"] = v.get("price_ticket") * number_of_seats

                    classify_status(v)
                    print("Cập nhật thành công! ")
                    return
        else:
            print("Không tìm thấy mã!")
            continue

def cancel_bus(bus_list):
    if not bus_list:
        print("Danh sách chuyến xe đang rỗng!")
        return
    while True:
        input_id = get_validate_input("Nhập mã CX muốn hủy: ")
        for i, v in enumerate(bus_list):
            if input_id.upper() == v.get("bus_id").upper():
                print("Bạn có chắc chắn muốn xóa chuyển xe này khỏi lịch trình không?")
                mini_choice = get_validate_input("Y/N: ")
                if mini_choice.upper() == "Y":
                    bus_list.pop(i)
                    print("Đã xóa thành công")
                    return
                elif mini_choice.upper() == "N":
                    print("Thoát hủy thành công!")
                    return
                else:
                    print("Lựa chọn không hợp lệ!")
                    break
        else:
            print("Không tìm thấy mã")
            continue
        
def search_bus(bus_list):
    if not bus_list:
        print("Danh sách xe không được để trông!")   
        return
    while True:
        input_id = get_validate_input("Nhập mã CX hoặc tuyến đường gần: ")
    
        for i, v in enumerate(bus_list):
            if input_id.upper() == v.get("bus_id").upper() or input_id.lower() in v.get("route").lower():
                print(f"{v.get('bus_id'):<8}| "
                    f"{v.get('route'):<25}| "
                    f"{v.get('price_ticket'):<10}")
                return
        else:
            print("Không tìm thấy chuyển xe! nhập lại")
            continue

def statistical_bus(bus_list):
    if not bus_list:
        print("Danh sách xe không được để trông!")   
        return
    
    few_bus = 0
    normal_bus = 0
    attract_bus = 0
    sold_out = 0
    for i, v in enumerate(bus_list):
        if v.get("status").title() == "Hết Vé":
            sold_out += 1
        elif v.get("status").title() == "Hút Khách":
            attract_bus += 1
        elif v.get("status").title() == "Bình Thường":
            normal_bus += 1
        else:
            few_bus += 1
    print(f"Hết vé: {sold_out}")
    print(f"Hút khách: {attract_bus}")
    print(f"Bình thường: {normal_bus}")
    print(f"Ế khách: {few_bus}")

def classify_status(bus):

    empty_rate = (
        bus.get("empty_seats") / bus.get("total_seats")
    )

    if bus.get("empty_seats") == 0:
        bus["status"] = "Hết vé"

    elif empty_rate < 0.15:
        bus["status"] = "Hút khách"

    elif 0.15 <= empty_rate <= 0.8:
        bus["status"] = "Bình thường"

    else:
        bus["status"] = "Ế khách"


def refresh_status(bus_list):

    if not bus_list:
        print("Danh sách chuyến xe đang rỗng!")
        return

    for v in bus_list:
        classify_status(v)

    print("Đã phân loại trạng thái tự động!")

def main():
    bus_list = [
        {
            "bus_id": "CX001", 
            "route": "Sài Gòn - Đà Lạt", 
            "price_ticket": 30000, 
            "empty_seats": 5, 
            "total_seats": 40, 
            "current_revenue": 10500000, 
            "status": "Hút khách"}
    ]
    while True:
        menu()
        choice = input("Mời bạn nhập lựa chọn (1-8): ").strip()

        match choice:
            case "1":
                show_bus_list(bus_list)
            case "2":
                print()
                declaration_bus (bus_list)
            case "3":
                update_ticket (bus_list)
                print()
            case "4":
                cancel_bus(bus_list)
                print()
            case "5":
                search_bus(bus_list)
                print()
            case "6":
                statistical_bus(bus_list)
                print()
            case "7":
                refresh_status(bus_list)
                print()
            case "8":
                print("Bạn thoát chương trinh thành công!")
                break
            case _:
                print("Lựa chọn không hợp lệ!")
main()
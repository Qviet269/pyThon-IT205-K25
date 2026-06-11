def menu():
    print("""
============== LIST BUS ==============
    1.Hiển thị danh sách chuyển xe
    2.Khai báo chuyển xe mới
    3.Cập nhật giá vé
    4.Hủy chuyển xe khỏi lịch trình
    5.Tìm kiếm chuyển xe
    6.Thống kê trang thái xe
    7.Phân loại tự động
    8. Thoát chương trình
=======================================
""")

def show_list (bus_list):
    if not bus_list:
        print("Danh sách trống")
        return
    
    print(f"{'Mã':<5}| {'Tuyến đường':<25}| {'Giá':<15}| {'Ghế trống':<10}| {'Tổng số ghế':<15}| {'Doanh thu':<15}| {'Trạng thái':<15}")
    for i, v in enumerate(bus_list):
        print(f"{v.get("bus_id"):<5}| {v.get("route"):<25}| {v.get("price_ticket"):<15}| {v.get("empty_seats"):<10}| {v.get("total_seats"):<15}| {v.get("current_revenue"):<15}| {v.get("status"):<15}")

# kiếm tra đầu vào    
def validate_input(prompt: str, input_type: str = "str"):
    while True:
        users = input(prompt).strip().title()

        if not users:
            print("Dữ liệu không được trống")
            continue

        if input_type == "int":
            try:
                value = int(users)
                if value <= 0:
                    print("Phải là số nguyên dương và lớn 0! Nhập lại")
                    continue
                return value
            except ValueError:
                print("Dữ liệu không hợp lệ!")
                continue
        return users

# Chức năng khai báo
def declaration_bus (bus_list):
    if not bus_list:
        print("Danh sách trống")
        return
    
    while True:
        bus_id = validate_input("Nhập mã CX mới: ")
        for i, v in enumerate(bus_list):
            if bus_id.upper() == v.get("bus_id").upper():
                print("Mã không được trùng! Hãy nhập lại")
                break
        else:
            break
    route = validate_input("Nhập tuyến đường mới: ")
    price_ticket = validate_input("Nhập giá vé xe: ", "int")
    total_seats = validate_input("Nhập tổng ghế: ", "int")
    empty_seats = total_seats

    number_seats_out = total_seats - empty_seats
    current_revenue = price_ticket * number_seats_out
 
    if empty_seats == 0:
        status = 'Hết vé'
    elif empty_seats < 0.15 * total_seats:
        status = 'hút khách'
    elif 0.15 * total_seats <= empty_seats <= 0.8 * total_seats:
        status = 'Bình thường'
    else:
        status = 'Ế khách'
    
    new_bus = {
        "bus_id": bus_id, 
        "route": route, 
        "price_ticket": price_ticket, 
        "empty_seats": empty_seats, 
        "total_seats": total_seats, 
        "current_revenue": current_revenue, 
        "status": status
    }
    bus_list.append(new_bus)
    print("Khai báo chuyển xe mới thành công!")

def classify_status(bus):
    if bus["empty_seats"] == 0:
        status = 'Hết vé'
    elif bus["empty_seats"] < 0.15 * bus["total_seats"]:
        status = 'hút khách'
    elif 0.15 * bus["total_seats"] <= bus["empty_seats"] <= 0.8 * bus["total_seats"]:
        status = 'Bình thường'
    else:
        status = 'Ế khách'


def update_ticket (bus_list):
    if not bus_list:
        print("Danh sách trống")
        return
    
    while True:
        bus_id = validate_input("Nhập mã cần cập nhật: ")
        for i, v in enumerate(bus_list):
            if bus_id.upper() == v.get("bus_id").upper():
                quantity = validate_input("Nhập số lượng vé đặt: ", "int")
                if quantity > v.get("empty_seats"):
                    print("Sô ghế trống không với số vé, vui lòng nhập lại!")
                    continue

                v["empty_seats"] -= quantity
                number_of_seats = v.get("total_seats") - v.get("empty_seats")
                v["current_revenue"] = v.get("price_ticket") * number_of_seats

                classify_status(v)
                print("Cập nhật thành công!")
                return
        else:
            print("Không tìm thấy mã xe! nhập lại")
            continue            

def cancel_bus(bus_list):
    if not bus_list:
        print("Danh sách trống")
        return
    
    while True:
        bus_id = validate_input("Nhập mã CX muốn hủy: ")
        for i, v in enumerate(bus_list):
            if bus_id.upper() == v.get("bus_id").upper():
                print('Bạn có chắc chắn muốn xóa chuyển xe này khỏi lịch trình không')
                mini_choice = validate_input("Y/N: ")
                if mini_choice.upper() == "Y":
                    bus_list.pop(i)
                elif mini_choice.upper() == "N":
                    print("Thoát hủy thành công!")
                    return
                else: 
                    print("Lựa chọn không hợp lệ!")
                    break
        else:
            print("Không tìm thấy mã xe!")
            continue

def search_bus(bus_list):
    if not bus_list:
        print("Danh sách trống")
        return
    
    while True:
        input_search = validate_input("Nhập mã CX hoặc Tuyến đường gần nhất: ")
        for i, v in enumerate(bus_list):
            if input_search.upper() == v.get("bus_id").upper() or input_search.title() in v.get("route"):
                print(f"Mã xe: {v.get("bus_id"):<5}| Tuyến đường: {v.get("route"):<20}| Giá vé: {v.get("price_ticket")}")
                return
        else:
            print("Không tìm chuyển xe! Nhập lại")
            continue

def statistical_bus(bus_list):
    if not bus_list:
        print("Danh sách trống")
        return
    few_bus = 0
    normal_bus = 0
    attract_bus = 0
    sold_out = 0

    for i, v in enumerate(bus_list):

        if v.get("status") == "Hết vé":
            sold_out += 1
        elif v.get("status") == "Hút khách":
            attract_bus += 1
        elif v.get("status") == "Bình thường":
            normal_bus += 1
        else:
            few_bus += 1

    print(f"Ế: {few_bus}")
    print(f"Hết vé: {sold_out}")
    print(f"Hút khách: {attract_bus}")
    print(f"Bình thường: {normal_bus} ")
def main():
    bus_list = [
        {
            "bus_id": "CX001", 
            "route": "Sài Gòn - Đà Lạt", 
            "price_ticket": 30000, 
            "empty_seats": 5, 
            "total_seats": 40, 
            "current_revenue": 10500000, 
            "status": "Hút khách"
            }
    ]
    while True:
        menu()

        choice = input("Mời bạn nhập lựa chọn: ").strip()

        match choice:
            case "1":
                print("-------- Danh sách xe --------")
                show_list (bus_list) 
            case "2":
                print("------- Khai báo chuyển xe --------")
                declaration_bus (bus_list)
            case "3":
                print("------ Cập nhật vé ---------")
                update_ticket (bus_list)
            case "4":
                print("------ Hủy chuyển -------")
                cancel_bus(bus_list)
            case "5":
                print("------- tìm chuyển xe ------")
                search_bus(bus_list)
            case "6":
                print("------ Thống kê ------")
                statistical_bus(bus_list)
            case "7":
                print()
            case "8":
                print("Bạn đã thoát thành công!")
                break
            case _:
                print("Lựa chọn không hợp lệ")

main()
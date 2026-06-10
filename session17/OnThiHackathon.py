def menu():
    print("""
===================== list player ==================
    1. Hiển thị sanh sách cầu thủ
    2. Tiếp nhận cầu thủ mới
    3. Cập nhật thông tin và chỉ số
    4. Xóa cầu thủ
    5. Tìm kiếm cầu thủ
    6. Thống kê phân loại phong độ
    7. Đánh giá phong độ tự động
    8. Thoát chương trình
====================================================
""")
    
def show_list (player_list):
    if not player_list:
        print("Danh sách cầu thủ đang rỗng")
        return
    
    print(f"{'Mã CT':<5}| {'Họ & Tên':<20}| {'Số trận':<10}| {'Số Bàn Thắng':<15}| {'Kiến Tạo':<10}| {'Hiệu suất':<15}| {'Phân loại':<25}")
    for i, v in enumerate(player_list):
        print(f"{v.get('player_id'):<5}| {v.get('fullname'):<20}| {v.get('matches'):<10}| {v.get('goal'):<15}| {v.get('construction'):<10}| {v.get('efficiency', "Chưa có dữ liệu"):<15}| {v.get('classify',"Chưa có dữ liệu"):<25}")

def validate_input (prompt: str, type_input: str = "str"):
    while True:
        users_input = input(prompt)

        if not users_input:
            print("Dữ liệu không được để trống!")
            continue

        if type_input == "int":
            try:
                value = int(users_input)
                if value < 0:
                    print("Giá trị phải là số nguyên và không được âm!")
                    continue
                return value
            except ValueError:
                print("Dữ liệu không hợp lệ!")
                continue
        
        
        return users_input
    
def add_player (player_list):
    if not player_list:
        print("Danh sách cầu thủ đang rỗng")
        return
    
    while True:
        new_player_id = validate_input("Nhập vào mã cầu thủ: ")
        for i, v in enumerate(player_list):
            if new_player_id.upper() == v.get("player_id").upper():
                print("Mã cầu thủ đã tồn tại!")
                break
        else:
            break
    fullname = validate_input("Nhập họ tên cầu thủ: ")
    matches = validate_input("Nhập vào số trận đấu", "matches") 
    goal = validate_input("Nhập số bàn thắng: ", "int")
    construction = validate_input("Nhập số kiến tạo: ", "int")
    efficiency = (matches * 1) + (goal * 3) + (construction * 2)
    classify = classify_player(efficiency)

    new = {
        "player_id": new_player_id,
        "fullname": fullname,
        "matches": matches,
        "goal": goal,
        "construction": construction,
        "efficiency": efficiency,
        "classify": classify
    }

    player_list.append(new)
    return

def classify_player (efficiency):

    if efficiency < 15:
        return  "Cần thanh lý"
    elif efficiency < 30:
        return  "Dự bị chiến lược"
    elif efficiency < 50:
        return  "Trụ cột đội bóng"
    else:
        return  "Ngôi sao đẳng cấp"


                


def main():
    player_list = [
        {
            "player_id": "CT007",
            "fullname": "Nguyen Quang Hải",
            "matches": 10,
            "goal": 5,
            "construction": 4,
        }
    ]

    while True:

        menu()
        choice = input("Mời bạn nhập lựa chọn: ").strip()

        match choice:
            case "1":
                print("----------- Hiển thị player ------------")
                show_list (player_list)
            case "2":
                print("----------- Tiếp nhận cầu thủ ------------")
                add_player (player_list)
            case "3":
                print()
            case "4":
                print()
            case "5":
                print()
            case "6":
                print()
            case "7":
                print()
            case "8":
                print("Bạn đã thoát khỏi chương trình thành công!")
                break
            case _:
                print("Lựa chon không hợp lệ!")
main()
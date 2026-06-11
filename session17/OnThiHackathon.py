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

def validate_input (prompt: str, type_input: str ="str"):
    while True:
        users = input(prompt)

        if not users:
            print("Dữ liệu không được trống! Nhập lại")
            continue

        if type_input == "int":
            try:
                value = int(users)
                if value < 0:
                    print("Số nguyên phải lớn hơn hoặc bằng 0! nhập lại")
                    continue
                return value
            except ValueError:
                print("Dữ liệu không hợp lệ!")
                continue

        if type_input == "matches":
            try:
                value = int(users)
                if 0 > value > 50:
                    print("Số trận thi đấu phải nằm trong khoảng 0 đến 50")
                    continue
                return value
            except ValueError:
                print("Dữ liệu không hợp lệ!")
                continue
        return users

def add_player (player_list):
    if not player_list:
        print("Danh sách cầu thủ đang rỗng")
        return
    while True:
        input_id = validate_input("Nhập mã CT: ")
        for i, v in enumerate(player_list):
            if input_id.upper() == v.get("player_id").upper():
                print("Mã CT đã tồn tại! vui lòng nhập lại")
                break
        else:
            break
    input_name = validate_input("Nhập tên cầu thủ: ")
    matches = validate_input("Nhập số trận: ", "matches")
    goal = validate_input("Nhập số bàn thắng: ", "int")
    construction = validate_input("Nhập số lần kiến tạo: ", "int")
    efficiency = (matches * 1) + (goal * 2) + (construction * 3)

    classify = classify_player (efficiency)

    new_player = {
        "player_id": input_id,
        "fullname": input_name,
        "matches": matches,
        "goal": goal,
        "construction": construction,
        "efficiency": efficiency,
        "classify": classify
    }

    player_list.append(new_player)
    return


def classify_player (efficiency):

    if efficiency < 15:
        return "Cần thanh lý"
    elif 15 <= efficiency <= 30:
        return "Dự bị"
    elif 30 <= efficiency <= 50:
        return "Trụ cột"
    else:
        return "Ngôi sao"
    
def update_player (player_list):
    if not player_list:
        print("Danh sách cầu thủ đang rỗng")
        return
    
    input_id = validate_input("Nhập mã CT cần cập nhật: ")
    for i, v in enumerate(player_list):
        if input_id.upper() == v.get("player_id").upper():
            v["matches"] = validate_input("Cập nhật lại số trận: ", "matches")
            v["goal"] = validate_input("Cập nhật lại bàn thắng: ", "int")
            v["construction"] = validate_input("Cập nhật lại số lần kiến tạo: ", "int")

            v["efficiency"] = (v["matches"] * 1) + (v["goal"] * 2) + (v["construction"] * 3)
            v["classify"] = classify_player (v["efficiency"])
            return
    else:
        print("Không tìm thấy mã CT!")
        return

def delete_player (player_list):
    if not player_list:
        print("Danh sách cầu thủ đang rỗng")
        return
    
    input_id = validate_input("Nhập mã CT muốn xóa: ")
    for i, v in enumerate(player_list):
        if input_id.upper() == v.get("player_id").upper():
            print("Bạn có chắc chắn muốn xóa cầu thủ này khỏi danh sách không? (Y/N)")
            mini_choice = validate_input("")
            if mini_choice.upper() == "Y":
                print("Bạn đã xóa thành công!")
                player_list.pop(i)
                return
            else:
                print("Bạn đã không đồng ý!")
                return
    else:
        print("Không tìm thấy mã cầu thủ!")
        return

def search_player (player_list):
    if not player_list:
        print("Danh sách cầu thủ đang rỗng")
        return
    
    flag = False
    search = validate_input("Nhập mã CT hoặc tên CT bạn muốn tìm: ")
    for i, v in enumerate(player_list):
        if search.upper() == v.get("player_id").upper() or search.title() in v.get("fullname").title():
            flag = True
            print(f"{v.get('player_id'):<5}| {v.get('fullname'):<20}| {v.get('matches'):<10}| {v.get('goal'):<15}| {v.get('construction'):<10}| {v.get('efficiency', "Chưa có dữ liệu"):<15}| {v.get('classify',"Chưa có dữ liệu"):<25}")

    if not flag:
        print("Không tìm thấy cầu thủ!")
    return    

def statistics_player (player_list):
    if not player_list:
        print("Danh sách cầu thủ đang rỗng")
        return
    classify_star = 0
    classify_classify = 0
    classify_reserve = 0
    reserve_liq = 0

    
 
    for i, v in enumerate(player_list):
        if v.get("classify") == "Cần thanh lý":
            reserve_liq += 1
        elif v.get("classify") == "Ngôi sao":
            classify_star += 1
        elif v.get("classify") == "Trụ cột":
            classify_classify += 1
        else: 
                classify_reserve += 1

    print(f"Ngôi sao: {classify_star}")
    print(f"Cần thành lý: {reserve_liq}")
    print(f"Trụ cột: {classify_classify}")
    print(f"Dự bị: {classify_reserve}")
    return

def auto_player(player_list):
    if not player_list:
        print("Danh sách cầu thủ đang rỗng")
        return
    
    for i, v in enumerate(player_list):
        v["efficiency"] = (v["matches"] * 1) + (v["goal"] * 2) + (v["construction"] * 3)
        v["classify"] = classify_player (v["efficiency"])
        
def main():
    player_list = [
        {
            "player_id": "CT007",
            "fullname": "Nguyen Quang Hải",
            "matches": 10,
            "goal": 5,
            "construction": 4
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
                print("------ Cập nhật thông tin --------")
                update_player (player_list)
            case "4":
                print("-------- Xóa cầu thủ ---------")
                delete_player (player_list)
                
            case "5":
                print("-------- Tìm Cầu thủ -----------")
                search_player (player_list)
            case "6":
                print("------- Thống kê --------")
                statistics_player (player_list)
            case "7":
                print()
            case "8":
                print("Bạn đã thoát khỏi chương trình thành công!")
                break
            case _:
                print("Lựa chon không hợp lệ!")
main()
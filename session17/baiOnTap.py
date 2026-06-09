def get_validate_input(prompt, input_type="str"):
    while True:
        user_input = input(prompt).strip()

        if not user_input:
            print("Dữ liệu không được để trống!")
            continue

        if input_type == "int":
            if user_input.isdigit():
                return int(user_input)
            else:
                print("Vui lòng nhập số!")
                continue

        return user_input


def get_status(empty_chair, all_chair):
    if empty_chair == 0:
        return "Hết vé"

    rate = empty_chair / all_chair

    if rate < 0.15:
        return "Hút khách"
    elif rate <= 0.8:
        return "Bình thường"
    else:
        return "Ế khách"


def get_income(travel):
    sold = travel["all_chair"] - travel["empty_chair"]
    return sold * travel["price"]


def menu():
    print("\n" + "=" * 60)
    print("      HỆ THỐNG QUẢN LÝ CHUYẾN XE")
    print("=" * 60)
    print("1. Hiển thị danh sách chuyến xe")
    print("2. Khai báo chuyến xe mới")
    print("3. Cập nhật đặt vé")
    print("4. Hủy chuyến xe khỏi lịch trình")
    print("5. Tìm kiếm chuyến xe")
    print("6. Thống kê trạng thái chuyến xe")
    print("7. Rà soát và cập nhật trạng thái")
    print("8. Thoát")


def show_travel_list(travel_list):
    if not travel_list:
        print("Danh sách chuyến xe đang trống!")
        return

    print("\n" + "-" * 130)
    print(
        f"{'STT':<5}"
        f"{'Mã CX':<10}"
        f"{'Tuyến đường':<30}"
        f"{'Giá vé':<15}"
        f"{'Ghế trống':<15}"
        f"{'Tổng ghế':<15}"
        f"{'Doanh thu':<20}"
        f"{'Trạng thái'}"
    )
    print("-" * 130)

    for index, travel in enumerate(travel_list, start=1):
        print(
            f"{index:<5}"
            f"{travel['id']:<10}"
            f"{travel['road']:<30}"
            f"{travel['price']:<15,}"
            f"{travel['empty_chair']:<15}"
            f"{travel['all_chair']:<15}"
            f"{get_income(travel):<20,}"
            f"{travel['status']}"
        )


def new_travel(travel_list):
    print("\nTHÊM CHUYẾN XE")

    while True:
        trv_id = get_validate_input("Nhập mã chuyến xe: ")

        duplicated = False

        for item in travel_list:
            if item["id"].lower() == trv_id.lower():
                duplicated = True
                break

        if duplicated:
            print("Mã chuyến xe đã tồn tại!")
        else:
            break

    trv_road = get_validate_input("Nhập tuyến đường: ")

    while True:
        trv_price = get_validate_input("Nhập giá vé: ", "int")
        if trv_price > 0:
            break
        print("Giá vé phải lớn hơn 0!")

    while True:
        trv_allchair = get_validate_input("Nhập tổng số ghế: ", "int")
        if trv_allchair > 0:
            break
        print("Tổng số ghế phải lớn hơn 0!")

    new_item = {
        "id": trv_id,
        "road": trv_road,
        "price": trv_price,
        "empty_chair": trv_allchair,
        "all_chair": trv_allchair,
        "status": get_status(trv_allchair, trv_allchair)
    }

    travel_list.append(new_item)
    print("Thêm chuyến xe thành công!")


def update_booking(travel_list):
    if not travel_list:
        print("Danh sách chuyến xe đang trống!")
        return

    trv_id = get_validate_input("Nhập mã chuyến xe: ")

    for item in travel_list:

        if item["id"].lower() == trv_id.lower():

            while True:
                quantity = get_validate_input(
                    "Nhập số lượng vé đặt: ",
                    "int"
                )

                if quantity <= 0:
                    print("Số vé phải lớn hơn 0!")
                    continue

                if quantity > item["empty_chair"]:
                    print("Số vé vượt quá ghế trống!")
                    continue

                item["empty_chair"] -= quantity

                item["status"] = get_status(
                    item["empty_chair"],
                    item["all_chair"]
                )

                print("Đặt vé thành công!")
                return

    print("Không tìm thấy chuyến xe!")


def delete_travel(travel_list):
    if not travel_list:
        print("Danh sách chuyến xe đang trống!")
        return

    trv_id = get_validate_input("Nhập mã chuyến xe cần xóa: ")

    for index, item in enumerate(travel_list):

        if item["id"].lower() == trv_id.lower():

            confirm = input(
                "Bạn có chắc muốn xóa chuyến xe này? (Y/N): "
            ).upper()

            if confirm == "Y":
                travel_list.pop(index)
                print("Xóa thành công!")
            else:
                print("Đã hủy thao tác!")

            return

    print("Không tìm thấy chuyến xe!")


def search_travel(travel_list):
    if not travel_list:
        print("Danh sách chuyến xe đang trống!")
        return

    print("\n1. Tìm theo mã chuyến xe")
    print("2. Tìm theo tuyến đường")

    choice = input("Chọn: ")

    result = []

    if choice == "1":

        keyword = get_validate_input("Nhập mã chuyến xe: ")

        for item in travel_list:
            if item["id"].lower() == keyword.lower():
                result.append(item)

    elif choice == "2":

        keyword = get_validate_input("Nhập tuyến đường: ")

        for item in travel_list:
            if keyword.lower() in item["road"].lower():
                result.append(item)

    else:
        print("Lựa chọn không hợp lệ!")
        return

    if result:
        show_travel_list(result)
    else:
        print("Không tìm thấy dữ liệu!")


def main():

    travel_list = [
        {
            "id": "CX001",
            "road": "Sài Gòn - Đà Lạt",
            "price": 300000,
            "empty_chair": 5,
            "all_chair": 40,
            "status": "Hút khách"
        },
        {
            "id": "CX002",
            "road": "Sài Gòn - Nha Trang",
            "price": 250000,
            "empty_chair": 35,
            "all_chair": 40,
            "status": "Ế khách"
        }
    ]

    while True:

        menu()

        choice = input("Nhập lựa chọn của bạn: ")

        match choice:

            case "1":
                show_travel_list(travel_list)

            case "2":
                new_travel(travel_list)

            case "3":
                update_booking(travel_list)

            case "4":
                delete_travel(travel_list)

            case "5":
                search_travel(travel_list)
            case "6":
                print("Cảm ơn đã sử dụng chương trình!")
                break
            case _:
                print("Lựa chọn không hợp lệ!")


main()
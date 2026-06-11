orders_list = []


def menu():
    print("""
==================================================
            QUẢN LÝ ĐƠN HÀNG - AGENT ORDER
==================================================
1. Xem danh sách đơn hàng hiện có
2. Tạo mới đơn hàng đại lý
3. Cập nhật trạng thái thanh toán
4. Tính tổng doanh thu & Chiết khấu
5. Thoát chương trình
==================================================
""")


def validate_input(message):
    while True:
        value = input(message).strip()
        if value:
            return value
        print("[Lỗi]: Không được để trống dữ liệu!")


def validate_amount():
    while True:
        try:
            amount = float(input("Nhập giá trị đơn hàng (VND): "))
            if amount > 0:
                return amount
            print("[Lỗi][ERR-02]: Giá trị đơn hàng phải là số tiền lớn hơn 0!")
        except ValueError:
            print("[Lỗi][ERR-02]: Giá trị đơn hàng phải là số tiền lớn hơn 0!")


def show_orders(orders_list):
    if not orders_list:
        print("[Trạng thái]: Chưa có đơn hàng nào trong hệ thống!")
        return

    print("\n{:<15}{:<25}{:<20}{:<15}".format(
        "MÃ ĐƠN", "TÊN ĐẠI LÝ", "GIÁ TRỊ(VND)", "TRẠNG THÁI"
    ))
    print("-" * 75)

    for order in orders_list:
        print("{:<15}{:<25}{:<20,.0f}{:<15}".format(
            order["id"],
            order["agent_name"],
            order["total_amount"],
            order["status"]
        ))


def create_order(orders_list):
    order_id = validate_input("Nhập mã đơn hàng: ").upper()

    for order in orders_list:
        if order["id"] == order_id:
            print("[Lỗi][ERR-01]: Mã đơn hàng này đã tồn tại trong hệ thống!")
            return

    agent_name = validate_input("Nhập tên đại lý: ")

    total_amount = validate_amount()

    new_order = {
        "id": order_id,
        "agent_name": agent_name,
        "total_amount": total_amount,
        "status": "Unpaid"
    }

    orders_list.append(new_order)

    print(f"[Thành công]: Đơn hàng {order_id} đã được tạo thành công!")


def update_payment_status(orders_list):
    if not orders_list:
        print("[Trạng thái]: Danh sách đơn hàng đang rỗng!")
        return

    order_id = validate_input(
        "Nhập mã đơn hàng cần cập nhật: "
    ).upper()

    for order in orders_list:
        if order["id"] == order_id:

            if order["status"] == "Paid":
                print("[Lỗi][ERR-04]: Đơn hàng này đã được thanh toán trước đó!")
                return

            order["status"] = "Paid"

            print(
                f"[Thành công]: Đơn hàng {order_id} đã được cập nhật trạng thái ĐÃ THANH TOÁN."
            )
            return

    print(f"[Lỗi][ERR-03]: Không tìm thấy đơn hàng nào có mã {order_id}!")


def calculate_financials(orders_list):
    revenue = 0

    for order in orders_list:
        if order["status"] == "Paid":
            revenue += order["total_amount"]

    if revenue >= 100_000_000:
        discount = revenue * 0.05
    else:
        discount = 0

    return revenue, discount


def show_financial_report(orders_list):
    revenue, discount = calculate_financials(orders_list)

    print("\n========== BÁO CÁO TÀI CHÍNH ==========")
    print(f"Tổng doanh thu thực tế : {revenue:,.0f} VND")
    print(f"Chiết khấu doanh nghiệp: {discount:,.0f} VND")
    print(f"Doanh thu sau chiết khấu: {(revenue-discount):,.0f} VND")
    print("=======================================")


while True:
    menu()

    try:
        choice = int(input("Mời chọn chức năng (1-5): "))

        match choice:
            case 1:
                show_orders(orders_list)

            case 2:
                create_order(orders_list)

            case 3:
                update_payment_status(orders_list)

            case 4:
                show_financial_report(orders_list)

            case 5:
                print("Đã thoát chương trình!")
                break

            case _:
                print("[Lỗi][ERR-05]: Lựa chọn không hợp lệ. Vui lòng nhập số từ 1 đến 5!")

    except ValueError:
        print("[Lỗi][ERR-05]: Lựa chọn không hợp lệ. Vui lòng nhập số từ 1 đến 5!")
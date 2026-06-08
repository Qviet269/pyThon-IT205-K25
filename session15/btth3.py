available_seats = 50
flight_revenue = 0.0
BASE_PRICE = 2000.0


def menu():
    print("""
============= SKYBOOKING SYSTEM =============
Chuyến bay: VN2026 | Khởi hành: Hà Nội
1. Đặt vé máy bay
2. Hủy vé & Hoàn tiền
3. Xem tình trạng chuyến bay
4. Đóng hệ thống
=============================================
""")


def validate_input(prompt):

    while True:

        try:
            data = int(input(prompt))

            if data <= 0:
                print("Dữ liệu phải lớn hơn 0")
            else:
                return data

        except:
            print("Vui lòng nhập số")


def calculate_ticket_price(quantity, seat):

    if seat == 1:
        price = BASE_PRICE
    else:
        price = BASE_PRICE * 1.5

    total = price * quantity

    service = total * 0.05

    final_total = total + service

    return final_total, service, total


def book_flight(quantity, final_total):

    global available_seats
    global flight_revenue

    if quantity > available_seats:
        print(f"Rất tiếc, chuyến bay chỉ còn [{available_seats}] chỗ trống")
        return False

    available_seats -= quantity

    flight_revenue += final_total

    return True


def cancel_booking(quantity):

    global available_seats
    global flight_revenue

    if available_seats + quantity > 50:
        print("Lỗi: Số lượng vé hủy vượt quá số vé đã bán ra.")
        return None

    refund = quantity * (BASE_PRICE * 0.8)

    available_seats += quantity

    flight_revenue -= refund

    return refund


def flight_report():

    """
    Hàm hiển thị báo cáo hiện tại của chuyến bay VN2026.
    Bao gồm:
    - Tổng sức chứa
    - Ghế đã đặt
    - Ghế trống
    - Tổng doanh thu
    """

    booked_seats = 50 - available_seats

    print("--- TÌNH TRẠNG CHUYẾN BAY VN2026 ---")
    print("Sức chứa tối đa: 50")
    print(f"Ghế đã đặt: {booked_seats}")
    print(f"Ghế trống: {available_seats}")
    print(f"Tổng doanh thu hiện tại: ${flight_revenue:,.1f}")


def main():

    while True:

        menu()

        choice = input("Chọn chức năng (1-4): ").strip()

        match choice:

            case "1":

                print("--- ĐẶT VÉ MÁY BAY ---")

                quantity = validate_input("Nhập số lượng vé: ")

                while True:

                    seat = validate_input("Chọn hạng vé (1: Economy, 2: Business): ")

                    if seat in [1, 2]:
                        break

                    print("Hạng vé không tồn tại")

                final_total, service, total = calculate_ticket_price(quantity, seat)

                if seat == 1:
                    seat_name = "Economy"
                else:
                    seat_name = "Business"

                check = book_flight(quantity, final_total)

                if check:

                    print("-> Xác nhận đặt chỗ:")
                    print(f"Số lượng: {quantity} | Hạng: {seat_name}")
                    print(f"Tạm tính: ${total}")
                    print(f"Phí dịch vụ (5%): ${service}")
                    print(f"Tổng thanh toán: ${final_total}")
                    print(f"Đặt vé thành công! Ghế trống còn lại: {available_seats}")

            case "2":

                print("--- HỦY VÉ & HOÀN TIỀN ---")

                quantity = validate_input("Nhập số lượng vé muốn hủy: ")

                refund = cancel_booking(quantity)

                if refund != None:

                    print(f"Hủy vé thành công. Hệ thống đã hoàn lại: ${refund} (80% giá cơ bản).")
                    print(f"Ghế trống hiện tại: {available_seats}")

            case "3":

                flight_report()

            case "4":

                print("Đóng hệ thống...")
                break

            case _:

                print("Lựa chọn không hợp lệ!")


main()
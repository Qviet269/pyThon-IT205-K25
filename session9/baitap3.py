
# PHÂN TÍCH & THIẾT KẾ GIẢI PHÁP QUẢN LÝ ĐƠN HÀNG


# 1. INPUT / OUTPUT
# - Input: 
#   + order_list: Kiểu List[str] (mảng chứa mã đơn hàng ban đầu).
#   + choice: Kiểu str (lựa chọn menu từ bàn phím).
#   + new_order / del_order: Kiểu str (mã đơn do người dùng nhập).
# - Output: Menu điều khiển, danh sách đơn hàng có đánh số (1, 2, 3...) hoặc thông báo lỗi/thành công.

# 2. GIẢI PHÁP KỸ THUẬT
# - Dùng vòng lặp 'while True' + cấu trúc 'match-case' để điều hướng menu (1-4).
# - Xử lý bẫy dữ liệu (Edge Cases):
#   + Dùng hàm '.strip().upper()' để ép toàn bộ mã đơn nhập vào về dạng chuẩn (Xóa khoảng trắng thừa, viết hoa).
#   + Sử dụng toán tử 'in' kiểm tra sự tồn tại của mã trước khi dùng '.remove()' để tránh lỗi crash chương trình (ValueError).
# - Thao tác List: Kiểm tra mảng rỗng bằng 'len(order_list) > 0'; Duyệt index tăng dần bằng 'enumerate(order_list, 1)'; Thêm phần tử bằng '.append()'.

# 3. THUẬT TOÁN (PSEUDOCODE)
# Bắt đầu vòng lặp:
#   Hiển thị 4 chức năng menu
#   Nhận choice từ người dùng
#   Khớp choice:
#     Nếu "1": Nếu len(order_list) > 0 -> Duyệt vòng lặp for in ra "index. mã_đơn". Ngược lại -> Báo danh sách trống.
#     Nếu "2": Nhập mã mới -> Chuẩn hóa (.strip().upper()) -> Thêm vào cuối bằng .append().
#     Nếu "3": Nhập mã cần xóa -> Chuẩn hóa -> Nếu mã có 'in' order_list -> Xóa bằng .remove(). Ngược lại -> Báo lỗi không tìm thấy.
#     Nếu "4": In thông báo thoát -> Gọi lệnh 'break' dừng vòng lặp.
#     Trường hợp khác (_): Báo lựa chọn không hợp lệ, lặp lại menu.
# Kết thúc vòng lặp.

order_list = ["GE001", "GE002", "GE003"]

while True:
    print("""
======= Hệ Thống Quản Lý Đơn Hàng Grap Express =======
1. Hiển thị sanh sách đơn hàng
2. Thêm đơn hàng theo mã
3. Xóa đơn hàng theo mã
4. Thoát chương trinh
""")
    choice = input('Lựa chọn của bạn (1-5): ')

    match choice:
        case "1":
            if len(order_list) > 0:
                print('\nDanh sach đơn hàng hiện tại')
                for i, v in enumerate(order_list, 1):
                    print(f'{i}. {v}')
            else:
                print('Danh sách đơn hàng hiện đang trống!')
        case "2":
            new_order = input('Nhập mã đơn hàng mới: ').strip().upper()
            order_list.append(new_order)

            print(order_list)
        case "3":
            del_order = input('Nhập mã đơn hàng cần xóa: ').strip().upper()
            if del_order in order_list:
                order_list.remove(del_order)
                print('Đã xóa thành công!')
            else:
                print('Không tìm thấy mã đơn hàng cần xóa')
        case "4":
            print('Thoát chương trình')
            break
        case _:
            print("lựa chọn không hợp lệ")
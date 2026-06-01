

# I. PHÂN TÍCH INPUT / OUTPUT 

# 1. INPUT (Dữ liệu vào):
#    - choice: Lựa chọn chức năng từ menu (Kiểu: Chuỗi - String)
#    - name_shop, product, description, category: Thông tin sản phẩm (Kiểu: Chuỗi)
#    - list_search: Chuỗi từ khóa cách nhau bằng dấu phẩy (Kiểu: Chuỗi)
#    - voucher: Mã giảm giá cần kiểm tra (Kiểu: Chuỗi)
#    - find_key, replace_key: Từ khóa cần tìm và từ khóa thay thế (Kiểu: Chuỗi)
#
# 2. OUTPUT (Dữ liệu ra):
#    - Giao diện menu dòng lệnh cố định (1 đến 5)
#    - Chức năng 1: Báo cáo thống kê sản phẩm đã xử lý khoảng trắng và chữ hoa/thường
#    - Chức năng 2: Tên shop dạng URL (Ví dụ: shop-rikkei-education-mall)
#    - Chức năng 3: Kết quả thông báo mã hợp lệ hoặc chi tiết lỗi vi phạm
#    - Chức năng 4: Số lần từ khóa xuất hiện và mô tả mới sau khi thay thế




# II. ĐỀ XUẤT GIẢI PHÁP & PHƯƠNG THỨC XỬ LÝ 

# 1. Các phương thức xử lý chuỗi áp dụng:
#    - .strip(): Xóa khoảng trắng thừa ở hai đầu chuỗi (Shop, Sản phẩm, Mô tả)
#    - .lower() / .upper(): Chuyển chuỗi thành chữ thường / chữ hoa toàn bộ
#    - .title(): Viết hoa chữ cái đầu tiên của mỗi từ (Tên sản phẩm)
#    - .split(): Cắt chuỗi thành Danh sách (Nếu trống: cắt theo khoảng trắng và xóa rác)
#    - .join(): Nối Danh sách thành Chuỗi bằng ký tự chỉ định (" ", "-", ", ")
#    - .replace(): Thay thế cụm từ cũ bằng cụm từ mới (Chức năng 4)
#    - .count(): Đếm số lần xuất hiện của từ khóa trong văn bản (Chức năng 4)
#
# 2. Các hàm kiểm tra điều kiện (Validation):
#    - len(): Đếm số ký tự chuỗi hoặc đếm số lượng phần tử trong Danh sách
#    - " " in chuỗi: Kiểm tra xem chuỗi có chứa khoảng trắng hay không
#    - .isupper(): Kiểm tra chuỗi có viết hoa toàn bộ hay không
#    - .isalnum(): Kiểm tra chuỗi chỉ chứa chữ và số (không chứa ký tự đặc biệt)
#    - .startswith(): Kiểm tra chuỗi có bắt đầu bằng cụm từ chỉ định không (SALE, shop-)




# III. THIẾT KẾ THUẬT TOÁN

# BẮT ĐẦU (START)
# Vòng lặp vô hạn (while True):
#     Hiển thị MENU -> Nhập lựa chọn (choice)
#     Rẽ nhánh cấu trúc (match choice):
#
#         Trường hợp "1": Nhập thông tin SP
#             In name_shop.strip() và product.strip().title()
#             In description.strip() và len(description.strip())
#             Xử lý Danh mục: .split() rồi .join(" ") lại để xóa khoảng trắng thừa ở giữa
#             Xử lý Từ khóa: .replace(",", " ").split() để dọn sạch khoảng trắng -> len() đếm số từ
#
#         Trường hợp "2": Chuẩn hóa tên shop
#             after_name_shop = name_shop.lower().split() (Xóa khoảng trắng thừa, chữ thường)
#             ten_ghep = "-".join(after_name_shop)
#             NẾU ten_ghep bắt đầu bằng "shop-": In ra ten_ghep
#             NẾU KHÔNG: In ra "shop-" + ten_ghep (Tránh bị lặp shop-shop-)
#
#         Trường hợp "3": Kiểm tra Voucher
#             NẾU rỗng -> Báo lỗi rỗng
#             NẾU " " trong voucher -> Báo lỗi chứa khoảng trắng (Sửa lỗi choice ở code cũ)
#             NẾU len < 6 hoặc len > 12 -> Báo lỗi độ dài
#             NẾU không .isupper() -> Báo lỗi chưa viết hoa toàn bộ
#             NẾU không .isalnum() -> Báo lỗi chứa ký tự đặc biệt
#             NẾU không .startswith('SALE') -> Báo lỗi không bắt đầu bằng SALE
#             NẾU KHÔNG VI PHẠM -> Báo hợp lệ
#
#         Trường hợp "4": Tìm kiếm & Thay thế
#             NẾU find_key có trong description:
#                 Đếm số lần = description.count(find_key)
#                 Cập nhật mô tả mới = description.replace(find_key, replace_key)
#                 In số lần và mô tả mới ra màn hình
#             NẾU KHÔNG: In không tìm thấy
#
#         Trường hợp "5": Thoát chương trình (break)
#         Trường hợp còn lại (_): Báo lựa chọn không hợp lệ
# KẾT THÚC (END)


while True:

    print("""
+======================================================+
|       Hệ Thống Quản Lý Nội Dung Sản Phẩm Shoppee     |
+======================================================+
|   1. Nhập dữ liệu sản phẩm và xem báo cáo thống kê   |
|   2. Chuẩn hóa tên shop                              |
|   3. Kiếm tra mã giảm giá hợp lệ                     |
|   4. tìm kiếm và thay thế từ khóa trong tả sản phẩm  |
|   5. Thoát chương trình                              |
+======================================================+
""")
    choice = input('> Mời bạn chọn chức năng (1 - 5): ')

    match choice:
        case "1":
            name_shop = input('Nhập tên shop: ')
            product = input('Nhập tên sản phẩm: ')
            description = input('Nhập mô tả sản phẩm: ')
            category = input('Nhập danh mục sản phẩm: ')
            list_search = input('Nhập danh sách từ khóa tìm kiếm: ')

            print(f'Tên Shop: {name_shop.strip()}')
            print(f'tên sản phẩm: {product.strip().title()}')
            print(f'Mô tả: {description.strip()}')
            print(f'Độ dài mô tả: {len(description.strip())}')
            print(f'Danh mục: {" ".join(category.split()).lower()}')

            item_list = list_search.replace(',', ' ').split()
            print(f'Danh sach: {", ".join(item_list)}')
            print(f'Số lượng từ: {len(item_list)} ')

            print(f'Mô tả sản phẩm chuyển sang thường: {description.lower()}')
            print(f'Mô tả sản phẩm chuyển sang hoa: {description.upper()}')
        case "2":
            print(f'Tên shop ban đầu: {name_shop}')

            after_name_shop = name_shop.strip().lower().split()

            print(f'Tên shop sau khi chuyển hóa: shop-{"-".join(after_name_shop)}')
        case "3":
            voucher = input('Nhập mã giảm giá: ')

            if len(voucher) == 0:
                print('Mã giảm giá không được rỗng')
            elif " " in choice:
                print('Mã giảm giá không được chứa khoảng trắng')
            elif len(voucher) < 6 or len(voucher) > 12:
                print('Mã giảm giá phải có độ dài 6 đến 12 ký tự')
            elif not voucher.isupper():
                print('Mã giảm giá phải được viết hóa toàn bộ')
            elif not voucher.isalnum():
                print('Mã giảm giá chỉ được chứa chữ cái và chữ số')
            elif not voucher.startswith('SALE'):
                print('Mã giảm giá phải bắt đầu bằng chuỗi SALE')
            else:
                print('Mã giảm giá hợp lệ')

        case "4":
            find_key = input('Nhập từ khóa cần tìm: ')
            replace_key = input('Nhập từ khóa thay thế: ')

            if find_key in description:
                new_description = description.replace(find_key, replace_key)
                number = description.count(find_key)

                print(f'từ khoa {find_key} đã xuất hiện {number} lần');
                print(f'Mô tả sau khi thay thế; {new_description}')
            else:
                print('Phù hợp')
        case "5":
            print('Thoát chương trình!')
            break
        case _:
            print("Lựa chọn không hợp lệ!");
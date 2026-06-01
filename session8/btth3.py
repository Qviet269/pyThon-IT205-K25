# I. PHÂN TÍCH INPUT / OUTPUT (DỮ LIỆU ĐẦU VÀO & ĐẦU RA)

# 1. INPUT (Dữ liệu vào):
#    - choice: Lựa chọn chức năng từ menu (Kiểu: Chuỗi - String)
#    - Chức năng 1: name_sender, phone_sender, address_sender, name_receiver, 
#                   phone_receiver, address_receiver, note: Thông tin đơn hàng (Chuỗi)
#    - Chức năng 2: order_id: Mã đơn hàng cần chuẩn hóa (Kiểu: Chuỗi)
#    - Chức năng 3: Ẩn SĐT dựa trên dữ liệu phone_sender và phone_receiver đã nhập ở CN1
#    - Chức năng 4: find_key, replace_key: Từ khóa cần tìm và thay thế (Kiểu: Chuỗi)
#
# 2. OUTPUT (Dữ liệu ra):
#    - Giao diện menu dòng lệnh gồm 5 lựa chọn cố định.
#    - Chức năng 1: Báo cáo thống kê thông tin đơn hàng đã làm sạch và xử lý chuỗi.
#    - Chức năng 2: Mã đơn hàng chuẩn hóa dạng URL (Ví dụ: GRAB-GX-12345).
#    - Chức năng 3: Định dạng số điện thoại bảo mật dạng ẩn (Ví dụ: 098*****21).
#    - Chức năng 4: Số lần từ khóa cũ xuất hiện và nội dung ghi chú mới sau thay thế.




# II. ĐỀ XUẤT GIẢI PHÁP & PHƯƠNG THỨC XỬ LÝ (STRING METHODS)

# 1. Các phương thức xử lý chuỗi áp dụng:
#    - .strip(): Xóa khoảng trắng thừa ở hai đầu chuỗi.
#    - .lower() / .upper(): Chuyển chuỗi thành chữ thường / chữ hoa toàn bộ.
#    - .title(): Viết hoa chữ cái đầu tiên của mỗi từ (Tên người gửi, người nhận).
#    - .split(): Cắt chuỗi thành Danh sách (Nếu trống: tự động dọn sạch khoảng trắng thừa).
#    - .join(): Nối Danh sách thành Chuỗi bằng ký tự chỉ định (" ", "-", "*").
#    - .replace(): Thay thế cụm từ cũ bằng cụm từ mới.
#    - .count(): Đếm số lần xuất hiện của cụm từ trong văn bản.
#
# 2. Các hàm kiểm tra điều kiện (Validation):
#    - len(): Đếm số ký tự chuỗi hoặc số lượng phần tử trong Danh sách.
#    - .isdigit(): Kiểm tra chuỗi chỉ chứa các ký tự số từ 0-9.
#    - .startswith(): Kiểm tra chuỗi có bắt đầu bằng cụm từ chỉ định không (GRAB-).

# BẮT ĐẦU (START)
# Vòng lặp vô hạn (while True):
#     Hiển thị MENU -> Nhập lựa chọn (choice)
#     Rẽ nhánh cấu trúc (match choice):
#
#         Trường hợp "1": Nhập & thống kê đơn hàng
#             Nhập: name_sender, phone_sender, address_sender, name_receiver, phone_receiver, address_receiver, note
#             Hiển thị name_sender.strip().title() và name_receiver.strip().title()
#             Xử lý Địa chỉ: .split() rồi .join(" ") để dọn sạch khoảng trắng thừa ở giữa
#             Xử lý Ghi chú: note_clean = note.strip()
#             Đếm số từ ghi chú: len(note_clean.split())
#             Hiển thị note_clean dạng chữ thường (.lower()) và chữ hoa (.upper())
#
#         Trường hợp "2": Chuẩn hóa mã đơn hàng
#             Nhập order_id
#             Chuyển viết hoa và cắt sạch khoảng trắng: id_split = order_id.upper().split()
#             Nối lại bằng dấu gạch ngang: id_joined = "-".join(id_split)
#             NẾU id_joined bắt đầu bằng "GRAB-":
#                 final_id = id_joined
#             NẾU KHÔNG:
#                 final_id = "GRAB-" + id_joined
#             Hiển thị final_id
#
#         Trường hợp "3": Ẩn số điện thoại
#             NẾU chưa nhập dữ liệu ở Chức năng 1 -> Báo lỗi thiếu dữ liệu
#             NẾU KHÔNG:
#                 Kiểm tra SĐT người gửi và người nhận qua 3 bước:
#                     1. Nếu len == 0 -> Báo lỗi rỗng
#                     2. Nếu không .isdigit() -> Báo lỗi chứa chữ/ký tự đặc biệt
#                     3. Nếu len != 10 -> Báo lỗi không đủ 10 số
#                 Nếu hợp lệ: Cắt chuỗi lấy 3 số đầu + "*****" + 2 số cuối -> Hiển thị
#
#         Trường hợp "4": Tìm kiếm & Thay thế từ khóa
#             Nhập find_key, replace_key
#             Đếm số lần xuất hiện: count_appear = note.count(find_key)
#             NẾU count_appear > 0:
#                 new_note = note.replace(find_key, replace_key)
#                 Hiển thị count_appear và new_note
#                 Cập nhật note = new_note
#             NẾU KHÔNG:
#                 Hiển thị thông báo không tìm thấy từ khóa
#
#         Trường hợp "5": Thoát chương trình
#             Hiển thị "Thoát chương trình"
#             Dừng vòng lặp (break)
#
#         Trường hợp còn lại (_):
#             Hiển thị "Lựa chọn không hợp lệ!"
# KẾT THÚC (END)


# III. CHƯƠNG TRÌNH CHÍNH 

while True:
    print("""
+====================================================================+
|             HỆ THỐNG QUẢN LÝ NỘI DUNG ĐƠN HÀNG GRAB                |
+====================================================================+
|   1. Nhập dữ liệu đơn hàng và xem báo cáo thống kê                 |
|   2. Chuẩn hóa mã đơn hàng                                         |
|   3. Ẩn số điện thoại khách hàng                                   |
|   4. Tìm kiếm và thay thế từ khóa trong ghi chú giao hàng          |
|   5. Thoát chương trình                                            |
+====================================================================+
""")
    choice = input('> Mời bạn chọn chức năng (1 - 5): ')

    match choice:
        case "1":

            name_sender = input('Nhập tên người gửi: ')
            phone_sender = input('Nhập số điện thoại người gửi: ')
            address_sender = input('Nhập địa chỉ lấy hàng: ')
            name_receiver = input('Nhập tên người nhận: ')
            phone_receiver = input('Nhập số điện thoại người nhận: ')
            address_receiver = input('Nhập địa chỉ giao hàng: ')
            note = input('Nhập ghi chú giao hàng: ')

            print("\n--- BÁO CÁO THỐNG KÊ ĐƠN HÀNG ---")
            print(f'- Tên người gửi: {name_sender.strip().title()}')
            print(f'- Tên người nhận: {name_receiver.strip().title()}')

            print(f'- Địa chỉ lấy hàng: {" ".join(address_sender.split())}')
            print(f'- Địa chỉ giao hàng: {" ".join(address_receiver.split())}')

            note_clean = note.strip()
            print(f'- Ghi chú giao hàng: {note_clean}')
            print(f'- Độ dài ghi chú giao hàng: {len(note_clean)}')
            
            words_in_note = len(note_clean.split())
            print(f'- Số lượng từ trong ghi chú: {words_in_note}')
            
            print(f'- Ghi chú dạng chữ thường: {note_clean.lower()}')
            print(f'- Ghi chú dạng chữ hoa: {note_clean.upper()}')

        case "2":
            print("\n--- CHỨC NĂNG 2: CHUẨN HÓA MÃ ĐƠN HÀNG ---")
            order_id = input('Nhập mã đơn hàng cần chuẩn hóa: ')

            original_id = order_id
            
            id_split = order_id.upper().split()
            
            id_joined = "-".join(id_split)
            
            if id_joined.startswith("GRAB-"):
                final_id = id_joined
            else:
                final_id = "GRAB-" + id_joined
                
            print(f'Mã đơn hàng ban đầu: "{original_id}"')
            print(f'Mã đơn hàng sau khi được chuẩn hóa: "{final_id}"')

        case "3":
            print("\n--- CHỨC NĂNG 3: ẨN SỐ ĐIỆN THOẠI KHÁCH HÀNG ---")
            
            if 'phone_sender' not in locals() or 'phone_receiver' not in locals():
                print("Lỗi: Vui lòng chạy Chức năng 1 để nhập thông tin SĐT trước!")
            else:
                
                if len(phone_sender) == 0:
                    print("SĐT người gửi: KHÔNG hợp lệ (Không được để rỗng)")
                elif not phone_sender.isdigit():
                    print("SĐT người gửi: KHÔNG hợp lệ (Chỉ được chứa chữ số)")
                elif len(phone_sender) != 10:
                    print("SĐT người gửi: KHÔNG hợp lệ (Phải có đúng 10 ký tự)")
                else:
                    hidden_sender = phone_sender[0:3] + "*****" + phone_sender[8:10]
                    print(f"SĐT người gửi: {hidden_sender}")
                    

                if len(phone_receiver) == 0:
                    print("SĐT người nhận: KHÔNG hợp lệ (Không được để rỗng)")
                elif not phone_receiver.isdigit():
                    print("SĐT người nhận: KHÔNG hợp lệ (Chỉ được chứa chữ số)")
                elif len(phone_receiver) != 10:
                    print("SĐT người nhận: KHÔNG hợp lệ (Phải có đúng 10 ký tự)")
                else:
                    hidden_receiver = phone_receiver[0:3] + "*****" + phone_receiver[8:10]
                    print(f"SĐT người nhận: {hidden_receiver}")
            print("------------------------------------------------")

        case "4":
            print("\n--- CHỨC NĂNG 4: TÌM KIẾM VÀ THAY THẾ TỪ KHÓA ---")
            
          
            if 'note' not in locals():
                note = input("Chưa có dữ liệu ghi chú. Vui lòng nhập ghi chú đơn hàng hiện tại: ")
            else:
                print(f"Ghi chú đơn hàng hiện tại:\n{note}")

            find_key = input('Nhập từ khóa cần tìm: ')
            replace_key = input('Nhập từ khóa thay thế: ')

            
            count_appear = note.count(find_key)

           
            if count_appear > 0:
                new_note = note.replace(find_key, replace_key)
                note = new_note 
                
                print(f'Số lần xuất hiện của từ khóa: {count_appear}')
                print(f'Ghi chú đơn hàng sau khi thay thế:\n{new_note}')
            else:
                print(f'Thông báo: Từ khóa "{find_key}" không tồn tại trong ghi chú đơn hàng.')
        case "5":
            print('Thoát chương trình.')
            break
            
        case _:
            print("Lựa chọn không hợp lệ! Vui lòng chọn lại từ 1 đến 5.")
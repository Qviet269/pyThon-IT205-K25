# 1. INPUT / OUTPUT:
#   - Input: 
#     + order_list: Mảng tĩnh List[str] dạng chuỗi phối hợp "MÃ - TRẠNG_THÁI".
#     + choice / mini_choice: Chuỗi ký tự số (str) điều hướng chức năng hệ thống.
#     + order_id, status, new_code, new_status, pos_input, index_del: Chuỗi dữ liệu thô nhập tự do từ console.
#   - Output: Giao diện phân tầng (Menu chính / Menu con), dữ liệu hiển thị có index định dạng, 
#             báo cáo thống kê số liệu và thông báo lỗi phản hồi nghiệp vụ.

# 2. ĐỀ XUẤT GIẢI PHÁP & XỬ LÝ BẪY (EDGE CASES):
#   - Đồng nhất dữ liệu: Áp dụng hàm kết hợp '.strip().upper()' loại bỏ khoảng trắng thừa đầu cuối và chữ thường.
#   - Kiểm soát ngoại lệ Index: Sử dụng điều kiện '.isdigit()' (phải có dấu ngoặc hàm) lọc sạch dữ liệu dạng chữ ký tự đặc biệt.
#     Chuyển đổi cận từ hiển thị thực tế (bắt đầu từ 1) sang chỉ số kỹ thuật Python bằng phép toán (vị trí - 1). Chặn biên an toàn 
#     bằng biểu thức so sánh logic '0 <= idx < len(order_list)' loại bỏ hoàn toàn lỗi dừng chương trình đột ngột (IndexError).
#   - Duy trì luồng lặp phân cấp: Thiết lập vòng lặp lồng cấu trúc, dùng lệnh 'break' tại nhánh thoát menu con để tự động chuyển tiếp về menu gốc.

# 3. THIẾT KẾ THUẬT TOÁN THỐNG KÊ (MÔ TẢ LUỒNG):
#   - Bước 1: Khởi tạo 4 bộ đếm tích lũy bằng số nguyên (int): pending, delivering, completed, cancelled bằng giá trị 0.
#   - Bước 2: Sử dụng vòng lặp duyệt tuần tự 'for i, v in enumerate(order_list):' để bóc tách từng chuỗi đơn hàng ra xử lý.
#   - Bước 3: Kiểm tra cấu trúc chuỗi có chứa chuỗi phân cách lý tưởng " - ". Nếu thỏa mãn, thực thi phương thức '.split(' - ')'.
#   - Bước 4: Trích xuất chuỗi trạng thái ở chỉ số mảng cắt thứ hai (phần tử [1]), loại bỏ khoảng trắng nếu có bằng '.strip()'.
#   - Bước 5: Sử dụng các khối rẽ nhánh điều kiện 'if-elif' để so khớp chính xác chuỗi trạng thái với các từ khóa tiêu chuẩn 
#             (PENDING, DELIVERING, COMPLETED, CANCELLED) và tăng giá trị biến đếm tương ứng lên 1 đơn vị.
#   - Bước 6: In kết xuất các thông số đếm được và tính tổng lượng đơn hàng bằng hàm đo độ dài 'len(order_list)'.

order_list = [
    "GE001 - PENDING",
    "GE002 - DELIVERING",
    "GE003 - CANCELLED"
]

while True:
    print("""
===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAP EXPRESS =====
    1. Hiển thị danh đơn hàng 
    2. Cập nhật danh sách đơn hàng
    3. Thống kê đơn hàng theo trạng thái
    4. Thoát chương trình
""")
    
    choice = input('Lựa chọn của bạn (1-4): ')

    match choice:
        case "1":
            if len(order_list)  > 0:
                for i, v in enumerate(order_list, 1):
                    print(f'{i}. {v}')
            else:
                print('Danh sách đơn hàng hiện đang trống!')
            
        case "2":
            while True:
                print("""
-----CẬP NHẬT DANH SÁCH ĐƠN HÀNG-----
    1. Thêm đơn hàng mới
    2. Sửa đơn hàng theo vị trí
    3. Xóa đơn hàng theo vị trí
    4. Quay lại menu chính
""")
                mini_choice = input('Lựa chọn của bạn (1-4): ')
                match mini_choice:
                    case "1":
                        order_id = input('Nhập mã đơn hàng: ').strip().upper()
                        status = input('Nhập trong thái: ').strip().upper()

                        update_oder = f'{order_id} - {status}'
                        order_list.append(update_oder)
                        print("Đã thêm vào thành công!")

                    case "2":
                        pos_input = input("Nhập vị trí đơn hàng cần sửa: ").strip()
                        if pos_input.isdigit():
                            idx = int(pos_input)
                            idx = idx - 1
                            if 0 <= idx < len(order_list):
                                new_code = input("Nhập mã đơn hàng mới: ").strip().upper()
                                new_status = input("Nhập trạng thái mới: ").strip().upper()
                                order_list[idx] = f"{new_code} - {new_status}"
                                print(f"Đã cập nhật")
                            else:
                                print("Không tồn tại đơn hàng!")
                        else:
                            print("Vị trí không hợp lệ!")
                        
                    case "3":
                        index_del = input('Nhập vị trí cần xóa: ').strip()
                        
                        if index_del.isdigit():
                            idx = int(index_del)
                            idx = idx - 1
                            if 0 <= idx < len(order_list):
                                pop_index = order_list.pop(idx)
                                print(f'Đơn hàng vừa bị xóa {pop_index}')
                            else:
                                print('Không tồn tại vị trí đơn hàng này')
                        else:
                            print('Không tồn tại đơn hàng')
                    case "4":
                        break
                    case _:
                        print('Lựa chọn không hợp lệ!')
        case "3":
            pending = 0
            delivering = 0
            cancelled = 0
            completed = 0

            for i, v in enumerate(order_list):
                if " - " in v:
                    item = v.split(' - ')
                    status = item[1].strip()

                    if status == "PENDING":
                        pending += 1
                    elif status == "DELIVERING":
                        delivering += 1
                    elif status == "COMPLETED":
                        completed += 1
                    elif status == "CANCELLED":
                        cancelled += 1
                    
            print("\n===== THỐNG KÊ ĐƠN HÀNG =====")
            print(f"PENDING: {pending}")
            print(f"DELIVERING: {delivering}")
            print(f"COMPLETED: {completed}")
            print(f"CANCELLED: {cancelled}")
            print(f"Tổng số đơn hàng: {len(order_list)}")
            
        case "4":
            print('Thoát chương trình1')
            break
        case _:
            print('Lựa chọn không hợp lệ')
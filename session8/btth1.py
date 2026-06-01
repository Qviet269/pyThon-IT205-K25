"""
1. Phân tích Input / Output
Menu chương trình:

Input: Biến choice (Kiểu chuỗi str, nhập từ bàn phím).

Output: Chạy chức năng tương ứng (1, 2, 3, 4, 5) hoặc báo lỗi nếu chọn sai.

Chức năng 1 (Nhập và phân tích):

Input: account_name, title, description, list_hashtag (Tất cả đều là kiểu chuỗi str).

Output: In ra thông tin đã xử lý sạch khoảng trắng, viết hoa/thường, độ dài chữ, số lượng từ và số lượng hashtag.

Chức năng 2 (Chuẩn hóa tài khoản):

Input: Biến account_name đã nhập từ Chức năng 1.

Output: Chuỗi tài khoản mới có thêm chữ @ ở đầu và viết thường hết.

Chức năng 3 (Kiểm tra hashtag):

Input: Biến new_hashtag (Kiểu chuỗi str, nhập từ bàn phím).

Output: Thông báo xem hashtag có hợp lệ không (rỗng, thiếu dấu #, chứa khoảng trắng...). Nếu đúng thì cộng dồn vào chuỗi list_hashtag cũ.

Chức năng 4 (Tìm và thay thế):

Input: Từ khóa cần tìm find_word, từ khóa thay thế replace_word và chuỗi description.

Output: Chuỗi mô tả mới sau khi đổi chữ và số lần tìm thấy từ khóa đó.

Chức năng 5 (Thoát):

Output: In ra chữ "Thoát!" và dừng hẳn chương trình.

2. Đề xuất giải pháp xử lý
Luồng chạy chính: Dùng vòng lặp while True để giữ chương trình chạy liên tục. Dùng cấu trúc match case để bắt đúng lựa chọn từ "1" đến "5" của người dùng.

Xử lý văn bản (Chuỗi): * Dùng hàm .strip() để tự động xóa khoảng trắng thừa ở đầu và cuối.

Dùng .title() để viết hoa chữ cái đầu của mỗi từ (áp dụng cho tiêu đề).

Dùng .upper() để chuyển toàn bộ thành chữ HOA và .lower() để chuyển thành chữ thường.

Đếm số lượng và Thay thế: * Dùng .count() để đếm xem ký tự khoảng trắng hoặc từ khóa xuất hiện bao nhiêu lần.

Dùng .replace() để tìm và đổi từ cũ thành từ mới.


3. Thiết kế thuật toán

VÒNG LẶP VÔ HẠN:
    HIỂN THỊ Menu (1-5)
    NHẬP choice
    KIỂM TRA choice:
        Case "1":
            NHẬP account_name, title, description, list_hashtag
            IN chuỗi sau khi xử lý bằng .strip(), .title(), .upper(), .lower()
            TÍNH số từ = description.count(" ") + 1
            TÍNH số hashtag = số lượng phần tử sau khi .split(",")
        Case "2":
            IN tài khoản chuẩn hóa: "@" + account_name.lower()
        Case "3":
            NHẬP new_hashtag
            NẾU rỗng HOẶC không bắt đầu bằng '#' HOẶC chứa ' ' HOẶC độ dài < 2 THÌ:
                IN thông báo lỗi tương ứng
            NGƯỢC LẠI:
                list_hashtag = list_hashtag + new_hashtag
        Case "4":
            NẾU description rỗng THÌ: Quay lại đầu vòng lặp (continue)
            NHẬP find_word, replace_word
            NẾU find_word có trong description THÌ:
                count_word = description.count(find_word)
                description = description.replace(find_word, replace_word)
                IN description mới và count_word
            NGƯỢC LẠI: IN "Không tìm thấy"
        Case "5":
            Thoát vòng lặp (break)
        Trường hợp khác:
            IN "Lựa chọn không hợp lệ!"
"""

while True:
    print("===Hệ thống quản lý nội dung tiktok===")
    print("1. Nhập và phân tích thông tin video")
    print("2. Chuẩn hóa tên tài khoản")
    print("3. Kiểm tra tính hợp lệ của hashtag")
    print("4. Tìm kiếm và thay thế từ khóa trong mô tả")
    print("5. Thoát!")

    choice = input("Nhập lựa chọn của bạn: ")
    match choice:
        case "1":
            account_name = input("Nhập vào tên tài khoản: ")
            title = input("Nhập vào tiêu đề: ")
            description = input("Nhập vào mô tả: ")
            list_hashtag = input("Nhập vào ds hashtag: ")

            print(f"Tên tài khoản: {account_name.strip()}")
            print(f"Tiêu đề: {title.title().strip()}")
            print(f"Mô tả: {description.strip()}")
            print(f"Độ dài mô tả trong video: {len(description)}")
            # "Hôm nay tôi vui"  => ["Hôm", "nay", "tôi", "vui"] dùng split()
            # "Hôm nay tôi vui" => dùng count để đếm số khoảng trắng trong chuỗi
            count_space = description.count(" ")
            print(f"Số lượng từ trong mô tả: {count_space + 1}")
            
            temp_list = list_hashtag.split(",") 
            new_list_hashtag = "".join(temp_list) 
            print(f"Danh sách hashtag sau khi chuẩn hóa khoảng trắng: {new_list_hashtag.strip()}")
            count_hashtag = list_hashtag.split(",")
            print(f"Số lượng hashtag: {len(count_hashtag)}")
            print(f"Mô tả video chuyển thành chữ hoa {description.upper()}")
            print(f"Mô tả video chuyển thành chữ thường {description.lower()}")
        case "2":
            print(f"Tên tài khoản ban đầu: {account_name}")
            print(f"Tên tài khoản được chuẩn hóa:  @{account_name.lower()}")
        case "3":
            new_hashtag = input("Nhập vào hashtag mới: ")
            if (len(new_hashtag) == 0):
                print("Không được rỗng!")
            elif (not new_hashtag.startswith("#")):
                print("Phải bắt đầu bằng dấu #")
            elif (" " in new_hashtag):
                print('Không được chưa khoảng trắng')
            elif (len(new_hashtag) < 2):
                print("Hashtag không được bé hơn 2 kí tự")
            else:
                print("Hashtag hợp lệ!")
                list_hashtag = list_hashtag + new_hashtag
                print(f"Danh sách hashtag mới {list_hashtag}")
        case "4":
            if 'description' not in locals() or not description:
                print("Mô tả video đang rỗng! Vui lòng chọn chức năng 1 để nhập dữ liệu trước.")
                continue

            find_word = input("Nhập vào từ khóa cần tìm: ")
            replace_word = input("Nhập vào từ khóa cần thay thế: ")

            if find_word in description:
                
                count_word = description.count(find_word)
                
                
                description = description.replace(find_word, replace_word)
                
               
                print("-> Đã tìm thấy và thay thế từ khóa thành công!")
                print(f"Mô tả sau khi thay thế: {description}")
                print(f"Số lượng từ tìm được là: {count_word}")
            else:
               
                print(f"Không tìm thấy từ khóa '{find_word}' trong mô tả video.")
        case "5":
            print("Thoát!")
            break
        case _:
            print("Lựa chọn không hợp lệ!")
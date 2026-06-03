

# 1. INPUT / OUTPUT
# - Input:
#   + playlist: Kiểu List[str] lưu tên các bài hát.
#   + main_choice / sub_choice: Kiểu str nhận diện lựa chọn menu.
#   + song_name / pos_input: Kiểu str nhập dữ liệu thô cho bài hát và vị trí.
# - Output: Giao diện menu phân cấp, danh sách bài hát có index, dữ liệu trích xuất dạng slice, thông báo lỗi.

# 2. ĐỀ XUẤT GIẢI PHÁP KỸ THUẬT & BẪY DỮ LIỆU (EDGE CASES)
# - Quản lý menu: Dùng vòng lặp 'while True' lồng nhau, thoát menu con bằng lệnh 'break'.
# - Bẫy 1 (Mảng rỗng): Kiểm tra điều kiện 'if not playlist:' đầu case 2, 3, 4 để chặn lỗi xử lý mảng trống.
# - Bẫy 2 (Xóa bài trùng/sai tên): Dùng toán tử 'in' check tồn tại trước khi gọi hàm '.remove()' tránh crash.
# - Bẫy 3 & 4 (Nhập sai vị trí/nhập chữ):
#   + Chặn nhập ký tự lạ, chữ bằng hàm '.isdigit()'.
#   + Chuyển vị trí thực tế về chỉ số mảng: index = vị_trí - 1.
#   + Biên an toàn cho chèn bài: 0 <= index <= len(playlist) (dùng hàm .insert).
#   + Biên an toàn cho xóa bài: 0 <= index < len(playlist) (dùng hàm .pop).

# 3. THIẾT KẾ THUẬT TOÁN (LUỒNG CHẠY CHÍNH)
# Khởi tạo playlist = []
# Vòng lặp chính (Menu tổng từ 1-5):
#   - Chọn "1" (Thêm): Menu phụ -> 1. Dùng .append() thêm cuối / 2. Dùng .insert() chèn theo index.
#   - Chọn "2" (Xem): Nếu mảng trống -> Báo lỗi. Ngược lại -> Duyệt mảng bằng 'enumerate(playlist, 1)' in ra dạng "Số_TT. Tên_bài".
#   - Chọn "3" (Xóa): Nếu mảng trống -> Báo lỗi. Ngược lại -> Menu phụ -> 1. Xóa bằng .remove(tên) / 2. Xóa bằng .pop(index).
#   - Chọn "4" (Sắp xếp/Trích xuất): Menu phụ -> 1. Dùng .sort() sắp xếp A-Z / 2. Dùng cú pháp cắt mảng 'playlist[:3]' lấy 3 bài đầu.
#   - Chọn "5" (Thoát): In thông báo và gọi 'break' dừng toàn bộ chương trình.
#   - Nhập sai format khác (_): In cảnh báo nhập lại.


playlist = []

while True:
    print("""
===== HỆ THỐNG QUẢN LÝ PLAYLIST GRAB MUSIC =====
1. Thêm bài hát vào danh sách phát
2. Xem danh sách phát
3. Xóa bài hát khỏi danh sách
4. Sắp xếp và Trích xuất danh sách
5. Thoát chương trình
""")
    main_choice = input("Lựa chọn của bạn (1-5): ").strip()

    if main_choice == "1":
        while True:
            print("""
--- CHỨC NĂNG THÊM BÀI HÁT ---
1. Thêm bài hát vào cuối danh sách
2. Chèn bài hát vào vị trí bất kỳ
3. Quay lại menu chính
""")
            sub_choice = input("Lựa chọn của bạn (1-3): ").strip()

            if sub_choice == "1":
                song_name = input("Nhập tên bài hát muốn thêm: ").strip()
                if song_name:
                    playlist.append(song_name)
                    print(f"-> Đã thêm thành công bài hát '{song_name}' vào cuối danh sách.")
                    print(f"-> Số lượng bài hát hiện tại trong playlist: {len(playlist)}")
                else:
                    print("Tên bài hát không được để trống!")

            elif sub_choice == "2":
                song_name = input("Nhập tên bài hát muốn chèn: ").strip()
                if song_name:
                    pos_input = input("Nhập số thứ tự muốn chèn (bắt đầu từ 1): ").strip()
                    # Bẫy 3 & 4: Kiểm tra vị trí hợp lệ
                    if pos_input.isdigit():
                        pos = int(pos_input)
                        idx = pos - 1
                        # Cho phép chèn từ vị trí 1 đến độ dài mảng + 1
                        if 0 <= idx <= len(playlist):
                            playlist.insert(idx, song_name)
                            print(f"-> Đã chèn thành công bài hát '{song_name}' vào vị trí số {pos}.")
                            print(f"-> Số lượng bài hát hiện tại trong playlist: {len(playlist)}")
                        else:
                            print("Vị trí không hợp lệ (Vượt quá giới hạn danh sách)!")
                    else:
                        print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên dương!")
                else:
                    print("Tên bài hát không được để trống!")

            elif sub_choice == "3":
                break
            else:
                print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên từ 1 đến 3!")

    elif main_choice == "2":
        # Bẫy 1: Thao tác với danh sách trống
        if not playlist:
            print("Danh sách phát hiện đang trống!")
        else:
            print("\n===== DANH SÁCH PHÁT HIỆN TẠI =====")
            for i, song in enumerate(playlist, 1):
                print(f"{i}. {song}")

    elif main_choice == "3":
        # Bẫy 1: Kiểm tra mảng rỗng trước khi xử lý xóa
        if not playlist:
            print("Danh sách phát hiện đang trống!")
            continue

        while True:
            print("""
--- CHỨC NĂNG XÓA BÀI HÁT ---
1. Xóa bài hát theo tên
2. Xóa bài hát theo vị trí (số thứ tự)
3. Quay lại menu chính
""")
            sub_choice = input("Lựa chọn của bạn (1-3): ").strip()

            if sub_choice == "1":
                song_name = input("Nhập chính xác tên bài hát cần xóa: ").strip()
                # Bẫy 2: Xóa bài hát không tồn tại
                if song_name in playlist:
                    playlist.remove(song_name)
                    print(f"-> Đã xóa bài hát '{song_name}' khỏi danh sách.")
                else:
                    print("Không tìm thấy bài hát trong danh sách phát.")

            elif sub_choice == "2":
                pos_input = input("Nhập số thứ tự bài hát cần xóa (bắt đầu từ 1): ").strip()
                # Bẫy 3 & 4: Kiểm tra định dạng số và giới hạn biên
                if pos_input.isdigit():
                    pos = int(pos_input)
                    idx = pos - 1
                    if 0 <= idx < len(playlist):
                        deleted_song = playlist.pop(idx)
                        print(f"-> Đã xóa bài hát '{deleted_song}' tại vị trí số {pos} khỏi danh sách.")
                    else:
                        print("Vị trí không hợp lệ (Vượt quá giới hạn danh sách)!")
                else:
                    print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên dương!")

            elif sub_choice == "3":
                break
            else:
                print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên từ 1 đến 3!")

    elif main_choice == "4":
        # Bẫy 1: Kiểm tra mảng rỗng trước khi sắp xếp/trích xuất
        if not playlist:
            print("Danh sách phát hiện đang trống!")
            continue

        while True:
            print("""
--- SẮP XẾP VÀ TRÍCH XUẤT ---
1. Sắp xếp danh sách phát theo thứ tự chữ cái (A-Z)
2. Nghe thử (Trích xuất 3 bài hát đầu tiên)
3. Quay lại menu chính
""")
            sub_choice = input("Lựa chọn của bạn (1-3): ").strip()

            if sub_choice == "1":
                playlist.sort()
                print("-> Đã sắp xếp lại danh sách phát theo thứ tự bảng chữ cái (A-Z) thành công.")

            elif sub_choice == "2":
                print("\n--- NGHE THỬ 3 BÀI HÁT ĐẦU TIÊN ---")
                # Trích xuất dữ liệu bằng cơ chế List Slicing
                preview_list = playlist[:3]
                for i, song in enumerate(preview_list, 1):
                    print(f"Nghe thử {i}: {song}")
                if len(playlist) < 3:
                    print(f"(Playlist chỉ có {len(playlist)} bài, hiển thị tối đa số bài hiện có)")

            elif sub_choice == "3":
                break
            else:
                print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên từ 1 đến 3!")

    elif main_choice == "5":
        print("Cảm ơn bạn đã sử dụng dịch vụ. Tạm biệt!")
        break

    else:
        # Bẫy 4: Người dùng nhập sai định dạng lựa chọn menu chính
        print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên")
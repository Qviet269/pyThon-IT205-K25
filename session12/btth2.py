# ==========================================
# 1. PHÂN TÍCH INPUT/OUTPUT & LOGIC NGHIỆP VỤ
# ==========================================
# - Cấu trúc dữ liệu: List chứa các Dict quản lý sổ tiết kiệm (ID, Tên, Tiền gửi, Kỳ hạn, Lãi suất, Trạng thái).
# - Input đầu vào: Nhận chuỗi từ bàn phím -> Chuẩn hóa bằng .strip().upper().
# - Kiểm tra lỗi (Validation): Dùng try-except ValueError để lọc các bẫy nhập chữ/ký tự đặc biệt.
# - Ràng buộc số: Kiểm tra điều kiện (> 0) cho tiền gửi, kỳ hạn, lãi suất và số tháng thực gửi.
# - Ràng buộc nghiệp vụ: Check trùng mã khi thêm mới; Check tồn tại và trạng thái "active" khi sửa/tính lãi/rút trước hạn.
# - Công thức tính lãi: Tiền lãi = Số tiền * (Lãi suất / 100) * (Số tháng / 12).

# ==========================================
# 2. THIẾT KẾ THUẬT TOÁN (PSEUDOCODE)
# ==========================================
# Bước 1: Khởi chạy vòng lặp vô hạn (while True) hiển thị Menu 7 chức năng.
# Bước 2: Nhận lựa chọn từ người dùng. Nếu ngoài phạm vi 1-7 hoặc sai định dạng -> Báo lỗi, quay lại Menu.
# Bước 3: Rẽ nhánh xử lý từng chức năng (if-elif-else):
#   - Chức năng 1 (Xem): Duyệt danh sách bằng vòng lặp. Nếu rỗng -> Báo trống. Ngược lại -> In chuỗi định dạng.
#   - Chức năng 2 (Mở): Quét trùng ID -> Check tên trống -> Ép kiểu & check số dương (>0) -> Lưu dict mới vào list.
#   - Chức năng 3 (Sửa): Quét tìm ID -> Check trạng thái 'closed' -> Nhập và xác thực thông tin mới -> Ghi đè vào dict.
#   - Chức năng 4 (Tất toán): Quét tìm ID -> Cập nhật trường 'status' = 'closed'.
#   - Chức năng 5 (Tính lãi gốc): Quét tìm ID & check 'closed' -> Áp dụng công thức tính lãi theo kỳ hạn gốc -> In kết quả.
#   - Chức năng 6 (Rút trước hạn): Quét tìm ID & check 'closed' -> Nhập số tháng thực tế.
#       + Nếu tháng thực tế < kỳ hạn gốc: Áp dụng lãi suất phạt 0.5%/năm.
#       + Nếu tháng thực tế >= kỳ hạn gốc: Giữ nguyên lãi suất gốc của sổ.
#       + Tính lãi thực nhận theo số tháng thực tế và lãi suất tương ứng -> In kết quả.
#   - Chức năng 7 (Thoát): Bẻ gãy vòng lặp (break) để dừng chương trình.



# Khởi tạo dữ liệu mẫu ban đầu
saving_accounts = [
    {
        "account_id": "STK001",
        "customer_name": "Nguyễn Văn An",
        "balance": 50000000,
        "term_months": 6,
        "interest_rate": 6.5,
        "status": "active"
    },
    {
        "account_id": "STK002",
        "customer_name": "Trần Thị Bình",
        "balance": 120000000,
        "term_months": 12,
        "interest_rate": 7.2,
        "status": "active"
    }
]

while True:
    # Hiển thị Menu CLI
    print("\n===== HỆ THỐNG QUẢN LÝ TÀI KHOẢN TIẾT KIỆM TECHBANK =====")
    print("1. Xem danh sách sổ tiết kiệm")
    print("2. Mở sổ tiết kiệm mới")
    print("3. Cập nhật thông tin sổ tiết kiệm")
    print("4. Tất toán hoặc xóa sổ tiết kiệm")
    print("5. Tính lãi dự kiến khi đến hạn")
    print("6. Kiểm tra điều kiện rút trước hạn")
    print("7. Thoát chương trình")
    
    choice = input("Nhập lựa chọn của bạn (1-7): ").strip()
    
    # Bẫy 8 — Menu Validation
    if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại")
        continue
        
    # CHỨC NĂNG 1: Xem danh sách sổ tiết kiệm
    if choice == "1":
        if not saving_accounts:
            print("Danh sách sổ tiết kiệm hiện đang trống")
        else:
            print("Danh sách sổ tiết kiệm:")
            for index, acc in enumerate(saving_accounts, start=1):
                print(f"{index}. Mã sổ: {acc['account_id']} | Khách hàng: {acc['customer_name']} | "
                      f"Số tiền gửi: {acc['balance']} | Kỳ hạn: {acc['term_months']} tháng | "
                      f"Lãi suất: {acc['interest_rate']}%/năm | Trạng thái: {acc['status']}")
                      
    # CHỨC NĂNG 2: Mở sổ tiết kiệm mới
    elif choice == "2":
        account_id = input("Nhập mã sổ tiết kiệm: ").strip().upper()
        
        # Bẫy 1 — Mở sổ tiết kiệm với mã bị trùng
        id_exists = False
        for acc in saving_accounts:
            if acc["account_id"] == account_id:
                id_exists = True
                break
        if id_exists:
            print("Mã sổ tiết kiệm đã tồn tại!")
            continue
            
        customer_name = input("Nhập tên khách hàng: ").strip()
        # Bẫy 2 — Tên khách hàng bị bỏ trống
        if not customer_name:
            print("Tên khách hàng không được để trống")
            continue
            
        balance_input = input("Nhập số tiền gửi: ").strip()
        term_input = input("Nhập kỳ hạn gửi theo tháng: ").strip()
        
        # Bẫy 3 — Số tiền gửi hoặc kỳ hạn không hợp lệ
        try:
            balance = int(balance_input)
            term_months = int(term_input)
            if balance <= 0 or term_months <= 0:
                print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                continue
        except ValueError:
            print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
            continue
            
        rate_input = input("Nhập lãi suất năm: ").strip()
        # Bẫy 4 — Lãi suất không hợp lệ
        try:
            interest_rate = float(rate_input)
            if interest_rate <= 0:
                print("Lãi suất không hợp lệ!")
                continue
        except ValueError:
            print("Lãi suất không hợp lệ!")
            continue
            
        # Thêm sổ tiết kiệm mới hợp lệ vào hệ thống
        new_account = {
            "account_id": account_id,
            "customer_name": customer_name,
            "balance": balance,
            "term_months": term_months,
            "interest_rate": interest_rate,
            "status": "active"
        }
        saving_accounts.append(new_account)
        print("Mở sổ tiết kiệm mới thành công!")
        
    # CHỨC NĂNG 3: Cập nhật thông tin sổ tiết kiệm
    elif choice == "3":
        account_id = input("Nhập mã sổ tiết kiệm cần cập nhật: ").strip().upper()
        
        # Tìm kiếm tài khoản dựa trên mã sổ
        found_account = None
        for acc in saving_accounts:
            if acc["account_id"] == account_id:
                found_account = acc
                break
                
        # Bẫy 5 — Cập nhật với mã không tồn tại
        if not found_account:
            print("Không tìm thấy mã sổ tiết kiệm")
            continue
            
        # Bẫy 6 — Thao tác trên sổ đã tất toán
        if found_account["status"] == "closed":
            print("Không thể thao tác với sổ tiết kiệm đã tất toán")
            continue
            
        # Thu thập dữ liệu cập nhật mới
        new_name = input("Nhập tên khách hàng mới: ").strip()
        if not new_name:
            print("Tên khách hàng không được để trống")
            continue
            
        new_balance_input = input("Nhập số tiền gửi mới: ").strip()
        new_term_input = input("Nhập kỳ hạn mới theo tháng: ").strip()
        
        try:
            new_balance = int(new_balance_input)
            new_term_months = int(new_term_input)
            if new_balance <= 0 or new_term_months <= 0:
                print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                continue
        except ValueError:
            print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
            continue
            
        new_rate_input = input("Nhập lãi suất năm mới: ").strip()
        try:
            new_interest_rate = float(new_rate_input)
            if new_interest_rate <= 0:
                print("Lãi suất không hợp lệ!")
                continue
        except ValueError:
            print("Lãi suất không hợp lệ!")
            continue
            
        # Cập nhật thông tin sau khi tất cả dữ liệu đầu vào hợp lệ
        found_account["customer_name"] = new_name
        found_account["balance"] = new_balance
        found_account["term_months"] = new_term_months
        found_account["interest_rate"] = new_interest_rate
        print("Cập nhật thông tin sổ tiết kiệm thành công!")
        
    # CHỨC NĂNG 4: Tất toán hoặc xóa sổ tiết kiệm
    elif choice == "4":
        account_id = input("Nhập mã sổ tiết kiệm cần tất toán/xóa: ").strip().upper()
        
        found_account = None
        for acc in saving_accounts:
            if acc["account_id"] == account_id:
                found_account = acc
                break
                
        if not found_account:
            print("Không tìm thấy mã sổ tiết kiệm")
            continue
            
        found_account["status"] = "closed"
        print(f"Tất toán thành công sổ tiết kiệm {account_id}. Trạng thái chuyển sang 'closed'.")
        
    # CHỨC NĂNG 5: Tính lãi dự kiến khi đến hạn
    elif choice == "5":
        account_id = input("Nhập mã sổ tiết kiệm cần tính lãi: ").strip().upper()
        
        found_account = None
        for acc in saving_accounts:
            if acc["account_id"] == account_id:
                found_account = acc
                break
                
        if not found_account:
            print("Không tìm thấy mã sổ tiết kiệm")
            continue
            
        if found_account["status"] == "closed":
            print("Không thể thao tác với sổ tiết kiệm đã tất toán")
            continue
            
        # Tính toán tiền lãi dự kiến và tổng nhận
        balance = found_account["balance"]
        interest_rate = found_account["interest_rate"]
        term_months = found_account["term_months"]
        
        interest = balance * interest_rate / 100 * term_months / 12
        total_received = balance + interest
        
        print(f"Tiền lãi dự kiến khi đến hạn: {interest:.2f}")
        print(f"Tổng tiền nhận khi đến hạn: {total_received:.2f}")
        
    # CHỨC NĂNG 6: Kiểm tra điều kiện rút trước hạn
    elif choice == "6":
        account_id = input("Nhập mã sổ tiết kiệm cần kiểm tra: ").strip().upper()
        
        found_account = None
        for acc in saving_accounts:
            if acc["account_id"] == account_id:
                found_account = acc
                break
                
        if not found_account:
            print("Không tìm thấy mã sổ tiết kiệm")
            continue
            
        if found_account["status"] == "closed":
            print("Không thể thao tác với sổ tiết kiệm đã tất toán")
            continue
            
        actual_months_input = input("Nhập số tháng thực gửi: ").strip()
        
        # Bẫy 7 — Số tháng thực gửi không hợp lệ
        try:
            actual_months = int(actual_months_input)
            if actual_months <= 0:
                print("Số tháng thực gửi không hợp lệ!")
                continue
        except ValueError:
            print("Số tháng thực gửi không hợp lệ!")
            continue
            
        balance = found_account["balance"]
        original_term = found_account["term_months"]
        
        # Xác định lãi suất áp dụng dựa trên số tháng thực gửi
        if actual_months < original_term:
            applied_rate = 0.5
            print("Khách hàng rút trước hạn. Áp dụng lãi suất không kỳ hạn: 0.5%/năm.")
        else:
            applied_rate = found_account["interest_rate"]
            print(f"Khách hàng đủ điều kiện hưởng lãi đúng hạn. Áp dụng lãi suất ban đầu: {applied_rate}%/năm.")
            
        # Tính toán theo công thức thực nhận
        interest_earned = balance * applied_rate / 100 * actual_months / 12
        total_earned = balance + interest_earned
        
        print(f"Tiền lãi thực nhận: {interest_earned:.2f}")
        print(f"Tổng tiền thực nhận: {total_earned:.2f}")
        
    # CHỨC NĂNG 7: Thoát chương trình
    elif choice == "7":
        print("Đã thoát chương trình quản lý tài khoản tiết kiệm. Tạm biệt!")
        break
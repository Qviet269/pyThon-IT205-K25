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

    print("""
====== HÊ THỐNG QUẢN LÝ TÀI KHOẢN TIẾT KIỆM TECHBANK ======
    1. Xem danh sách số tiết kiệm 
    2. Mở số tiết kiệm mới
    3. Cập nhật thông tin số tiết kiệm
    4. tất toán hoặc xóa số tiết kiệm
    5. tính lãi dự kiến khi đến hạn
    6. Kiếm tra điều kiện rút trước hạn
    7. Thoát chương trinh
""")
    choice = input('Mời bạn nhập lựa chọn (1-7): ')

    match choice:
        case "1":
            print("Danh sách số tiết kiệm:")
            
            print()
        case "2":
            print()
        case "3":
            print()
        case "4":
            print()
        case "5":
            print()
        case "6":
            print()
        case "7":
            print("Thoát chương trình!")
            break
        case _:
            print("Lựa chọn không hợp lệ!")
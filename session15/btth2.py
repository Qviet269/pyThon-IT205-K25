atm_vault_balance = 50000000
user_account_balance = 10000000

def menu():
    print("""
============== SMART ATM ===============
    1. Xem số dư
    2. Nạp tiền
    3. Rút tiền
    4. Kết thúc giao dịch
""")
def display_balances():
    global atm_vault_balance
    global user_account_balance
    print("---- SỐ DƯ TÀI KHOẢN ---")
    print(f"Tài khoản của bạn: {user_account_balance:,} VND")
    print(f"(Debug) Tiền mặt trong ATM: {atm_vault_balance:,} VND")

def validate (prompt):
    while True:
        try:
            data = int(input(prompt))

            if data <= 0:
                print("Số tiền không hợp lệ!")
            else:
                return data
        except:
            print("Bạn nhập không phải số!")

def deposit_money(amount):
    global user_account_balance
    global atm_vault_balance

    user_account_balance += amount
    print(f"Giao dịch thành công! Số dư tài khoản hiện tại: {user_account_balance:,} VND")
    return True

def  check_withdrawal_rules(amount):
    
    fee = 1100
    deducted = amount + fee

    if deducted > user_account_balance:
        return "INSUFFICIENT_FUNDS"
    elif amount > atm_vault_balance:
        return "ATM_OUT_OF_CASH"
    else:
        return "OK"



def main():
    global atm_vault_balance
    global user_account_balance
    while True:
        menu()
        choice = input("Vui lòng chọn giao dịch: ").strip()

        match choice:
            case "1":
                display_balances()
            case "2":
                print("--- NẠP TIỀN ---")
                amount = validate("Nhập số tiền muốn nạp: ")
                deposit_money(amount)
            case "3":

                print("--- Rút tiền ---")
                while True:
                    amount = validate("Nhập số tiền cần rút: ")
                    result = check_withdrawal_rules(amount)

                    if amount % 50000 != 0:
                        print("Số tiền rút phải là bội của 50,000")
                    elif result == "INSUFFICIENT_FUNDS":
                        print("Giao dịch thất bại: Số dư tài khoản không đủ.")
                    elif result == "ATM_OUT_OF_CASH":
                        print("Giao dịch thất bại: Máy ATM không đủ tiền mặt để phục vụ.")

                    elif result == "OK":
                        fee = 1100
                        deducted = amount + fee

                        atm_vault_balance -= amount
                        user_account_balance -= deducted
                        print("Giao dịch đang xử lý...")
                        print(f"Phí giao dịch: {fee:,} VND")
                        print(f"Bạn đã rút thành công {amount:,} VND")
                        print(f"Số dư tài khoản còn lại: {user_account_balance:,} VND")

            case "4":
                print("Cảm ơn quý khách đã sử dụng dịch vụ!")
                break
            case _:
                print("Lụa chọn không hợp lệ!")
main()
    
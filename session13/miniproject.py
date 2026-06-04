parking_lot = []



while True:

    print("""
==================================================
        QUẢN LÝ BÃI ĐẬU XE - SMART PARKING
==================================================
    1. Check-in (Đăng ký xe vào)
    2. Báo cáo tồn kho (Hiển thị danh sách)
    3. Tìm kiếm xe (Theo biển số)
    4. Check-out (Xử lý xe ra & Tính phí)
    5. Thoát chương trình
==================================================
""")
    choice = input("Nhập lựa chọn của bản (1-5): ")

    match choice:
        case "1":
            print("===== Check in =====")

            plate = input("Nhập biển số xe: ")

            if plate == "":
                print("Biển số không được để rỗng!")
                continue

            found = False

            for car in parking_lot:
                if car["plate"] == plate:
                    found= True
                    break
            if found == True:
                print("Xe với biển số xe đã tồn tại trong bãi!")
                continue

            type = int(input('Nhập loại xe (1. Xe máy, 2. Ô tô'))

            if type != 1 and type != 2:
                print('Loại xe không hơp lệ!')
                continue

            entry_time = int(input('Nhập giờ vào (0-24)h: '))

            if entry_time < 0 or entry_time > 24:
                print('giờ vào không hợp lệ!')
                continue

            car = {
                "plate": plate,
                "type": type,
                "entry_time": entry_time
            }

            parking_lot.append(car)

            print('Check in thành công!')

        case "2":
            print('\n====  Danh sách bãi xe =====')

            if len(parking_lot) == 0:
                print('Bãi xe hiện đang rỗng!')
                continue

            print(f"{'ID':<5}|{'Biển số':<15}|{'Loại xe':<15}|{'Giờ vào':<10}")
            for car in parking_lot:
                if car["type"] == 1:
                    car_name = 'Xe máy'
                else:
                    car_name = 'Ô tô'
                print(f"{car['ID']:<5}|{car['plate']:<15}|{car_name:<15}|{car["entry_time"]:<10}")
        case "3":
            print("\n==== tìm kiếm xe ====")

            if len(parking_lot) == 0:
                print('Bãi xe hiện tại đang rỗng!')
                continue

            search_plate = input('Nhập biển số cần tìm: ')

            flag = False

            for car in parking_lot:
                if search_plate == car["plate"]:
                    flag = True

                    print("=== Thông tin xe ===")

                    print(f"ID: {car["ID"]}| Biển SỐ: {car["plate"]}| Loại xe: {car_name}| Giờ vào: {car["entry_time"]}")
                    break
            if flag:
                print("Không tìm thấy")

        case "4":
            print("\n===== CHECK-OUT XE =====")

            if len(parking_lot) == 0:
                print("Bãi xe đang trống")
                continue

            plate = input("Nhập biển số cần check-out: ")

            found = False
            for car in parking_lot:

                if plate == car["plate"]:
                    found = True
                
                    exit_time = int(input("Nhập giờ ra: "))

                    # kiểm tra giờ ra
                    if exit_time < car["entry_time"]:
                        print("Giờ ra không hợp lệ")
                        break

                    # tính số giờ gửi
                    hours = exit_time - car["entry_time"]

                    # tính tiền
                    if car["type"] == 1:
                        total = hours * 5000
                    else:
                        total = hours * 10000

                    print("\n===== HÓA ĐƠN =====")

                    print("Biển số:", car["plate"])
                    print("Số giờ gửi:", hours)
                    print("Tổng tiền:", total, "VND")

                    # xóa xe khỏi bãi
                    parking_lot.remove(car)

                    print("Check-out thành công")

                    break

            if found == False:
                print("Không tìm thấy xe")
        case 5:
            print("Thoát chương trình!")
            break
        case _:
            print("Lựa chọn không hợp lệ")
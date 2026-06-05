staff_list = []
staff_id = 100

while True:
    print("""
===================================================
          QUẢN LÝ NHÂN SỰ - STAFF MANAGER
===================================================
    1. Thêm nhân viên mới
    2. Danh sách nhân viên
    3. Xóa nhân viên khỏi hệ thống
    4. thoát chương trinh
===================================================
""")
    
    choice = input("Nhập lựa chọn của bạn (1-5): ")

    match choice:
        case "1":
            if len(staff_list) == 0:
                new_id = 101
            else:
                new_id = staff_list[-1]["id"] + 1

            while True:
                name = input("nhập tên nhân viên: ")

                if name != "":
                    break
                else:
                    print('Tên không được để trống!')
            while True:
                salary = input("Nhập lương: ")
                try:
                    salary = float(salary)
                    if salary > 0:
                        break
                    else:
                        print("Lương phải lớn 0")
                except:
                    print("Lương không hợp lệ")
            staff = {
                'id': new_id,
                'name': name,
                'salary': salary                     
            }
            staff_list.append(staff)
        case "2":
            if len(staff_list) == 0:
                print('Phòng chưa có nhân sự!')
                break
            else:
                print(f"{'id':<5}|{'Tên nhân viên':<15}|{'Mức lương':<10}")
                for i, v in enumerate(staff_list):
                    print(f"{v['id']:<5}|{v['name']:<15}|{v['salary']:<10}")
            
        case "3":
            if len(staff_list) == 0:
                print("Chưa có nhân viên để xóa")

            else:

                delete_id = input("Nhập ID cần xóa: ")

                if delete_id.isdigit():

                    delete_id = int(delete_id)

                    found = False

                    for i, staff in enumerate(staff_list):

                        if staff["id"] == delete_id:

                            staff_list.remove(staff)

                            found = True

                            print("Đã xóa nhân viên thành công")

                            break

                    if found == False:
                        print("Không tìm thấy nhân viên")

                else:
                    print("ID không hợp lệ")
            print()
        case 4:
            print("Thoát chương trình!")
            break
        case  _:
            print("Lựa chọn không hợp lệ!")
#Yêu cầu tạo 1 menu 3 chức năng. Menu phải dùng hàm 
# Chức năng 1: Nhập sinh viên vào danh sách (Nhập số lượng sv rồi Nhập từng sinh viên vào)
# Chức năng 2: Hiển thị danh sách sinh viên ra màn hình
# Chắc năng 3: Tìm kiếm sinh viên theo tên (tìm đối tượng)
# Lưu ý: tất cả đều dùng hàm để gọi vào trong mỗi case


def menu():
    print("""
============== MENU ================
    1. Thêm Sinh viên
    2. Hiển thị danh sách
    3. Tìm kiếm sinh viên
====================================
""")
# ============================================================
def get_validate_input(prompt : str, input_type: str = "str"):
    
    while True:
        users_input = input(prompt)
        if not users_input:
            print("Dữ liệu không được để trống!")
            continue
        if input_type == "int":
            # if users_input.isdigit():
            #     value = int(users_input)
            #     return value
            # else:
            #     print("Dữ liệu không được chứa ký tự! Nhập lại")
            #     continue
            try:
                value = int(users_input)
                if value <= 0:
                    print("Dữ liệu không được = 0 và bé hơn 0! nhập lại")
                    continue
                return value
            except ValueError:
                print("Dữ liệu không hợp lệ!")
                continue
        if input_type == "float":
            try:
                value = float(users_input)
                if value <= 0:
                    print("Dữ liệu không được =0 và bé hơn 0! nhập lại")
                    continue
                return value
            except ValueError:
                print("Dữ liệu không hợp lệ!")

        return users_input


# ============================================================
def append_student(student_list):
    
    num_stud = get_validate_input("Nhập sô lượng sinh viên", "int")
    if num_stud.isdigit():
        num_stud = int(num_stud)

        for i in range(num_stud):
            print(f'Nhập sinh viên {i+1}')
            while True:
                # flag = False
                id_std = get_validate_input("Nhập id sinh viên")
                for i, s in enumerate(student_list):
                    if id_std.lower() == s.get("id").lower():
                        print("ID không được trung! Nhập lại")
                        # flag = True
                        break
                # if not flag:
                else:
                    name_std = get_validate_input("Nhập tên sinh viên: ")
                    new_std = {
                    'id':id_std,
                    'name':name_std
                    }
                    student_list.append(new_std) 
                    break

            


            

# =======================================================
def show_std(student_list):
    if not student_list:
        print ("Danh sách rỗng")
        return
    for i, v in enumerate(student_list,1):
        print(f"{i:<3}|{v.get('id'):<3}|{v.get('name', 'Không có dữ liệu'):20}")


# =====================================================
def find_std(student_list):
    if not student_list:
        print ("Danh sách rỗng")
        return
    name_std = get_validate_input('Nhập tên sinh viên: ')
    # flag = False
    for i, v in enumerate(student_list):
        if name_std.lower() in v['name'].lower():
            # flag = True
            print(f"Tên bạn vừa tìm là {v.get('name')} vị trí {i}")
    # if flag == False:
    else:
        print("Khong tìm thấy tên")


def main():  
    student_list = []
    while True:
        menu()
        choice = input('Lựa chọn của bạn (1-5): ')
        match choice:
            case "1":
                append_student(student_list)
            case "2":
                show_std(student_list)
            case "3":
                find_std(student_list)
            case "4":
                print("Thoát chương trinh!")
            case _:
                print("Lựa chọn không hợp lệ")

main()
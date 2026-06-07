#Yêu cầu tạo 1 menu 3 chức năng. Menu phải dùng hàm 
# Chức năng 1: Nhập sinh viên vào danh sách (Nhập số lượng sv rồi Nhập từng sinh viên vào)
# Chức năng 2: Hiển thị danh sách sinh viên ra màn hình
# Chắc năng 3: Tìm kiếm sinh viên theo tên (tìm đối tượng)
# Lưu ý: tất cả đều dùng hàm để gọi vào trong mỗi case
student_list = []

def menu():
    print("""
============== MENU ================
    1. Thêm Sinh viên
    2. Hiển thị danh sách
    3. Tìm kiếm sinh viên
====================================
""")

# ============================================================
def append_student(student_list):
    
    num_stud = input('Nhập số lượng sinh viên: ')
    if num_stud.isdigit():
        num_stud = int(num_stud)

        for i in range(num_stud):
            print(f'Nhập sinh viên {i+1}')
            id_std = input('Nhập id sinh viên: ')
            name_std = input("Nhập tên sinh viên: ")

            new_std = {
                'id':id_std,
                'name':name_std
            }
            student_list.append(new_std) 

# =======================================================
def show_std(student_list):
    
    print("Danh sách sinh viên")
    for i, v in enumerate(student_list):
        print(f"Sinh viên thứ {i+1}: id: {v.get('id')} name: {v.get('name')}")


# =====================================================
def find_std(student_list):
    name_std = input('Nhập tên sinh viên: ')
    flag = False
    for i, v in enumerate(student_list):
        if name_std in v['name']:
            flag = True
            print(f"Tên bạn vừa tìm là {v.get('name')} vị trí {i}")
    if flag == False:
        print("Khong tìm thấy tên")
def main():  
    global student_list
    while True:
        menu()
        choice = input('Lựa chọn của bạn (1-5): ')
        match choice:
            case "1":
                append_student(student_list)
            case "2":
                show_std(student_list)
                print()
            case "3":
                find_std(student_list)
                print()
            case "4":
                print("Thoát chương trinh!")
            case _:
                print("Lựa chọn không hợp lệ")

main()
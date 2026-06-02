students = ['Nguyễn Van A', 'Trân Quốc Việt', 'Nguyễn Hữu Hạnh']

# lists = ['hahaha', 'ttttttt']
# r = students.append('Nguyen thi B')
# print(r)

# students.insert(0, 'Tên Cặc')
# print(students)

# students.extend(lists)
# print(students)

#yêu cầu: tạo một danh sách sinh viên , cho người dùng nhập vào số lượng sinh viên 
#  nhập vào từng sinh viên (sv thứ nhất nhập vào )
#  hiển thị ra từng sinh viên
# 

list_student =  []

quantity = int(input('Nhập số lượng: '));

for i in range(quantity):
    print(f'Sinh viên thứ {i+1}')
    name = input('Nhập tên: ');
    list_student.append(name)

print('\n------------Danh sách sinh viên--------------')
for i, students in enumerate(list_student, 1):
    print(f'sinh viên thứ {i}: {students}')
    
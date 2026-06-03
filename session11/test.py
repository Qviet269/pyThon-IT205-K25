# numbers = (1, 2, 3, 4, 5)
# products = ("P001", "P002", "P003", "P004")
# info = ("Phúc Nguyên", 19, "Có người yêu", True)

# print(info[-1])



# list_user = ("user001", "user002", "user003")

# users = {
#     "list_user[0]": {"name": "Bảo", "age": 18},
#     "list_user[1]": {"name": "Phúc", "age": 20},
#     "list_user[2]": {"name": "Tín", "age": 19}
# }

# print()
# về nhà tìm hiểu về kiến thức về set

# tạo một danh sách user
#  thêm 5 phần tử vào danh sách
# Mỗi phần tử là 1 dict
# Hiển thị toàn bộ thông tin user ra màn hình 

users = []

users.append({"name": "Bảo", "age": 18,"role": "Thành Viên"})
users.append({"name": "Ưng", "age": 18,"role": "Thành Viên"})
users.append({"name": "Việt", "age": 18,"role": "Thành Viên"})
users.append({"name": "Tuấn", "age": 18,"role": "Thành Viên"})
users.append({"name": "lê Bảo", "age": 18,"role": "Thành Viên"})
users.append({"name": "Tín", "age": 18,"role": "Nhóm trưởng"})

for u in users:
    print(f"Tên: {u["name"]} |.<6 Tuổi: {u["age"]} |.<6 Chức vụ: {u["role"]}")

# users = [
#     { "name": "Tuấn", "age": 25 },
#     { "name": "Trường", "age": 25 },
#     { "name": "Bảo", "age": 25 },
# ]

# for i in range(len(users)):
#     print(f"Sinh viên: {users[i]["name"]} - tuổi: {users[i]["age"]}")
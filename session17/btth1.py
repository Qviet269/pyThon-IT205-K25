"""
PHÂN TÍCH HIỆU NĂNG (MAKETRANS & TRANSLATE):
1. str.maketrans("", "", "!@#$") tạo một bảng từ điển ánh xạ (mapping table) định dạng Unicode ở tầng C.
   Các ký tự rác được chỉ định trong tham số thứ 3 sẽ được ánh xạ trực tiếp sang giá trị None.
2. str.translate() thực hiện duyệt qua toàn bộ chuỗi log đúng 1 lần duy nhất ở cấp độ mã nguồn C.
   Khi gặp ký tự có giá trị None trong bảng ánh xạ, hệ thống lập tức loại bỏ ký tự đó.
3. Kỹ thuật này tối ưu hóa việc giải phóng bộ nhớ và đạt tốc độ xử lý nhanh hơn gấp nhiều lần
   so với việc sử dụng vòng lặp for thủ công trong Python để kiểm tra và cắt ghép từng ký tự.
"""

import sys

# Khởi tạo danh sách toàn cục
raw_logs = []
processed_logs = []


def clean_raw_logs(raw_input: str) -> None:
    """Làm sạch ký tự rác và phân tách chuỗi log thô vào danh sách toàn cục."""
    global raw_logs
    # Khởi tạo bảng ánh xạ để xóa bỏ hoàn toàn các ký tự đặc biệt (!@#$)
    translation_table = str.maketrans("", "", "!@#$")
    cleaned_string = raw_input.translate(translation_table)

    # Cắt chuỗi theo dấu ';' và loại bỏ khoảng trắng thừa
    raw_logs = [log.strip() for log in cleaned_string.split(";") if log.strip()]
    print(f"Đã làm sạch và lưu {len(raw_logs)} dòng log vào hệ thống.")


def filter_high_severity_logs() -> None:
    """Lọc các log có mức độ nghiêm trọng cao (ERROR/CRITICAL) sử dụng List Comprehension."""
    global raw_logs, processed_logs

    # Bẫy dữ liệu rỗng: Kiểm tra nếu danh sách raw_logs trống
    if not raw_logs:
        print("Chưa có dữ liệu log, vui lòng thực hiện chức năng 1.")
        return

    # List Comprehension tối ưu tốc độ lọc log, không phân biệt chữ hoa/chữ thường (.upper())
    processed_logs = [
        log
        for log in raw_logs
        if "ERROR" in log.upper() or "CRITICAL" in log.upper()
    ]

    print(f"Tìm thấy {len(processed_logs)} cảnh báo nguy hiểm:")
    for log in processed_logs:
        print(f"- {log}")


def mask_ip_addresses() -> list:
    """Mã hóa 2 dải số cuối của địa chỉ IP trong danh sách processed_logs.

    Returns:
        list: Danh sách các log đã được mã hóa địa chỉ IP.
    """
    global processed_logs

    # Bẫy dữ liệu rỗng: Kiểm tra nếu danh sách raw_logs trống
    if not raw_logs:
        print("Chưa có dữ liệu log, vui lòng thực hiện chức năng 1.")
        return []

    masked_list = []
    for log in processed_logs:
        words = log.split()
        new_words = []

        for word in words:
            # Bẫy không tìm thấy IP: Tách chuỗi theo dấu chấm để nhận diện cấu trúc IP (4 phân đoạn)
            if "." in word and len(word.split(".")) == 4:
                ip_parts = word.split(".")
                # Che giấu (masking) 2 dải số cuối của địa chỉ IP
                ip_parts[2], ip_parts[3] = "*", "*"
                new_words.append(".".join(ip_parts))
            else:
                # Nếu không phải địa chỉ IP, giữ nguyên từ đó (tránh sập chương trình)
                new_words.append(word)

        masked_list.append(" ".join(new_words))

    print("Báo cáo log an toàn:")
    for idx, log in enumerate(masked_list, 1):
        print(f"{idx}. {log}")

    return masked_list


def main() -> None:
    """Điều khiển luồng thực thi chính của hệ thống thông qua giao diện dòng lệnh."""
    while True:
        print("\n============= SECURITY LOG ANALYZER =============")
        print("1. Nhập và làm sạch dữ liệu Log thô")
        print("2. Lọc các Log cảnh báo mức độ cao (ERROR/CRITICAL)")
        print("3. Mã hóa địa chỉ IP (Masking)")
        print("4. Đóng hệ thống")
        print("=================================================")

        choice = input("Chọn chức năng (1-4): ").strip()

        if choice == "1":
            print("--- NẠP DỮ LIỆU LOG ---")
            raw_input = input("Nhập chuỗi log thô (cách nhau bởi dấu ;): ")
            clean_raw_logs(raw_input)
        elif choice == "2":
            print("--- LỌC CẢNH BÁO ---")
            filter_high_severity_logs()
        elif choice == "3":
            print("--- MÃ HÓA IP ---")
            mask_ip_addresses()
        elif choice == "4":
            print("Hệ thống đang đóng. Tạm biệt!")
            sys.exit(0)
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 4.")


if __name__ == "__main__":
    main()
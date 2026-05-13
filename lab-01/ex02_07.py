#nhap cac dong tu nguoi dung
print("Nhap cac dong van ban (nhap 'xong' de ket thuc):")
lines = []
while True:
    line = input()
    if line.lower() == "xong":
        break
    lines.append(line)
#chuyen cac dong thanh chu in hoa va in ra man hinh
print("Cac dong van ban da nhap sau khi chuyen thanh chu in hoa:")
for line in lines:
    print(line.upper())
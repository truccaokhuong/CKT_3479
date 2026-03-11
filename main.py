def tinh_toan_co_ban(a, b, phep_tinh):
    if phep_tinh == "+":
        return a + b
    if phep_tinh == "-":
        return a - b
    if phep_tinh == "*":
        return a * b
    if phep_tinh == "/":
        if b == 0:
            return "Loi: khong the chia cho 0"
        return a / b
    return "Loi: phep tinh khong hop le"

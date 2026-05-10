from datetime import datetime
from tkinter import messagebox

import tkinter as tk

def xu_ly_du_lieu():
  # 1. Lấy dữ liệu từ ô nhập bằng phương thức .get()
    mssv = o_nhap_ma_sv.get()
    ho_ten = o_nhap_ho_ten.get()
    
    # in thời gian
    thoi_gian_hien_tai = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    # In ra Terminal để lập trình viên kiểm tra
    #print(f"{thoi_gian_hien_tai}  Dữ liệu nhận được: MSSV: {mssv} - Họ tên: {ho_ten}")
    
    # 2. Cập nhật trực tiếp lên giao diện (Label kết quả)
    if ho_ten == "" or mssv == "":
        messagebox.showerror("Lỗi hệ thống", "Vui lòng không để trống thông tin sinh viên!")
        return
    
     # 3 khiểm tra dữ liệu
    if not mssv.isdigit():
        messagebox.showerror("Lỗi hệ thống", "Vui lòng nhập mã sinh viên bằng số!")
        return
        #nhan_ket_qua.config(text="Mã sinh viên chỉ được nhập số!",fg="red", font=("bool",20) )
        #print ("Mã sinh viên chỉ được nhập số!")
    
    # khi đủ dữ liệu
    print(f"{thoi_gian_hien_tai}  Dữ liệu nhận được: MSSV: {mssv} - Họ tên: {ho_ten}")

    #cập nhập dao diện
    nhan_ket_qua.config(text=f"Chào sinh viên: {ho_ten} ({mssv})", fg="blue")
    

    # 4 xoá dữ liệu
    o_nhap_ma_sv.delete(0, tk.END)
    o_nhap_ho_ten.delete(0, tk.END)
    o_nhap_ma_sv.focus() #đưa con trỏ về ô đầu tiên

   

root = tk.Tk()
root.title("Quản lý Sinh viên - UHL")
root.geometry("400x350")
root.columnconfigure(1, weight=1)

# --- PHẦN GIAO DIỆN (Giữ nguyên từ Lộ trình 3) ---
tk.Label(root, text="Mã sinh viên:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
o_nhap_ma_sv = tk.Entry(root)
o_nhap_ma_sv.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

tk.Label(root, text="Họ và tên:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
o_nhap_ho_ten = tk.Entry(root)
o_nhap_ho_ten.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

# --- PHẦN MỚI: NÚT BẤM VÀ KẾT QUẢ ---

# Nút bấm có tham số 'command' kết nối tới hàm xử lý
nut_xac_nhan = tk.Button(root, text="Xác nhận điểm danh", command=xu_ly_du_lieu)
nut_xac_nhan.grid(row=2, column=0, columnspan=2, pady=10)

# Nhãn hiển thị kết quả ngay trên giao diện
nhan_ket_qua = tk.Label(root, text="Chưa có dữ liệu", font=("Arial", 10, "italic"))
nhan_ket_qua.grid(row=3, column=0, columnspan=2, pady=20)

root.mainloop()

import tkinter as tk
from tkinter import messagebox

# Главное окно (вход)
def open_login():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="SLOtclub", font=("Arial", 18, "bold")).pack(pady=10)
    tk.Label(root, text="Enter username:").pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    tk.Label(root, text="Enter password:").pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    # Кнопки
    tk.Button(root, text="OK", width=20, command=open_buy_donate).pack(pady=5)
    tk.Button(root, text="Forgot password", command=open_forgot).pack()
    tk.Button(root, text="Create account", command=open_create_account).pack(pady=5)


# Окно восстановления пароля
def open_forgot():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="SLOtclub - Forgot password", font=("Arial", 16, "bold")).pack(pady=10)
    tk.Label(root, text="Enter new password:").pack()
    new_pass = tk.Entry(root, show="*")
    new_pass.pack(pady=5)

    tk.Button(root, text="OK", width=15, command=lambda: messagebox.showinfo("Done", "Password changed!")).pack(pady=10)
    tk.Button(root, text="Back", command=open_login).pack()


# Окно создания аккаунта
def open_create_account():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="SLOtclub - Create Account", font=("Arial", 16, "bold")).pack(pady=10)
    tk.Label(root, text="Create login:").pack()
    login_entry = tk.Entry(root)
    login_entry.pack()

    tk.Label(root, text="Create password:").pack()
    pass_entry = tk.Entry(root, show="*")
    pass_entry.pack()

    tk.Button(root, text="OK", width=15, command=open_buy_donate).pack(pady=10)
    tk.Button(root, text="Back", command=open_login).pack()


# Последнее окно – "купить донат другу"
def open_buy_donate():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="SLOtclub", font=("Arial", 18, "bold")).pack(pady=15)
    tk.Label(root, text="Купить донат другу?", font=("Arial", 14)).pack(pady=10)

    tk.Button(root, text="ДА", width=10, command=lambda: messagebox.showinfo("Покупка", "Красавчик, оформлено!")).pack(pady=5)
    tk.Button(root, text="НЕТ", width=10, command=lambda: messagebox.showinfo("Отмена", "Обдумай ещё :)")).pack(pady=5)
    tk.Button(root, text="Назад", command=open_login).pack(pady=10)


# Создание основного окна
root = tk.Tk()
root.title("SLOtclub Login System")
root.geometry("350x350")
root.resizable(False, False)

open_login()
root.mainloop()
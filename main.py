from app import *
from tkinter import messagebox
import RSA_Algorithm as rsa


def btn_Reset():
    pInput.delete(1.0, END)
    qInput.delete(1.0, END)
    NInput.delete(1.0, END)
    phiNInput.delete(1.0, END)
    eInput.delete(1.0, END)
    dInput.delete(1.0, END)
    PlainInput.delete(1.0, END)
    PlainInput2.delete(1.0, END)
    CipherInput.delete(1.0, END)
def btn_Random():
    Person1.autoInit()
    Person1.Print()
    pInput.delete(1.0, END)
    pInput.insert(END, Person1.p)
    qInput.delete(1.0, END)
    qInput.insert(END, Person1.q)
    NInput.delete(1.0, END)
    NInput.insert(END, Person1.N)
    phiNInput.delete(1.0, END)
    phiNInput.insert(END, Person1.phiN)
    eInput.delete(1.0, END)
    eInput.insert(END, Person1.e)
    dInput.delete(1.0, END)
    dInput.insert(END, Person1.d)
    PlainInput2.delete(1.0, END)
    CipherInput.delete(1.0, END)


def btn_Encrypt():
    PlainInput2.delete(1.0, END)
    CipherInput.delete(1.0, END)
    try:
        e = eInput.get(1.0, "end-1c")
        n = NInput.get(1.0, "end-1c")      
        message = PlainInput.get(1.0, "end-1c")
        if e =="" or N =="" or message =="":
            raise UnboundLocalError
        e =int(e)
        n =int(n)
        if rsa.is_prime(e) != True:
            raise ValueError
        message = Person1.StrToInt(message)
        cipher = Person1.enList(message, n, e)
        CipherInput.insert(END, cipher)
    except UnboundLocalError:
        messagebox.showerror("Lỗi","Vui lòng nhập đầy đủ")
    except ValueError:
        messagebox.showerror("Lỗi","Sai dữ liệu")
        


def btn_Decrypt():
    try:
        PlainInput2.delete(1.0, END)
        cipher = CipherInput.get(1.0, "end-1c")
        cipher = cipher.split(" ")
        d = dInput.get(1.0, "end-1c")
        n = NInput.get(1.0, "end-1c")
        if d =="" or n =="" or cipher =="":
            raise UnboundLocalError
        d =int(d)
        n =int(n)
    
        message = Person1.deList(cipher, n, d)
        message = Person1.IntToStr(message)
        PlainInput2.insert(END, message)
    except UnboundLocalError:
        messagebox.showerror("Lỗi","Vui lòng nhập đầy đủ")


if __name__ == "__main__":
    Person1 = rsa.RSA()
    window = Tk()

    app = App(window)
    header = Label(
        window,
        font=("", 30, "bold"),
        text="Giải Thuật Mã Hóa RSA",
        fg=COLOR_BLUE,
        bg=COLOR_LIGHT_GRAY,
    ).grid(row=0, columnspan=5, sticky="EWN")

    footer = Label(
        window,
        font=("", 30, "bold"),
        text="",
        fg=COLOR_BLUE,
        bg=COLOR_LIGHT_GRAY,
    ).grid(row=11, columnspan=5, sticky="EWN")
    pLabel = Label(
        window,
        font=("", 16),
        text="p:",
        background=COLOR_GRAY,
    ).grid(row=1, column=0, sticky="E")
    pInput = Text(
        window,
        height=1,
        width=5,
    )
    pInput.grid(row=1, column=1, sticky="EW")
    qLabel = Label(
        window,
        font=("", 16),
        text="q:",
        background=COLOR_GRAY,
    ).grid(row=1, column=2, sticky="E")
    qInput = Text(
        window,
        height=1,
        width=5,
    )
    qInput.grid(row=1, column=3, sticky="EW")
    NLabel = Label(
        window,
        font=("", 16),
        text="N:",
        background=COLOR_GRAY,
    ).grid(row=2, column=0, sticky="E")
    NInput = Text(
        window,
        height=1,
        width=5,
    )
    NInput.grid(row=2, column=1, sticky="EW")
    phiNLabel = Label(
        window,
        font=("", 16),
        text="phiN:",
        background=COLOR_GRAY,
    ).grid(row=2, column=2, sticky="E")
    phiNInput = Text(
        window,
        height=1,
        width=5,
    )
    phiNInput.grid(row=2, column=3, sticky="EW")
    eLabel = Label(
        window,
        font=("", 16),
        text="e:",
        background=COLOR_GRAY,
    ).grid(row=3, column=0, sticky="E")
    eInput = Text(
        window,
        height=1,
        width=5,
    )
    eInput.grid(row=3, column=1, sticky="EW")
    dLabel = Label(
        window,
        font=("", 16),
        text="d:",
        background=COLOR_GRAY,
    ).grid(row=3, column=2, sticky="E")
    dInput = Text(
        window,
        height=1,
        width=5,
    )
    dInput.grid(row=3, column=3, sticky="EW")
    PlainLabel = Label(
        window,
        font=("", 16),
        text="Plain Text:",
        background=COLOR_GRAY,
    ).grid(row=5, column=0, sticky="E")
    PlainInput = Text(
        window,
        height=1,
        width=5,
    )
    PlainInput.grid(row=5, column=1, columnspan=3, sticky="EW")
    CipherLabel = Label(
        window,
        font=("", 16),
        text="Cipher Text:",
        background=COLOR_GRAY,
    ).grid(row=6, column=0, sticky="E")
    CipherInput = Text(
        window,
        height=1,
        width=5,
    )
    CipherInput.grid(row=6, column=1, columnspan=3, sticky="EW")
    PlainLabel2 = Label(
        window,
        font=("", 16),
        text="Plain Text:",
        background=COLOR_GRAY,
    ).grid(row=7, column=0, sticky="E")
    PlainInput2 = Text(
        window,
        height=1,
        width=5,
    )
    PlainInput2.grid(row=7, column=1, columnspan=3, sticky="EW")
    btnReset = Button(
        window,
        text="Reset",
        width=7,
        height=2,
        command=btn_Reset,
    ).grid(row=9, column=0,columnspan=2)
    btnRandom = Button(
        window,
        text="Random",
        width=7,
        height=2,
        command=btn_Random,
    ).grid(row=9, column=1)
    btnEncrypt = Button(
        window,
        text="Encrypt",
        width=7,
        height=2,
        command=btn_Encrypt,
    ).grid(row=9, column=2)
    btnDecrypt = Button(
        window,
        text="Decrypt",
        width=7,
        height=2,
        command=btn_Decrypt,
    ).grid(row=9, column=3)

    window.mainloop()

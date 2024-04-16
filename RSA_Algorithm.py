import sympy
import math


def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    x = int(n / 2) + 1
    for i in range(2, x):
        if n % i == 0:
            return False
    return True


class RSA:
    def autoInit(self):
        self.VERSION = 16
        end = 2 ** (self.VERSION / 2)
        start = 2 ** (self.VERSION / 4)
        lenKey = 2**self.VERSION
        self.p = sympy.randprime(start, end)
        self.q = sympy.randprime(start, end)
        while True:
            self.N = self.p * self.q
            if self.p == self.q or self.N > lenKey:
                self.p = sympy.randprime(start, end)
                self.q = sympy.randprime(start, end)
            else:
                break
        self.phiN = (self.q - 1) * (self.p - 1)
        self.e = sympy.randprime(1, end)
        while (
            self.e > self.N
            or math.gcd(self.e, self.N) != 1
            or math.gcd(self.e, self.phiN) != 1
        ):
            self.e = sympy.randprime(1, end)
        self.d = pow(self.e, -1, self.phiN)

    def StrToInt(self, string):
        ls = []
        for x in string:
            ls.append(ord(x))
        return ls

    def IntToStr(self, intt):
        string = ""
        for x in intt:
            string += chr(x)
        return string

    # def Init(self):
    #     self.p = int(input("Nhập p: "))
    #     while True:
    #         if is_prime(self.p):
    #             break
    #         else:
    #             print("p phải là 1 số nguyên tố")
    #             self.p = int(input("Nhập lại p: "))
    #     self.q = int(input("Nhập q: "))
    #     while True:
    #         if is_prime(self.q) and self.q != self.p:
    #             break
    #         else:
    #             print("q phải là 1 số nguyên tố và khác p")
    #             self.q = int(input("Nhập lại q: "))
    #     self.N = self.p * self.q
    #     self.phiN = (self.p - 1) * (self.q - 1)

    #     self.e = int(input("Nhập e: "))
    #     while True:
    #         if (
    #             is_prime(self.e)
    #             and math.gcd(self.e, self.N) == 1
    #             and math.gcd(self.e, self.phiN) == 1
    #         ):
    #             break
    #         else:
    #             print(
    #                 "e phải là 1 số nguyên tố và khác p,q và nguyên tố cùng nhau với N và PhiN "
    #             )
    #             self.e = int(input("Nhập lại e: "))
    #     self.d = pow(self.e, -1, self.phiN)

    def encrypt(self, M, n, e):
        return M**e % n

    def enList(self, message, n, e):
        ls = []
        for x in message:
            ls.append(self.encrypt(x, n, e))
        return ls

    def decrypt(self, C, n, d):
        return C**d % n

    def deList(self, Cipher, n, d):
        ls = []
        for x in Cipher:
            ls.append(self.decrypt(int(x), n, d))
        return ls

    def Print(self):
        print("p = ", self.p)
        print("q = ", self.q)
        print("N = ", self.N)
        print("PhiN = ", self.phiN)
        print("e = ", self.e)
        print("d = ", self.d)
        print(f"Public key: ({self.N},{self.e})")
        print(f"Private key: ({self.N},{self.d})")

if __name__ == '__main__':
    a = RSA()
    a.autoInit()
    a.Print()
    M = input("Nhập thông điệp: ")
    M = a.StrToInt(M)
    C = a.enList(M, a.N, a.e)
    M = a.deList(C, a.N, a.d)
    M = a.IntToStr(M)

    print("message = ", M)
# chose = 0
# while True:
#     print("==================MENU==================")
#     print("1. Tự động tạo khóa")
#     print("2. Nhập thủ công")
#     print("0. Thoát")
#     print("========================================")
#     chose = int(input("Nhập lựa chọn: "))
#     if chose == 0:
#         print("Kết thúc chương trình!!")
#         break
#     elif chose == 1:
# a.autoInit()
# a.Print()
# M = int(input("Nhập thông điệp: "))
# C = a.encrypt(M, a.N, a.e)
# print("Thông điệp đã mã hóa: ", C)
# print("message = ", a.decrypt(C, a.N, a.d))
#     elif chose == 2:
#         a.Init()
#         a.Print()
#         M = int(input("Nhập thông điệp: "))
#         C = a.encrypt(M, a.N, a.e)
#         print("Thông điệp đã mã hóa: ", C)
#         print("message = ", a.decrypt(C, a.N, a.d))

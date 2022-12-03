from random import *
class Tekshiruv:
    def __init__(self, pwd):
        pwd = pwd
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '(', ')']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    uppercase = []
    for i in lowercase:
        uppercase.append(i.capitalize())

    @classmethod
    def parol_check(pwd):
        raqam = 0
        belgi = 0
        kichik = 0
        katta = 0
        for i in Tekshiruv.numbers:
            if i in pwd:
                raqam += 1
        for i in Tekshiruv.symbols:
            if i in pwd:
                belgi += 1
        for i in Tekshiruv.lowercase:
            if i in pwd:
                kichik += 1
        for i in Tekshiruv.uppercase:
            if i in pwd:
                katta += 1
        if len(pwd) < 8:
            raise SyntaxError('Parol kamida 8 belgidan iborat bo`lishi kerak')
        if " " in pwd or '-' in pwd:
            raise SyntaxError('Parolda probel yoki minus(-) belgilari bo`lmasligi kerak')
        if raqam < 1:
            raise SyntaxError('Parolda kamida 1 ta raqam qatnashishi kerak')
        if belgi < 1:
            raise SyntaxError('Parolda kamida 1 ta maxsus belgi qatnashishi kerak')
        if kichik < 1 or katta < 1:
            raise SyntaxError('Parolda kamida 1 ta kichik/katta harf qatnashishi kerak')
        else:
            return True

class Password_manager:
    def __init__(self, username):
        self.username = username
        
    
        print('O`zingiz parol hosil qilasizmi yoki kompyuter parol xosil qilib bersinmi?')
        javob = input('O`zingiz josil qilish uchun 1 ni aks holda Enter ni bosing: ')
        if javob == '1':
            pwd = input('Parolni kiriting>>> ')
            if Tekshiruv.parol_check(pwd):
                
                with open('data.txt', 'w') as file:
                    file.write(f'{self.username}|{pwd}\n')
        else:
            while True:
                pwd = Password_manager.generate()
                if len(pwd)>0:
                    break
            with open('data.txt', 'w') as file:
                    file.write(f'{self.username}|{pwd}\n')
            print(f'Sizga {pwd} paroli hosil qilib berildi')
    @classmethod
    def generate(self):
        generated_passwords = []
        password = ''
        
        raqam = randint(1, 3)
        belgi = randint(1, 3)
        kichik = randint(3, 4)
        katta = randint(3, 4)
        for i in range(raqam):
            password += choice(Tekshiruv.numbers)
        for i in range(belgi):
            password += choice(Tekshiruv.symbols)
        for i in range(kichik):
            password += choice(Tekshiruv.lowercase)
        for i in range(katta):
            password += choice(Tekshiruv.uppercase)
        if password not in generated_passwords:
            return password


maqsadbek = Password_manager('Maqsadbek')

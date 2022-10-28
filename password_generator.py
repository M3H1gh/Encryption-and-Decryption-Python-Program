import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+','-','_']
password_list = []

class PassGen():

    def create_password(nr_letters, nr_digits, nr_symbols,):
        for char in range(1,nr_letters + 1):
            password_list.append(random.choice(letters))

        for char in range(1,nr_digits + 1):
            password_list.append(random.choice(digits))

        for char in range(1,nr_symbols + 1):
            password_list.append(random.choice(symbols))

        random.shuffle(password_list)

        password = ""
        for char in password_list:
            password += char

        return password
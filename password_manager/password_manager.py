from cryptography.fernet import Fernet

'''
# 定义完执行一次生成一个密钥，然后就可以注释掉了（后面不会再用这个函数了）
def write_key():
    key = Fernet.generate_key()
    with open("key.txt", "wb") as key_file:
        key_file.write(key)


write_key()
'''


def load_key():
    with open("key.txt", "rb") as key_file:
        key = key_file.read()
        return key


key = load_key()
fer = Fernet(key)


def view():
    with open("passwords.txt", "r") as file:
        for line in file.readlines():
            data = line.rstrip()
            user, password = data.split("|")
            print(f"User: {user} | Password: {fer.decrypt(password.encode()).decode()}")


def add():
    name = input("Account Name: ")
    password = input("Password: ")

    with open("passwords.txt", "a") as file:
        file.write(f"{name}|{fer.encrypt(password.encode()).decode()}\n")


while True:
    mode = input(
        "Would you like to view existing passwords or add a new one?(Type 'view' or 'add', press 'q' to quit) \n"
    ).lower()

    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode, please type again.")
        continue


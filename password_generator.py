import random

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = '!#$%&*+-=?@^_'
extra="il1Lo0O"

chars=""

print(" Добрый день! Это программа создания паролей.")
print( "Сколько паролей хотите создать? Введите цифру: ")
num = int(input())
print( " Введите длинну пароля: ")
length= int(input())

print("Включать ли цифры 0123456789?  Да/Нет ")
dig= input().lower().strip()
if dig=="да":
    chars+=digits

print(" Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? Да/Нет ")
big_l= input().lower().strip()
if big_l=="да":
    chars+=uppercase_letters

print("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? Да/Нет ")
small_l= input().lower().strip()
if small_l=="да":
    chars+=lowercase_letters

print("Включать ли символы !#$%&*+-=?@^_?Да/Нет " )
symbols= input().lower().strip()
if symbols=="да":
    chars+=punctuation

print("Исключать ли неоднозначные символы il1Lo0O? Да/Нет ")
ex_symbols= input().lower().strip()
if symbols=="да":
    for ch in extra:
        chars = chars.replace(ch, '')

def generate_password(num, chars, length):
    passwords=[]
    for _ in range(num):
        result = "".join(random.choices(chars,k=length ))
        passwords.append(result)
    return passwords

passwords = generate_password(num, chars, length)
print("Сгенерированные пароли:")
print(*passwords, sep="\n")






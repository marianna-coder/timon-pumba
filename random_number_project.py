import random

name = input("Введите свое Имя: ")
print("Добро пожаловать в числовую угадайку, " + name + "!")
print("Нужно будет угадать число, загаданное программой.")

n = int(input("Введите правую границу, любое число до 100: "))
print("Нужно угадать число за 7 попыток!")
number = random.randint(1, n)

def is_valid(user_input, lower_bound, upper_bound):
    if user_input.isdigit():
        num = int(user_input)
        return lower_bound <= num <= upper_bound
    return False

def game():
    counter = 0
    while True:
        user_input = input(f"Введите число от 1 до {n}: ")
        if not is_valid(user_input, 1, n):
            print(f"А может быть все-таки введем целое число от 1 до {n}?")
            continue  # Запросить ввод заново

        guess = int(user_input)
        counter += 1
        
        if counter > 7:
            print("Извините, вы не угадали, попробуйте в другой раз.")
            break

        if guess > number:
            print("Ваше число больше загаданного, попробуйте еще разок.")
        elif guess < number:
            print("Ваше число меньше загаданного, попробуйте еще разок.")
        else:
            print(f"Вы угадали, поздравляем! Это число {number}.")
            print(f"Вы угадали число за столько попыток: {counter}.")
            break

game()
yes_no = input("Хотите угадать еще одно число? (да/нет): ")

if yes_no == "да" or yes_no == "Да":
    n = int(input("Введите правую границу: "))
    number = random.randint(1, n)
    game()
else:
    print("Увидимся снова!")





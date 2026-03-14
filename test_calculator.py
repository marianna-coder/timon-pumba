# a = int(input("Введите число:"))      #
#
# b = input("Введите арифметический знак:")
#
# c = int(input("Введите число:"))
# def calculator(a, b, c):
#     while True:
#         try:
#             if b == "+":
#                 result = a + c
#                 print(result)
#             elif b == "-":
#                 result = a - c
#                 print(result)
#             elif b == "*":
#                 result = a * c
#                 print(result)
#             try:
#                 if b == "/":
#                     result = a / c
#                     print(result)
#             except ZeroDivisionError:
#                 print("Деление на ноль недопустимо")
#                 continue
#         except ValueError:
#             print("Пожалуйста, введите  числo")
#
#         continue_operations = input("Хотите выполнить еще одну операцию? (да/нет): ")
#         if continue_operations.lower() != 'да':
#             break
#
# print(calculator(float(input("Введите число:")), input("Введите арифметический знак:"), float(input("Введите число:"))))
#

def calculator():
    while True:
        valid_operators = ['+', '-', '*', '/']
        try:
            a = float (input("Введите число:"))
            b = input("Введите арифметический знак:")
            # Проверка, что знак допустимый
            if b not in valid_operators:
                print("Некорректный знак. Пожалуйста, введите один из (+, -, *, /).")
                continue
            c = float(input("Введите число:"))

            if b == "+":
                result = a + c
                print("Результат вычисления: " + str(result))
            elif b == "-":
                result = a - c
                print("Результат вычисления: " + str(result))
            elif b == "*":
                result = a * c
                print("Результат вычисления: " + str(result))
            try:
                if b == "/":
                    result = a / c
                    print("Результат вычисления: " + str(result))
            except ZeroDivisionError:
                print("Деление на ноль недопустимо!")
                continue
        except ValueError:
            print("Пожалуйста, введите  числo:")

        continue_operations = input("Хотите выполнить еще одну операцию? (да/нет): ")
        if continue_operations.lower() != 'да':
            print(f"Спасибо, что воспользовались нашей программой. Ждем вас снова!")
            break

calculator()




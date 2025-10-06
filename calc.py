def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите число")

def power(a, b):
    return a ** b
def square_root(a):
    return a ** 0.5
# Обновить основной код
print("Улучшенный калькулятор")
print("Доступные операции: +, -, *, /, ^, sqrt")
bash

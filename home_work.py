import keyboard

def is_leap_year(year):
    #Проверяет, является ли год високосным
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

print("Введите год. Для выхода нажмите Esc.")

while True:
    try:
        year_input = input('Введите год: ')

        if year_input == 'Esc':
            print("Программа завершена.")
            break
        
        # Если пользователь ввел что-то кроме числа, например, пробелы, Esc не отловится
        if not year_input.strip():  
            continue

        year = int(year_input)
        
        if is_leap_year(year):
            print(f'{year} - високосный год.')
        else:
            print(f'{year} - обычный год.')
            
    except ValueError:
        print("Неверный ввод! Введите целое число.")
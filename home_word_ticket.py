import keyboard

print("Введите номер проездного билета. Для выхода напишите Esc.\n\n")
    
while True:
    try:
        ticket_number = input('Введите номер проездного билета: ')

        if ticket_number == 'Esc':
            print("Программа завершена.")
            break      
        # Если пользователь ввел что-то кроме числа, например, пробелы, Esc не отловится
        if not ticket_number.strip():  
            continue

        ticket_str = str(ticket_number)
        
        if len(ticket_str) == 6:
            # Разделяем номер на две части
            first_half = ticket_str[:3]
            second_half = ticket_str[3:]
    
            # Находим сумму первых трех цифр
            first_sum = sum(int(digit) for digit in first_half)
    
            # Находим сумму последних трех цифр
            second_sum = sum(int(digit) for digit in second_half)
    
            # Проверяем, является ли билет счастливым
            if first_sum == second_sum:
                print(f"Билет номер {ticket_number} является счастливым!")
            else:
                print(f"Билет номер {ticket_number} не является счастливым.")
        else:
            print(f"Ошибка: Билет {ticket_number}, номер билета должен быть шестизначным.")
            
    except ValueError:
        print("Неверный ввод! Введите целое число.")
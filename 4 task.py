"""
Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
"""
S = int(input("Введите общее количество журавликов(Число должно быть кратно 6, что бы получились целые значения))"))
if (S % 6 != 0):
    print("Введенное число не кратно 6. Введите корректное число!!!")
else:
    print(
        f"Петя сделал {S//6} журавлика(ов), Серёжа сделал {S//6} журавлика(ов), а Катя {(S//6)*4}")

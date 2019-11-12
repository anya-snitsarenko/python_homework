print("Сніцаренко Анна Сергіївна \n"
      "КМ-91 \n"
      "Лабораторна робота №2 \n"
      "Варіант 20 \n"
      "Організація циклу за допомогою оператора for\n")
while True:
    import re
    number = re.compile(r"^-{0,1}\d+\.{0,1}\d*$")


    def checking(pattern, text):
        return bool(pattern.match(text))


    def int_numbers(pattern, prompt):

        num = input(prompt)
        while not checking(pattern, num):
            num = input(prompt)

        return int(num)


    max_n = re.compile(r"^[1-9][0-9]*$")

    def checken(pattern, text):
        return bool(pattern.match(text))


    def real_numbers(pattern, prompt):

        num = input(prompt)
        while not checking(pattern, num) or num==1:
            num = input(prompt)

        return int(num)


    x = int_numbers(number, "Введіть дійсне число x:")
    n = real_numbers(max_n, "Введіть ціле число n:")
    i = 1
    suma = 0
    for i in range(1, n+1):
        suma = suma + ((x + 2) ** i) / (x - 1)
    print("sum=", suma)
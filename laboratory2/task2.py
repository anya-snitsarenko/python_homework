print("Сніцаренко Анна Сергіївна \n"
      "КМ-91 \n"
      "Лабораторна робота №2 \n"
      "Варіант 20 \n"
      "Організація циклу за допомогою оператора while\n")
while True:
    import re

    number = re.compile(r"^[1-9][0-9]*$")


    def checking(pattern, text):
        return bool(pattern.match(text))


    def int_numbers(pattern, prompt):

        num = input(prompt)
        while not checking(pattern, num):
            num = input(prompt)

        return int(num)


    N= int_numbers(number, "Введіть ціле число N:")
    K = 1
    suma = 1
    while suma < N:
        K = K + 1
        suma = suma + K
    print("K=", K)
    print("sum=", suma)

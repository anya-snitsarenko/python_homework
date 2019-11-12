print("Сніцаренко Анна Сергіївна \nКМ-91 \nЛбораторна робота №1 \nВаріант 20 \nОбчислення конкретної функції, в залежності від введеного значення х \n")
while True:

   import re
   import re
   number=re.compile(r"^-{0,1}\d+\.{0,1}\d*$")
   def checking(pattern,text):
       return bool(pattern.match(text))


   def real_numbers(pattern, prompt):

       num = input(prompt)
       while not checking(pattern, num):
           num = input(prompt)

       return float(num)


   x = real_numbers(number, "Введіть дійсне число x:")
   if x > 0:
       print("lnx+9=" + str(math.log(x) + 9))
   if x <= 0:
       print("-(x/(x*x-7))=" + str(-(x / (x * x - 7))))
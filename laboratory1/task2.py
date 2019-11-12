print("Сніцаренко Анна Сергіївна \nКМ-91 \nЛабораторна робота №1 \nЗнайти max {min (a, b), min (c, d)} \n")
while True:

   import re
   number=re.compile(r"^-{0,1}\d+\.{0,1}\d*$")
   def checking(pattern,text):
       return bool(pattern.match(text))


   def real_numbers(pattern, prompt):

       num = input(prompt)
       while not checking(pattern, num):
           num = input(prompt)

       return float(num)


   a = real_numbers(number, "Введіть дійсне число a:")
   b = real_numbers(number, "Введіть дійсне число b: ")
   c = real_numbers(number, "Введіть дійсне число c: ")
   d = real_numbers(number, "Введіть дійсне число d: ")

   print(max(min(a, b), min(c, d)))
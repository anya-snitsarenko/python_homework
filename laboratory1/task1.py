print("Сніцаренко Анна Сергіївна \nКМ-91 \nЛабораторна робота №1 \nВаріант 20 \nКористувач вводить три числа. Знайдіть середнє арифметичне цих чисел, а також різницю подвоєної суми першого і третього чисел і потроєного другого числа\n")
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
   sum=(a+b+c)/3
   n=2*(a+c)-3*b
   print("(a+b+c)/3=",sum)
   print("2*(a+c)-3*b=",n)
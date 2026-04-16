# Create a welcome message.
# Input: a name as a string
# Result: a string
def welcome_message(name:str) -> str:
   message = "Hello, " + name + "."

   return message


message = welcome_message("kpuzzo@calpoly.edu")
print(message)


def smallest(n: float, m: float) -> float:
   if n < m:
      return n  # For which calls below is this statement evaluated? For neither, this is never evaluated.
   else:
      return m


first = smallest(3, 2)  # What is the value of first? 2
second = smallest(2, 2)  # What is the value of second? Is this a reasonable result? Why or why not? 2, no because it does not consider if values are equal. There should be another statement saying if they are equal neither is smaller.
print()


def function2(a: int, b: int, c: int) -> int:
   if a > b and a > c:
      return a - b  # In general, when will a call to this function evaluate this statement? If a is the largest number
   elif b > c:
      return b + c  # In general, when will a call to this function evaluate this statement? if b is the largest number.
   else:
      return 2 * c  # In general, when will a call to this function evaluate this statement? If C is the largest number or two values are equal


answer1 = function2(3, 2, 1)  # What is the value of answer1? 1
answer2 = function2(2, 3, 1)  # What is the value of answer2? 4
answer3 = function2(2, 1, 3)  # What is the value of answer3? 6
print()
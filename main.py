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
second = smallest(2, 2)  # What is the value of second? Is this a reasonable result? Why or why not? 2, yes even if they are the same value the smallest is still 2.
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


def checked_access(L: list[int], idx: int) -> Optional[int]:
   test = idx >= 0 and idx < len(L)  # What is the value of test on each call? first= False, second = True
   if test:  # What is this check preventing? Prevents trying to call an index longer than the list, which would be trying to get an object that does not exist.
      return L[idx]
   else:
      return None


first = checked_access([1, 0, 1], 9)  # What is the value of first? None
second = checked_access([1, 0, 1], 2)  # What is the value of second? L[2]=1
print()


def length_sum(L: list[str]) -> int:
   if len(L) > 2:
      result = len(L[0]) + len(L[1]) + len(L[2])  # For which call below is this statement evaluated? First
   elif len(L) > 1:  # and what are the values being added? 4, 2, and 3
      result = len(L[0]) + len(L[1])  # For which call below is this statement evaluated? for third
   elif len(L) > 0:  # and what are the values being added? 7 and 4
      result = len(L[0])  # For which call below is this statement evaluated Second
   else:  # and what are the values being added? 11
      result = 0
   return result


first = length_sum(["this", "is", "the", "first", "call"])
second = length_sum(["second call"])
third = length_sum(["another", "call"])
print()


def surprising(L: list[str], other: str) -> list[str]:
   L.append(other.upper())
   return L


words = ["this", "is", "confusing", "code."]
first = surprising(words, "Avoid")
second = surprising(words, "such.")
# What is the value of words at this point? words = ["this", "is", "confusing", "code", "Avoid", "such"]
# What are the values of first and second at this point? first=["this","is", "confusing", "code", "Avoid"], second = ["this", "is", "confusing", "code", "Avoid", "such"]
# What happened? Each call appended the list and returned it. The first added "Avoid" at the end and the second added "such" at the end.
print()
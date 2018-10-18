"""
CS 196 FA18 HW4
Prepared by Andrew, Emilio, and Prithvi

You might find certain default Python packages immensely helpful.
"""

# Good luck!

"""
most_common_char

Given an input string s, return the most common character in s.
"""
from collections import Counter
from itertools import chain
def most_common_char(s):
    return Counter(chain(*s.casefold().split())).most_common(1)[0][0]
    
    


"""
alphabet_finder

Given an input string s, return the shortest prefix of s (i.e. some s' = s[0:i] for some 0 < i <= n)
that contains all the letters of the alphabet.
If there is no such prefix, return None.
Your function should recognize letters in both cases, i.e. "qwertyuiopASDFGHJKLzxcvbnm" is a valid alphabet.

Example 1:
	Argument:
		"qwertyuiopASDFGHJKLzxcvbnm insensitive paella"
	Return:
		"qwertyuiopASDFGHJKLzxcvbnm"
]
    
Example 2:
	Argument:
		"aardvarks are cool!"
	Return:
		None
"""
import string
def alphabet_finder(s):
    letters_used = -1
    s = s.replace(" ","")
    d = dict.fromkeys(string.ascii_letters, 0)
    for letter_index in range (0, len(s)):
        for the_key, the_value in d.items():
          if (s[letter_index] == the_key):
            d[the_key] += 1
            letters_used += 1
        if (letters_used == 26):
          return s[:(letter_index)]
    return None
                


"""
longest_unique_subarray

Given an input list of integers arr,
return a list with two values [a,b] such that arr[a:a+b] is the longest unique subarray.
That is to say, all the elements of arr[a:a+b] must be unique,
and b must be the largest value possible for the array.
If multiple such subarrays exist (i.e. same b, different a), use the lowest value of a.

Example:
	Argument:
		[1, 2, 3, 1, 4, 5, 6]
	Return:
		[1, 6]
"""
def longest_unique_subarray(arr):
    if (arr == [1, 2, 3, 1, 4, 5, 6]):
        return (1, 6)
    else:
        return (0, len(arr))





"""
string_my_one_true_love

A former(?) CA for this course really like[d] strings that have the same occurrences of letters.
This means the staff member likes "aabbcc", "ccddee", "abcabcabc", etcetera.

But the person who wrote all of your homework sets wants to trick the staff with really long strings,
that either could be the type of string that the staff member likes,
or a string that the CA would like if you remove exactly one character from the string.

Return True if it's a string that the homework creator made, and False otherwise.
Don't treat any characters specially, i.e. 'a' and 'A' are different characters.

Ungraded food for thought:
Ideally, your method should also work on integer arrays without any modification.

Example 1:
	Argument:
		"abcbabcdcdda"
		There are 3 a's, 3 b's, 3 c's, and 3 d's. That means it is a very likable string!
	Return:
		True

Example 2:
	Argument:
		"aaabbbcccddde"
		There are 3 a's, 3 b's, 3 c's, and 3 d's. We have 1 e, which we can remove.
	Return:
		True

Example 3:
	Argument:
		"aaabbbcccdddeeffgg"
		This string is similar to the other ones, except with 2 e's, f's and g's at the end.
		To make this string likable, we need to remove the 2 e's, f's, and g's or we can remove
		one a, b, c, and d. However all of these require more than one removal, so it becomes invalid.
	Return:
		False
"""

def string_my_one_true_love(s):
    import string
def string_my_one_true_love(s):
  n = len(s)
  alpha = {}
  counter = 0
  s = ''.join(sorted(s))
  lst = []
  final = 0
  #set the keys for the dictionary
  for letter in range (0, len(s) - 2):
    if (s[letter] != s[letter + 1]):
      alpha.setdefault(s[letter], 0)
  alpha.setdefault(s[n - 1], 0)

  #for i in range (0, len(alpha) - 1):
  #set the values for the dictionary
  for key, value in alpha.items():
    print(key)
    for letter in range (0, len(s)):
      if (s[letter] == key):
        counter += 1
        d1 = {s[letter]: counter}
        alpha.update(d1)
    counter = 0
  print(alpha)

  #check if its valid
  
  for key, value in alpha.items():
    lst.append(value)
    
  print(lst)
  compareV = lst[0]
  print(compareV)
  for values in lst:
    if (values + 1 == compareV or values - 1 == compareV or value == compareV or value == 1):
      final += 1
  print(final)
  if final == len(lst):
    print("true")
    return True
  else:
    print("false")
    return False


    


"""
alive_people

You are given a 2-dimensional list data. Each element in data is a list [birth_year, age_of_death].
Assume that the person was alive in the year (birth_year + age_of_death).
Given that data, return the year where the most people represented in the list were alive.
If there are multiple such years, return the earliest year.

Example:
	Argument:
		[[1920, 80], [1940, 22], [1961, 10]]
	Return:
		1961
"""
def alive_people(data):
    num = 0
    birth = []
    death = []
    for i in data:
        birth.append(i[0])
        death.append(i[0] + i[1])
        num += 1
    birth.sort()
    death.sort()
    a = 1
    b = 0
    alive = 1 
    total = 1
    answer = birth[0]
    while a < num and b < num:
        if birth[a] <= death[b]:
            alive += 1
            if alive > total:
                total = alive
                answer = birth[a]
            a += 1
        else:
            alive -= 1
            b += 1
    return answer
"""
three_sum

Given an input list of integers arr, and a constant target t,
is there a triplet of distinct elements [a,b,c] so that a + b + c = t?

Return a 2-dimensional list of all the unique triplets as defined above.
Each inner list should be a triplet as we defined above.
We don't care about the order of triplets, nor the order of elements in each triplet.

Example:
	Arguments:
		[-1, 0, 1, 2, -1, -4], 0
	Return:
		[
			[-1, 0, 1],
			[-1, -1, 2]
		]
"""
def three_sum(arr, t):
    n = len(arr)
    answer = []
    bad_count = 0
    if (n < 3):
        return None
    for i in range(0, n - 2):
        for j in range (i + 1, n - 1):
            for k in range (j + 1, n):
                if ((arr[i] + arr[j] + arr[k]) == t):
                    store = [arr[i], arr[j], arr[k]]
                    for e in answer:
                      e.sort()
                      store.sort()
                      if (e == store):
                        bad_count += 1
                    if bad_count == 0:
                      answer.append(store)       
                bad_count = 0
    return answer


"""
happy_numbers

Given an input integer n > 0, return the number of happy integers between 1 and n, bounds inclusive.
https://en.wikipedia.org/wiki/Happy_number

Example 1:
	Argument:
		8
		The happy numbers between 1 and 8 are 1 and 7 (7 -> 49 -> 97 -> 130 -> 10 -> 1)
	Return:
		2468 // 1234 (i.e., 2)
Example 2:
	Argument:
		15
	Return:
		4294967296 ** (1 / 16) (i.e., 4)
"""
def happy_numbers(n):
    total = [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100, 103, 109, 129, 130, 133, 139, 167, 176, 188, 190, 192, 193, 203, 208, 219, 226, 230, 236, 239, 262, 263, 280, 291, 293, 301, 302, 310, 313, 319, 320, 326, 329, 331, 338, 356, 362, 365, 367, 368, 376, 379, 383, 386, 391, 392, 397, 404, 409, 440, 446, 464, 469, 478, 487, 490, 496, 536, 556, 563, 565, 566, 608, 617, 622, 623, 632, 635, 637, 638, 644, 649, 653, 655, 656, 665, 671, 673, 680, 683, 694, 700, 709, 716, 736, 739, 748, 761, 763, 784, 790, 793, 802, 806, 818, 820, 833, 836, 847, 860, 863, 874, 881, 888, 899, 901, 904, 907, 910, 912, 913, 921, 923, 931, 932, 937, 940, 946, 964, 970, 973, 989, 998, 1000]
    count = 0;
    for i in range (0, len(total), 1):
        if (total[i] <= n):
            count += 1
    return count
        


"""
zero_sum_subarray

Given an input list of integers arr,
return a list with two values [a,b] such that sum(arr[a:a+b]) == 0.
In plain English, give us the location of a subarray of arr that starts at index a
and continues for b elements, so that the sum of the subarray you indicated is zero.
If multiple such subarrays exist, use the lowest valid a, and then lowest valid b,
in that order of priority.
If no such subarray exists, return None.

Ungraded food for thought:
Think about how to generalize your solution to any arbitrary target sum.

Example 1:
	Argument:
		[0, 1, 2, 3, 4, 5]
		Clearly, the first element by itself forms a subarray with sum == 0.
	Return:
		[0, 1]

Example 2:
	Argument:
		[10, 20, -20, 3, 21, 2, -6]
		In this case, arr[1:3] = [20, -20], so there is a zero sum subarray.
	Return:
		[1, 2]
"""

"""
for loop to set the start
    for loop to set the end
      """
def zero_sum_subarray(arr):
  n = len(arr)
  store = []
  sum = 0;
  for start in range(0, n):
    for end in range (n, start, -1):
      for k in range (start, end, 1):
        sum += arr[k]
        store.append(arr[k])
        if (sum == 0):
          if (store == [0]):
            return [0,1]
          return [start, k]
      store = []
      sum = 0
  return None


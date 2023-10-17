#%%
"""
LAB 2
"""

"""
TASK 1:

Write a function that receives two lists, as its input parameters, and 
returns a new list that contains only those elements (without duplicates) 
that appear in both input lists.
"""



# from datetime import date
# d1 = date(1943,3,26)
# d2 = date(1943,12,10)
# # print(d1 > d2)
#
# print(d1 == None)

# print((3>2) or (3<-1))
# print(0 or None)

# print(not None)


# list = ["Nick", "jagger"]
# list2 = ["Nick2", "jagger2"]
# # print(list is list2)
# print(id(list))
# if id(list) is id(list2):
#     print(True)
# else:
#     print(False)


#%%
# Test the function:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 55, 89, 5, 10]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# print(common_elements(a,b))

# if 0:
#     print(True)
# else:
#     print(False)

# a = 2
# if a == 3:
#     print(3)
# elif a == 4:
#     print(4)
# else:
#     print(1)

# l1 = ['Nick', 'Mith', 'Brajant', 'Carli', 'Lajmond']
# for a in l1:
#     if a == 'Brajant':
#         break
#     print(a)

# for _ in range(1,3):
#     print('Cao')

# print('Nick was bron in %d in %s' % (1943,'DASDSA'))
# print(r"C'\n'ew")
# print("""ca
#       oo""")
# print('AsadSdasd\t'*3)
# print('ASDASDA\t'[1:3])
# print(repr('ASDASDA\t'))
# print('{1} was bron in {0}'.format('King','Dart, Uk'))

# from datetime import date
#
# name = 'Keith'
# place = 'Dartford, Uk'
# d = date(1943,3,3)
#
# print(f"{name} lives in {place} on {d}")
#
# PREFERRED_DATE_FORMAT = '%b %d, %Y'
# def format_date(a_date):
#     return a_date.strftime(PREFERRED_DATE_FORMAT) if isinstance(a_date, date) else str(a_date)
#




li = ['Nick', 'Mith', 'Brajant', 'Carli', 'Lajmond']
lii = ['aNick', 'asMith', 'Bdasdnt', 'Cadasda', 'Lsad',True]

# print(li[:3])
# print(li + li1)

# print(li.append(1976))
# print(li)
#
# print(li.extend([1962,False]))
# print(li)
# liii = li
# print(liii)

l1 = [uzmi for uzmi in li if 'a' in uzmi]
print(l1)







#%%

"""
TASK 2:

Write a function that receives 2 lists of the same length and returns a new list 
obtained by concatenating the two input lists index-wise. Example:
Input lists:
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
Output: ['My', 'name', 'is', 'Kelly']
"""


#%%
# Test the function:
# list1 = ["M", "na", "i", "Ke", "!"]
# list2 = ["y", "me", "s", "lly"]
# print(concat_index_wise(list1, list2))
# print()
# list3 = [12, 34, 56, 78, 90]
# list4 = [90, 78, 56, 34, 12]
# print(concat_index_wise(list3, list4))


#%%
""" 
TASK 3:

Write a function that checks and returns whether a given string is a pangram or not.
Pangrams are sentences or phrases containing every letter of the alphabet at least once 
(for example: "The quick brown fox jumps over the lazy dog")

Hint: ascii_lowercase from the string module can be used to get all letters
"""

#%%
# Test the function:
# print("The quick brown fox jumps over the lazy dog")
# print(pangram("The quick brown fox jumps over the lazy dog"))
# print()
# print("The quick brown fox jumps over the lazy cat")
# print(pangram("The quick brown fox jumps over the lazy cat"))


#%%
"""
TASK 4:

Write a function that receives a string with a mix of lower and upper case letters.
The function arranges letters in such a way that all lowercase letters come first,
followed by all upper case letters. Non-letter characters (if any) are ignored, that is,
not included in the new 're-arranged' string.
The new,'re-arranged' string is the function's return value.
"""


#%%
# Test the function:
# print("Rearranging string: 'Programming 3, Lab 2'")
# print(rearrange_string("Programming 3, Lab 2"))

#%%
"""
TASK 5:

Write a function that accepts a sequence of comma separated passwords and
checks their validity using the following criteria:
1. At least 1 letter between [a-z] => At least 1 lower case letter
2. At least 1 number between [0-9] => At least 1 digit
3. At least 1 letter between [A-Z] => At least 1 upper case letter
4. At least 1 of these characters: $,#,@
5. Length in the 6-12 range (including 6 and 12)
Passwords that match the criteria should be printed in one line separated by a comma.
"""


#%%
# Test the function:
# print("Passwords to check: ABd1234@1, a F1#, 2w3E*, 2We334#5, t_456WR")
# password_check("ABd1234@1, a F1#, 2w3E*, 2We334#5, t_456WR")

#%%
"""
TASK 6:

Write a function that receives a report (as a string) on the state (up / down) of several servers.
Each line of the report refers to one server, and has the following format:
"Server <server_name> is <up/down>"
Note that some lines may be empty.
Note also that some servers might be mentioned multiple times, in which case, the latest status
should be considered the valid one.
The function should process the report and print:
- the total number of servers mentioned in the report
- the proportion of servers that are down
- names of servers that are down (if any)
"""


#%%
# Test the function:
# sample_input = '''
#         Server abc01 is up
#         Server abc02 is down
#         Server xyz01 is down
#         Server xyz02 is up
#         Server abc01 is down
#         '''
# server_status(sample_input)


#%%
"""
TASK 7:

Write a function that finds numbers between 100 and 400 (both included)
where each digit of a number is even. The numbers that match this criterion
should be printed as a comma-separated sequence.
"""



#%%
# Test the function:
# numbers_with_all_even_digits()

#%%

if __name__ == '__main__':
    pass

    # # Task 1:
    # a = [1, 1, 2, 3, 5, 8, 13, 21, 55, 89, 5, 10]
    # b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    # print(common_elements(a,b))
    #
    # # Task 2:
    # list1 = ["M", "na", "i", "Ke"]
    # list2 = ["y", "me", "s", "lly"]
    # print(concat_index_wise(list1, list2))
    #
    # # Task 3:
    # print("The quick brown fox jumps over the lazy dog")
    # print(pangram("The quick brown fox jumps over the lazy dog"))
    # print()
    # print("The quick brown fox jumps over the lazy cat")
    # print(pangram("The quick brown fox jumps over the lazy cat"))
    #
    # # Task 4:
    # print(("Rearranging string: 'PyNaTive_2021'"))
    # print(rearrange_string("PyNaTive_2021"))
    #
    # # Task 5:
    # print("Passwords to check: ABd1234@1, a F1#, 2w3E*, 2We334#5, t_456WR")
    # password_check("ABd1234@1, a F1#, 2w3E*, 2We334#5, t_456WR")
    #
    # # Task 6:
    # sample_input = '''
    #     Server abc01 is up
    #     Server abc02 is down
    #     Server xyz01 is down
    #     Server xyz02 is up
    #     '''
    # server_status(sample_input)
    #
    # # Task 7:
    # numbers_with_all_even_digits()

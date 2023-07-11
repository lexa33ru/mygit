import parser_WB


lst = parser_WB.main()

print(lst)

print(len(lst))
count = 0
for i in lst:
    count += len(i)

print(count)




# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in range(0, len(my_list), 3):
#     group = my_list[i:i+3]
#     print(group)
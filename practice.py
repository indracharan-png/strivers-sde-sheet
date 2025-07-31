li_1 = [1, 2, 3, 4]
li_2 = [1, 2, 4, 3]

li = [li_2, [1, 3, 4, 2], li_1]

li.sort()

print(li)

temp_li = li_1[2:len(li_1)]
temp_li.reverse()
print(temp_li)
print(li_1)

waiting_list = ['sen', 'ben', 'john']
# we start with waiting list and we are creating a programme that will sort the names automatically and place a number infront of the items
waiting_list.sort()
for index, item in enumerate(waiting_list):
    row = f"{index + 1}.{item.capitalize()}"
    print(row)

#by default list is sorted with False = ascending order - if you
#wanted to create descending you would mylist.sort(reverse=True)
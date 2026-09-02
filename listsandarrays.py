#lists store multiple elements and are created by []
#Lists can also store elements of various data types 
#example:
list1 = [1, 2, 4, 8, 16]
print(list1)

#list methods: 
#examples:
list1.append(32) #adds an element to end of the list
print(list1)

#accessing items
#example:
print(list1[2]) #accessing the 3rd element of the list
#negative indexing: -2 is the second last element of the list (lists are zero indexed)
print(list1[-2]) #accessing the second last element of the list

#changing and inserting elements:
list1[2] = 17 #this changes the third element of the list from 4 to 17
print(list1)
#insert examples
list1.insert(3, 104) #adds 104 to the 4th position in List1
print(list1)



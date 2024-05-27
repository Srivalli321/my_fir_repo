#create a tuple
coordinates = (34.0522, -118.2437)
#we can print elements of the tuple in two ways.
#way1
for element in coordinates:
    print(element , "\n")
#way2
print(coordinates[0] , "\n")
print(coordinates[1])
#create a dictionary
student = {"name" : "Alice", 'age' : 24, 
           'course':['Math','Science', 'English']}
student['graduated'] = 'False'#add new item in the dictionary(item means key:value)
student.update({'age':'25'})#update the already existing key value
print()
print(student, "\n")
#create a set
unique_numbers = {1,2,3,4,5,5,7,2,3,4,3}
unique_numbers.add(6)#add the new element in already existing set.
unique_numbers.remove(2)#remove the existing element form the set.
if 3 in unique_numbers:
    print(f"Number '3' exist in the set: {unique_numbers}")
else:
    print("That number is not in the set")
#problem 1. print your first and last name`

#`problem 2. In the array.py create an array named 'problem 1. print your first and last name`

#`problem 2. In the array.py create an array named 'cars' with the following elements in this order  ---- Ford,Chrysler,Dodge,Ram,Jeep,Chevy,GMC` (use single quotes for each element)EX: 'Ford' not "Ford" spelling matters
   
#`problem 3. print the array to the console`
cars = ['Ford','Chrysler','Dodge','Ram','Jeep','Chevy','GMC']
#problem 4. print the length of the array to the console `
print (cars)
#`problem 5. Append Buick to the Array`
print (len (cars) )
#`problem 6. print the array to the console`
cars.append ('Buick')
#`problem 7. Print the 4th element in the array (Not index 4, element 4)`
print (cars)
#`problem 8. Insert 'Toyota' into element 3 in the array`

print (cars[3])#`problem 9. print the array to the console`
cars.insert(2, 'toyota')
#`problem 10. Remove element 5 of the array (hint look at options for pop())`
print(cars)
#`problem 11. print the array to the console`
cars.pop(4)
#`problem 12. Sort the array in ascending order`
print(cars)
#`problem 13. print the array to the console`
cars.sort()
#`problem 14. Sort the array in descending order`
print(cars)
#`problem 15. print the array to the console`
cars.sort(reverse=True)
#`problem 16. create a variable called my_array_length with a value of the cars array length (spelling, capitilization, and spaces matter)`
print(cars)
#`problem 17. create a variable called array_string with a value of 'The length of my array is ' (spelling, capitilization, and spaces matter)`
my_array_length =len(cars)
#`problem 18. print array_string concatenated with my_array_length to the console.`
array_string = 'the length of my array is'

print(array_string +str(my_array_length))
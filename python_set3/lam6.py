# Code to filter odd numbers from a given list  
list_ = [34, 12, 64, 55, 75, 13, 63]  
odd_list = list(filter( lambda num: (num % 2 != 0) , list_ ))  
print(odd_list)  

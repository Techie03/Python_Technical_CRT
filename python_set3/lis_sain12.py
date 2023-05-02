list=[10,20,10,30,10,40,10,50]
n=10                          
print("original list:")
print(list)         
i=0
length=len(list) 
while(i<length):  
    if(list[i]==n):      
        list.remove(list[i])  
        length=length-1
        continue 
    i=i+1
    print("list after removing elements:")
    print(list)

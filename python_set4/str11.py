# count vowels in a string 
# declare, assign string 
str = "mallareddy is inhyderabad and he is POLITICIAN"
# declare count 
count = 0

# iterate and check each character
for i in str:
	# check the conditions for vowels
	if( i=='A' or i=='a' or i=='E' or i=='e'
	or i=='I' or i=='i' or i=='O' or i=='o'
	or i=='U' or i=='u'):
		count +=1;
		
# print count
print ("Total vowels are: ", count)

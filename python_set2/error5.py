num_list=[]
total=0
try:
    avg=total/len(num_list)
    print("Average:"+avg)
except ZeroDivisionError:
    print ("Zero Division Error occurred")

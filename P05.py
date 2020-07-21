#SOLUTION FOR P05 

#REVERSING A LIST
mylist = ['a','b','c','d','e','f','g']
count = 0
for item in mylist: 	#count the length of list
    count+=1
start=0  		# start of list
end=count-1  	        #end of list
while start<=end:
    mylist[start],mylist[end] = mylist[end],mylist[start]  #Exchange the values of start and end index
    start+=1
    end-=1
print(mylist)

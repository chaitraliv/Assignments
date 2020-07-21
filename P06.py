mylist=['x','a','m','a','x']
start = 0
end = len(mylist)-1
count=0
for item in mylist:
    if mylist[start] == mylist[end]:
        start+=1
        end-=1
        count=1
    else:
        start += 1
        end -= 1
        count-=1

if count > 0:
    print(f'Yes! Given list {mylist} is  a Palindrome !')
else:
    print(f'No! Given list {mylist} is not a Palindrome !')
#P15 (**) Replicate the elements of a list a given #number of times.


mylist=['a','b','c','d','e']
num=int(input('Replicate How many times = '))           #THE NUMBER OF TIMES WE WANT TO REPLICATE
new=[]
for i in mylist:
    new+=i*3                            #IN A NEW LIST MERGE THE REPLICATED COPY OF EVERY ELEMENT OF ORIGINAL LIST
print(new)

#avg of list number
fh = open('pactical4.txt','w')
Num_ls =[6,36,27,11,853,24,2,70]
i=0
sum=0
while i<len(Num_ls):
    sum+= Num_ls [i]
    i+=1
avg=sum/len(Num_ls)
fh.write(f'The average of a list of numbers is: {avg}')
fh.close()

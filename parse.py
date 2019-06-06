instr_name = [] # empty list to store name of instruction
inst = [] # empty list to store complete instruction
z = [] # empty list, dummy
with open("add.disass", "r") as f:
  #print (f.readline())
  #print (f.readline())


  for x in f:
    #print (x.split())
    if(x.split() != []):
      if(x.split()[0][0:3]=='800'):
        #print (x)
        instr_name.append(x.split()[2])
        line_length = len(x)
        z.append(x[33:line_length-1])
        #print(x[34:])

print (instr_name)
#print ("total instructions encountered: " + str(len(instr_name)))
print (z)
for x in z:
  print(x)


##### counting the number of branch instructions in pack of 4 #####
# 
i = 0 # index
count = 0 # stoes total count of branch instructions
count_0 = 0 # number of zero branch instructions in pack of 4
count_1 = 0 # numberr of one branch instructions in pack of 4
count_2 = 0
count_3 = 0
count_4 = 0
total_branch = 0

while(i+4 < len(instr_name)):
    print()
    print()
    print("iteration : " + str(i/4))
    
    for x in instr_name[i : i+4]:
        if(x[0]=='b'):
            print (x)
            count += 1
            total_branch +=1
    if(count == 0):
        count_0 += 1
    
    elif(count == 1):
        count_1 += 1
    
    elif(count == 2):
        count_2 += 1

    elif(count == 3):
        count_3 += 1

    else:
        count_4 += 1

    print("value of counters: {} {} {} {} {} ".format(count_0, count_1,
    count_2, count_3, count_4) )
    i = i + 4
    count = 0
    print("Value of i is : " + str(i))

print("length of instructions is: " + str(len(instr_name))) 
for x in instr_name[i : len(instr_name)]:
    print(x)
    if(x[0]=='b'):
        print(x)
        count += 1
        total_branch += 1
if(count == 0):
     count_0 += 1
    
elif(count == 1):
    count_1 += 1
    
elif(count == 2):
    count_2 += 1

elif(count == 3):
    count_3 += 1

else:
    count_4 += 1   

#print (count)

print("value of counters: {} {} {} {} {} ".format(count_0, count_1,count_2,
count_3, count_4) )

print("total branch: " + str(total_branch))
print("total count: " + str( count_0 * 0 + count_1 + count_2*2 + count_3*3 + count_4*4))
print("match: total branch == sum of count? " + str(total_branch ==
count_0*0 + count_1*1 + count_2*2 + count_3*3 + count_4*4))

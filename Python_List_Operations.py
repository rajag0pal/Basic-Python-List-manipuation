# 1)
# L1=['a1','b2','c3d4']
# Split the number and letters in separate list.
# Ex_Output: [1,2,3,4] and [a,b,c,d]

L1=['a1','b2','c3d4']
string = ' '
for ele in L1:
  string+=ele
string = string.strip()

import re
print(re.findall('\d',string))
re.findall('[a-z]',string)


# 2)
# L2= [8,4,0,4,3,0,0,5,2]
# Ex_Output: [2,3,4,4,5,8,0,0,0]


L2= [0,7,8,7,0,9,7,100,1,28,7]
#Ex_Output: [1, 7, 7, 7, 7, 8, 9, 28, 100, 0, 0]

#Solution:
def custom_sort(l):
  sorted_list = l.sort()
  for i in L2:
    if i>0:
      index = L2.index(i)
      break
  print(L2[index::]+L2[:index])

custom_sort(L2)



# 3)
# L3=['a','b','c','d','e']
# Implement Bigram for above list.


L3=['a','b','c','d','e']
#Implement Bigram for above list.
#Solution: 
Bigram = [] #[['a','b'],['b','c'],['c','d'],['d','e']]
for i in L3:
	current_index = L3.index(i)
	if(L3.index(i) == len(L3)-1):
		break
	else:
		next_index = L3.index(i)+1
		temp = [L3[current_index], L3[next_index]]
		Bigram.append(temp)
Bigram




# 4)
# Customer_Id, Date_of_Purchase, Amount_Of_Purchase
# 1, 12-12-2022, 10
# 2, 12-13-2022, 10
# 1, 12-13-2022, 20

# Assume we have a customer dataframe with above mentioned three columns, have to find
# 4.1) How many times each customers visited the store?
# 4.2) What is the total amount of purchase spend by each customer?

	
# Solution:

import pandas as pd

#4.1
temp = customer_dataframe['Customer_Id'].count_values()
Customer_visit = pd.DataFrame(columns = ['Customer_Id','No.Of.Visits'])
Customer_visit['Customer_Id'] = temp.keys()
Customer_visit['No.Of.Visits'] = temp.values()

#4.2
Customer_Purchase_total = customer_data['Amount_of_Purchase].groupby(by = customer_dataframe['Customer_Id']).sum()





# 5)
# L4=['a','b','c']
# L5 = ['a','b']
# Expected_Output: ['c']


L4=['a','b','c']
L5 = ['a','b']
#Expected_Output: ['c']

#Solution:

difference = []
for i in L4:
	if (i not in L5):
		difference.append(i)

print(difference)




# 6)
# L6=[1,0,1,1,0,0,1,1,0,1,1,0,0,1]
# number of continuous zero stuck with two ones.


L6=[1,0,1,1,0,0,0,1,0,0,1,0,0,1,1,0,0,1]
#number of continuous zero stuck with two ones.
#Solution:

count = 0
i = 1
for i in range(1,len(L6)):
	if(L6[i] == 0 and L6[i+1] == 0):
		if(L6[i-1] == 1 and L6[i+2]):
			count+=1
print(count)





# 7)
# L7=[1,2,3,4,5]
# Ex_Output1=[51234]
# Ex_Output2=[45123]

L7=[1,2,3,4,5]
#Ex_Output1=[51234]
#Ex_Output2=[45123]

def conditional_reverse(l,k):
  print(l[k:]+l[:k])


conditional_reverse(L7, -1)
conditional_reverse(L7, -2)
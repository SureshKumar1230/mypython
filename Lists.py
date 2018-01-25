data1=[1,2,3,4]
data2=['x','y','z']  
print(data1[0]) 
print(data1[0:2])  
print(data2[-3:-1])  
print(data1[0:])  
print(data2[:2])  

#list operator

list1=[10,20]
list2=[30,40]
list3=list1+list2
print(list3)

list1=[10,20,30]
print(list1+[40])

print(list1*2)

list1=[1,2,3,4,5,6,7]
print(list1[0:3])

#appending the list
list1=[34,'z',12]
list1.append("rahul")
print(list1)

#deleting element from the list
list1=[10,'rahul',50.8,'a',20,30]  
print(list1)
del list1[0]  
print(list1)

#find the minimum and maximum element of list

list1=[101,981,32,44,112]  
list2=[21,45,121,100.45,98.2]  
print("Minimum value in List1:")
print(min(list1))  
print("Minimum value in List2:")
print(min(list2)) 

print("Maximum value in List1:")
print(max(list1))  
print("Maximum value in List2:")
print(max(list2)) 

print(len(list1))

data=[832,'abc','a',123.5]
print(data.index(123.5))
print(data.index('a'))

#pop the element from list
data = [786,'abc','a',123.5,786]  
print("Last element is")
print(data.pop())  
print("2nd position element:")
print(data.pop(1)) 
print(data)

#insert the element into list
data = [786,123.5,786]  
pri=data.insert(1,543)
print(pri)

#extend the list of data
data1=['abc',123,10.5,'a']  
data2=['ram',541]  
data1.extend(data2)  
print(data1) 

#remove data from the list
data1=['abc',123,10.5,'a']  
data1.remove('a')  
print(data1)

#reverse list
ist1=[10,20,30,40,50]  
print(list1.reverse())

#sort
list1=[10,50,13]  
l=list1.sort()
print(l)

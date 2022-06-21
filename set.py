colors={"Green","Yellow","Purple"}
for color in colors:
    print(color)
fruits={"Banana","Apple","Lemon"}
for counter,fruit in enumerate(fruits):
    print(fruit)
#using iter 
fruits={"Banana","Apple","Lemon"}
for fruit in iter(fruits):
    print(fruit)
#converting the set to a list then loop through 
#using while loop,
#ccreate variable and loop through length of the set.
cities= {'london', 'new york', 'seattle', 'sydney','chicago'}
country=list(cities)
number=0
while number<len(country):  #printed number and it brought only the indices of the items.
    print(country)        #number to represent each variable of the list 
    number+=1    #to perform same operation for all the items.
for number in range(0,len(country)):   #range represents the starting point and the last point,no need of iteration
    print(country)
#create an empty list and using list comprehension
#print i in the list
newl=[]
newl=[print(city) for city in cities]  
                   #no comma is needed in list comprehension





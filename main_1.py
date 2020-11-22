

dishes = ['real', 'kale chips', 'broccoli', 'pizza','daad']
da = ['faya', 'dada', 'real']
"""
print("Welcome to OnRep")
print("Here are all our dishes:")
print(dishes)

add = input('Enter Y to add something else')
rem = input('Enter N to remove something else')
"""
da_dishes =[]
 
for item in dishes:
    if item  in da:
        da_dishes.append(item)
    print(da_dishes)
         
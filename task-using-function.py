def fruit_list():
  fruit = ['orange', 'mango', 'papaya']
  return fruit

fruit = fruit_list()
for i in range (len(fruit)):
  if fruit[i]  == 'mango':
    fruit[i] ="banana"
    break
  else:
   print("The Previous list is:", fruit)
print("The updated list is", fruit)
'''while True:
    print('being executed')
'''
counter = 0

while counter < 10:
    counter += 1
    print(counter)

counter = 0

while counter < 20:
    counter += 1
    if counter == 15:
        break  #This is how to break the cicle with other condition
    print(counter)


counter = 0

while counter<20:
    counter +=1
    if counter <15:
     continue  #This will jump the execution of the block until the condition is no longer true. Result numbers from 15 to 20
    print(counter)
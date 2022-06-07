people_list = ["Your dentist', Big Brother ,Squirrel"]

comp_list = ["is cool", "is fantastic"]

with open ('People.txt') as f:
    for line in f: 
        l = line.strip()
        people_list.append(l)
        
with open('Compliment.txt') as f: 
    for line in f: 
        l = line.strip()
        comp_list.append(l)
        
import random 
num_people = random.randrange(0,len(people_list)) 
num_comp = random.randrange(0,len(comp_list))

print(people_list[num_people] + " " + comp_list[num_comp])
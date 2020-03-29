#3.1.2.11 LAB: The continue statement - the Pretty Vowel Eater

userWord = input("Enter a word : ")

userWord = userWord.upper()

for letter in userWord:
  if letter == "A":
    continue
  
  if letter == "E":
    continue
  
  if letter == "I":  
    continue
  
  if letter == "O": 
    continue
 
  if letter == "U":
    continue
  print(letter)

#3.1.2.14 LAB: Essentials of the while loop

blocks = int(input("Enter number of blocks: "))

height = 0

layer = 1

while blocks > height:
  height += 1
  blocks -= layer
  layer += 1
  
print("The height of the pyramid:", height)

#3.1.2.15 LAB: Collatz's hypothesis
c0 = int(input("give an integer : "))

steps = 0

while c0 > 1:
  if c0 % 2 == 0:
    c0 = c0 // 2
    
  else:
      c0 = (c0 * 3) + 1
  steps += 1
  print(c0)
print("steps = ", steps)


# 3.1.4.6 LAB: The basics of lists

hatList = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

step_1 = int(input("Give an integer : "))

hatList[2] = step_1

del hatList[-1]

print(len(hatList))
print(hatList)


# 3.1.4.13 LAB: The basics of lists - the Beatles

# step 1
beatles = []
print("Step 1:", beatles)

# step 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# step 3
name = ""
for i in range(2):
    name = input("add a member: ")
    beatles.append(name)
print("Step 3:", beatles)

# step 4

del beatles[-1]
del beatles[-1]
print("Step 4:", beatles)

# step 5

beatles.insert(0, "Ringo Starr")

print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))


#3.1.6.9 LAB: Operating with lists - basics

myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

newList = myList[2:9]
for i in myList:
    if i in newList:
        del myList[i]
print("The list with unique elements only:")
print(myList)



## Charlie Solk's CPU Architecture Quiz

# IMPORTS
from time import sleep as s
import sys,time

# TYPEWRITER ANIMATION
def typewriter(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        s(0.1)

# VARIABLES
intro="Welcome to a quiz on CPU Architecture made by...     the one...     the only...     Charlie Solk!\nThere are 5 questions in this quiz, each worth one mark so good luck!"
end="But I hope you enjoyed my quiz and thanks for having a go at it :)"
q1="1 - What is the shortened term for accumulator?" #ACC
q2="2 - Does MDR stand for Memory Decision Register?" #No
q3="3 - 'The CPU is responsible for _ _ _ _ _ _ _ _ _ _ all the data and instructions in a computer.'" #processing
q4="4 - Is it 'Fetch-Decode-Execute' or 'Fetch-Debug-Execute'?" #Fetch-Decode-Execute
q5="5 - What does ALU stand for?" #Arithmetic Logic Unit
s0="Really, 0! Could you not have done better?"
s1="Ok, well we know you have one strong point"
s2="Not the worst but not the best either."
s3="Around half-way, not too bad."
s4="Wow, quite good."
s5="WELL DONE!"

# INTRODUCTION
typewriter(intro)
print(" ")
print(" ")

# SETTING SCORE TO NONE
score=0

# QUESTION 1
s(1)
typewriter(q1)
q1a=input(": ").upper()
if q1a == "ACC":
    score+=1
    s(0.5)
    print("Correct, the ACC holds the current data being processed.")
    s(3)
    print("Your score =", score)
    s(1)
else:
    s(0.5)
    print("Incorrect, the answer is ACC and the accumulator holds the current data being processed.")
    s(5)
    print("Your score =", score)
    s(1)
print(" ")
    
# QUESTION 2
s(1)
typewriter(q2)
print(" ")
q2a=input("Yes or no: ").lower()
if q2a == "no":
    score+=1
    s(0.5)
    print("Correct, it actually stands for Memory Data Register.")
    s(3)
    print("Your score =", score)
    s(1)
elif q2a == "yes":
    s(0.5)
    print("Incorrect, it actually stands for Memory Data Register.")
    s(3)
    print("Your score =", score)
    s(1)
else:
    s(0.5)
    print("Sorry, that was not a valid answer. Please start again")
    sys.exit()
print(" ")

# QUESTION 3
s(1)
typewriter(q3)
print(" ")
q3a=input("What's the missing word: ").lower()
if q3a == "processing":
    score+=1
    s(0.5)
    print("Correct, the CPU is often referred to as the brain of the computer.")
    s(4)
    print("Your score =", score)
    s(1)
else:
    s(0.5)
    print("Incorrect, the word should have been 'processing'.")
    s(2.5)
    print("Your score =", score)
    s(1)
print(" ")

# QUESTION 4
s(1)
typewriter(q4)
q4a=input(": ").title()
if q4a == "Fetch-Decode-Execute" or q4a == "Fetch Decode Execute":
    score+=1
    s(0.5)
    print("Correct, it can also be called the Fetch-Execute cycle.")
    s(3)
    print("Your score =", score)
    s(1)
else:
    s(0.5)
    print("Incorrect, it's Fetch-Decode-Execute. Debugging is where you go through lines of code to make sure it all works properly.")
    s(8)
    print("Your score =", score)
    s(1)
print(" ")

# QUESTION 5
s(1)
typewriter(q5)
q5a=input(": ").title()
if q5a == "Arithmetic Logic Unit":
    score+=1
    s(0.5)
    print("Correct, the Arithmetic Logic Unit handles the calculations.")
    s(4)
    print("Your score =", score)
    s(1)
else:
    s(0.5)
    print("Incorrect, it stands for Arithmetic Logic Unit.")
    s(2.5)
    print("Your score =", score)
    s(1)
print(" ")

# FINAL SCORE
if score == 0:
    typewriter(s0)
    print(" ")
    typewriter(end)
    sys.exit()
elif score == 1:
    typewriter(s1)
    print(" ")
    typewriter(end)
    sys.exit()
elif score == 2:
    typewriter(s2)
    print(" ")
    typewriter(end)
    sys.exit()
elif score == 3:
    typewriter(s3)
    print(" ")
    typewriter(end)
    sys.exit()
elif score == 4:
    typewriter(s4)
    print(" ")
    typewriter(end)
    sys.exit()
elif score == 5:
    typewriter(s5)
    print(" ")
    typewriter(end)
    sys.exit()
else:
    sys.exit()

print("Welcome to the quiz")
decision = input("Are you ready to play? yes/no  ")
if decision != "yes":
    quit()
print("The answers are case sensitive.")
print("Mind the spacing")

cnt = 0

answer = input("What stands for JSON? ")
if answer == "javascript object notation":
    print("Correct!")
    cnt+= 1
else:
    print("Incorrect!")

answer = input("What is the square root of variance is called? ")
if answer == "standard deviation":
    print("Correct!")
    cnt+= 1
else:
    print("Incorrect!")

answer = input("Who is the CEO of Devin AI? ")
if answer == "scott wu":
    print("Correct!")
    cnt+= 1
else:
    print("Incorrect!")

answer = input("Which organization developed the chatbot chatgpt? ")
if answer == "openai":
    print("Correct!")
    cnt+= 1
else:
    print("Incorrect!")

answer = input("What does CNN stand for? ")
if answer == "convolutional neural network":
    print("Correct!")
    cnt+= 1
else:
    print("Incorrect!")

print("You got",cnt,"question(s) correct!")
print("and",5-cnt,"question(s) incorrect!")
print("You Obtained",(cnt/5)*100,"% marksyes!")

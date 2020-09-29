print ("Input the scores for your classes") #Giving instructions in the heading
print() #Creating space between heading and first input    
count = 0 #Declaring variable
total = 0 #Declaring variable

while count < 5: #Initiating while loop
    user = input("What was your score: ")
    value = int(user)
    count = count + 1 #Arithmetical operators
    total = total + value #Arithmetical operators

avg = total/count #Performing calculations

if 97 <= avg <= 100: #Stating conditions for if-elif-else statement
    print("For an average score of " + str(avg) + ", Your grade is A+")
elif 94 <= avg <= 97:
    print("For an average score of " + str(avg) + ", Your grade is A")
elif 90 <= avg <= 94:
    print("For an average score of " + str(avg) + ", Your grade is A-")
elif 87 <= avg <= 90:
    print("For an average score of " + str(avg) + ", Your grade is B+")
elif 84 <= avg <= 87:
    print("For an average score of " + str(avg) + ", Your grade is B")
elif 80 <= avg <= 84:
    print("For an average score of " + str(avg) + ", Your grade is B-")
elif 77 <= avg <= 80:
    print("For an average score of " + str(avg) + ", Your grade is C+")
elif 74 <= avg <= 77:
    print("For an average score of " + str(avg) + ", Your grade is C")
elif 70 <= avg <= 74:
    print("For an average score of " + str(avg) + ", Your grade is C-")
elif 67 <= avg <= 70:
    print("For an average score of " + str(avg) + ", Your grade is D+")
elif 64 <= avg <= 67:
    print("For an average score of " + str(avg) + ", Your grade is D")
elif 60 <= avg <= 64:
    print("For an average score of " + str(avg) + ", Your grade is D-")
elif 0 <= avg <= 60:
    print("For an average score of " + str(avg) + ", Your grade is F")
else:
    print("Cannot compute")

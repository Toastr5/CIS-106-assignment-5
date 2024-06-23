start = str(input("Do you want to start grade average calculator? (y/n): ")) #First prompt
total_users = 0 #Total users

while start == "n": #If user says no, program will prompt again
  start = str(input("Do you want to start grade average calculator? (y/n): "))

while start == "y": #if user says yes execute program
  name = str(input("Enter your name: "))
  score1 = float(input("Enter exam score 1: "))
  score2 = float(input("Enter exam score 2: "))
  ave_score = (score1 + score2)/2
  total_users = total_users + 1
  print(f"The average score for {name} is {ave_score} \n and total users is {total_users}")
  start = str(input("Do you want to start grade average calculator? (y/n): "))
       
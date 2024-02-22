total_class = int(input("Total class of the season: "))
attened =int(input("Student attendence of that season: "))
parcentage = (attened*100)/total_class
if parcentage >=75:
    print("Student will be allowed to sit in the exam")
else:
    print("Studet will not be allowed to sit in the exam")
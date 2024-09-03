def cgpaCalculator():
	Total = 0
	Grade = 0
	course = int(input("Please Enter the number of Courses you Offered: "))
	for x in range(course):
		Course1 = input("Enter The Course code:")
		gradepoints = int(input ("Points of course: "))
		score = int(input("Enter your Score:"))
		print ("------------")

		Total += gradepoints* 5
		if (score >= 95):
			grade = 10
		elif(score < 95 and  score > 90):
			grade = 9 
		elif(score < 90 and  score > 85 ):
			grade = 8
		elif(score < 85 and  score > 70):
			grade = 7
		elif (score < 70 and  score> 65):
			grade = 6
		else :
			grade = 0 


		Grade += gradepoints*grade

	Cgpa =float((Grade / Total) * 5)
	print("THANKS FOR ALL YOUR INPUT YOUR CGPA IS : " + str(Cgpa))


cgpaCalculator()

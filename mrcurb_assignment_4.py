student_name = "Mariyah Curb"  # Replace with your actual name
current_gpa = 3.04 # Float between 1.0-4.0
study_hours = int(20) # Integer (Ex. 25)
social_points = int(85) # Integer (Ex. 50)
stress_level = int(60) # Integer 0-100

# Display Welcome Stats

print(f"------ Welcome {student_name} ------")
print("")
print(f"    ---- Your Stats Are: ----")
print("")
print(f"        Current GPA: {current_gpa:.1f}")
print(f"        Study Hours: {study_hours}")
print(f"        Social Points: {social_points}")
print(f"        Stress Level: {stress_level}")

#My mom loves Harry potter this is for you Mum!
print(f"Choose your Wizardy Path!:")
print(f"A). Potions (Moderate)")
print(f"B). SpellCaster (Difficult)")
print(f"C). Curses (Brutal)")

choice = input("Your choice: ")

if choice == "A" or choice == "a":
    #path = potions
    if current_gpa >= 2.7:
        stress_level += 8
        study_hours +=4
    elif current_gpa < 2.7:
        stress_level += 15
        study_hours += 8
elif choice == "B"or choice == "b":
    #path = spells
    if current_gpa >= 3.0:
        stress_level += 8
        study_hours +=4
    elif current_gpa < 3.0:
        stress_level += 15
        study_hours += 8
elif choice == "C"or choice == "c":
    if current_gpa >= 3.5:
        stress_level += 8
        study_hours += 4
    elif current_gpa < 3.5:
        stress_level += 15
        study_hours += 8
    #path = curses
else:
    print("Invalid choice, Please Restart")

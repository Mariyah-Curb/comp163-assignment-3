student_name = "Mariyah Curb"  # Replace with your actual name
current_gpa = 3.04 # Float between 1.0-4.0
study_hours = int(20) # Integer (Ex. 25)
social_points = int(75) # Integer (Ex. 50)
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

choice = input("Type A, B, or C to make your choice: ")

path = None

if choice == "A" or choice == "a":
    path = "potions"
    if current_gpa >= 2.7:
        stress_level += 3
        study_hours += 2
    elif current_gpa < 2.7:
        stress_level += 6
        study_hours += 4
elif choice == "B"or choice == "b":
    path = "spells"
    if current_gpa >= 3.0:
        stress_level += 6
        study_hours += 4
    elif current_gpa < 3.0:
        stress_level += 10
        study_hours += 6
elif choice == "C"or choice == "c":
    path = "curses"
    if current_gpa >= 3.5:
        stress_level += 9
        study_hours += 6
    elif current_gpa < 3.5:
        stress_level += 12
        study_hours += 8
else:
    print("Invalid choice, Please Restart")

classes = None

# make specific classes for specific paths
if path == "potions":
    classes = ["Concoctions 339", "Mixtures 220", "Gases 100"]
elif path == "spells":
    classes = ["Lumos 101", "Bookestry 200", "Motions 343"]
    #Love the harry potter reference mariyah, thanks mariyah!
elif path == "curses":
    classes = ["Ouija 118", "Dark Magic 300", "Hatre 252"]

print("")
print(f"Here are your classes: {classes}")
print("")
focus_class = input("Type out your class of focus (Make sure to include the number):   ")
#print(focus_class)
print("")
print(focus_class)
print("")
if " " in focus_class and "3" in focus_class and "Error" not in path:
    #check study hours if they are good +++GPA --Social Points else --GPA -Social points +20 stress
    print("this is a hard class, I hope you have the stats to handle this...")
    print("")
    if current_gpa >= 3.2 and study_hours >= 20:
        print("Looks like you can handle it! Your gpa increases but you rarely go outside now Decreased social.")
        current_gpa += 0.2
        social_points -= 10
        stress_level += 5
    elif current_gpa < 3.2:
        print("Yikes you don't study enough to handle this class, You make time to chat in class but not to finish dem assignments.")
        current_gpa -= 0.1
        social_points -= 5
        stress_level += 20

elif "2" in focus_class:
    if current_gpa >= 2.9:
        print("A perfect balance! you handle this class very well but still don't go outside...")
        current_gpa += 0.1
        social_points -= 8
        stress_level - 5
    elif current_gpa <= 2.8 and social_points >= 60:
        print("")
        print("You stuggle but because of your social skills you share the burden with your wizardy peers")
        social_points += 10
        stress_level -= 10
    #Less study hours required but less GPA gained

elif "1" in focus_class:
    #GPA stays the same Depending on class determines how many social points can be obtained
    if current_gpa >= 2.6:
        print("You have the stats for this class but you get over confident and slack on study hours.")
        stress_level -= 10
        social_points += 5
        study_hours -= 8
        print("")
    elif current_gpa < 2.6 and social_points < 95:
        print("You struggle in the easiest class, your peers make fun of you and this stresses you out from embarrassment")
        stress_level += 15
        social_points -= 10
        print("")
    else:
        print("Taking the easy way out huh? that doesnt always work out... Abracadabra (A spell has been casted on your GPA)")
        current_gpa -= 0.3
else:
    print("Error: Please start over")

print("")

print("It's time for your last class of the day! Its a Pathwide Lecture for:")
print("")
if "1" or "2" or "3" in next_class:
    print(path)
    print("")
    print("You need to show off for your last class. What Skill will you show off?")
    option_1 = "Turn someone into a frog"
    option_2 = "Create a potion of invisibility"
    option_3 = "Summon the ghost of Duke Ellington"
    #Okay this is 100% necessary!!!
    print(f"Option 1: {option_1}, Option 2: {option_2}, Option 3: {option_3}")

project = input("Type 1, 2, or 3")
#Used Ai gemini to debug a issue here, I called the input fuction too many times

if "1" in project and path == "spells":
    print("Good job, Harry Potter would love you")
elif "2" in project and path =="potions":
    print("pills and potions...we overdosing... On good grades!!!")
elif "3" in project and path == "curses":
    print("Nice Job! and a Bibodi Boppidi BOO")
else:
    print("There was a better choice here...")
print("")
stats = [current_gpa, study_hours, social_points, stress_level]
Noads_Toads = False
fail = False
star_student = False

if stats[3] >= 90 or stats[2] <= 60:
    print("Oh no you're either too lonely or stressed, you now have Noads and Toads (Witch terms for depression)")
    Noads_Toads = True
elif stats[2] > 80 and stress_level < 65 and current_gpa < 2.6:
    print(" You may think that you had fun and made friends but I'm afriad that's simply not enough")
    fail = True
elif path == "curses" and current_gpa >= 3.0:
    print("You are one Heck of a wizard... I'm gonna break the fourth way and say Mariyah is truly proud if you took this path <3 it's the hardest honor to achieve")
    star_student = True

print("")

#Endings
print(f" GPA: {stats[0]}, Study Hours: {stats[1]}, Social points: {stats[2]}, Stress: {stats[3]}")
if Noads_Toads is not False:
    print(f"Depression: {Noads_Toads}")
    print(f"Oh no you had to drop out...yikes lock in next year")
elif star_student == True:
    print(f"Star Student: {star_student}")
elif fail == True:
    print(f"Failed Wizard School: {fail}")
else:
    print("You choose a normal path try again and see what lies in store for you future wizard")



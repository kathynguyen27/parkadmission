#Kathy Nguyen
#PM
#Theme Park Admission & Ride Eligibility System

#Below is the program introduction where we're collecting info through inputs and whatnot
print("=======================================================")
print("Welcome honored guest to Awesome Sauce park!")
print("We're so lucky to have you today, let's get your ticket!")
print("Your ticket will tell you what rides you can go on, so let's start")
print("-------------------------------------------------------")
guest_name = input("What is your name?: ")
age = int(input("How old are you?: "))
height = int(input("How tall are you in inches?: "))
ticket_type = input("What type of ticket do you plan on buying? Regular or Premium?: ")
park_member = input("Are you a park member (Yes or No)?: ")
adult_present = input("Are you visiting with an adult (Yes or No):  ")
visit_time = input("Are you visiting during the Morning or Evening?: ")
#function is calculate admission
#parameter is age
#can set something for a variable as place holder (the line below has no value)
admission_price = 0

#Calculating the admission price through this function
#Using intervals of age
#DONT FORGET COLON
def calculate_admission(age):
    if 0 <= age <=4:
        admission_price = 0
    elif 5 <= age <= 12:
        admission_price = 15
    elif 13 <= age <= 64:
        admission_price = 30
    else:
        admission_price = 20

    return admission_price
#always make sure when you call function to NOT have it idented
admission_price = calculate_admission(age)

#Calculate discount based off membership and visit time
def calculate_discount(admission_price, park_member, visit_time):
    discount_price = 0
#check if they are a park member
#put the conditions that require the most FIRST so they check that first before going to the more simple ones
#in this case age <= 4 is only first because we NEED this to be checked first, but other wise the point above applies
    if age <= 4:
            discount_price = admission_price
    elif park_member == "Yes" and visit_time == "Evening":
            discount_price = admission_price - 10
    elif park_member == "Yes" :
        discount_price = admission_price - 5
    elif park_member == "No":
        discount_price = admission_price
    #evening or morning
    elif visit_time == "Evening":
        discount_price = admission_price - 3
    elif visit_time == "Morning":
        discount_price = admission_price
        #special discount
    
    return discount_price
discount_price = calculate_discount(admission_price, park_member, visit_time)
#always definee

#Ride eligibility function, works the same as admission but we return a message instead of defining a number.
#Again, more req -> higher up in the function
def ride_level(age, height):
#Extreme ride
    if height >= 54 and age >= 16:
        return "Extreme rides"
#Thrill ride
    elif height >= 42 and age >= 8 :
        return "Thrill Rides"
    #no ride
    elif height <= 36:
        return "No rides"
    #kid ride
    elif 42 > height >= 36 :
       return "Kids Rides"
   
ride_level = ride_level(age, height)

#adult supervision
#just check answer is yes or no
#more req at the top
def check_supervision (age, adult_present):
    if age < 13 and adult_present == "No":
        return "Adult required"
    elif age < 13 and adult_present == "Yes":
        return "Approved"
    elif age > 13:
        return "Approved"
adult_present = check_supervision(age, adult_present)
    

#premium bonus
#must use the seperate check premium variable because ticket type is already defined and needs to be printed out differently
#INDENTT
def check_premium (ticket_type):
    if ticket_type == "Premium":
        return "PREMIUM PERK: Your ticket will come with a bonus meal and the fast line pass! :D"
    if ticket_type == "Regular":
        return "Enjoy your trip :D"
check_premium = check_premium(ticket_type)

#additional comments
#basically using ride level, but can't really choose like Extreme rides, so we just take the requirement that extreme rides qualified for and use that
def special_message (height, age):
    if height >= 54 and age >= 16:
        return "Have a great time on the EXTREMEEE rides! Don't barf!"
#gatekeeping for those who are in extreme rides
    else:
        return ""
special_message = special_message(height, age)

#final report

print("===============================")
print("AWESOME SAUCE PARK RECIEPT")
print("===============================")
print(" ")
print("Guest name: ", guest_name)
print("Height: ", height, "inches")
print("Age: ", age, "years old")
print("Ticket type: ", ticket_type)
print("Park Member: ", park_member)
print(" ")
print("Regular Admission: $", admission_price )
print("Discounted Price: $", discount_price)
print(" ")
print("Highest Ride Level:", ride_level)
print("Adult Supervision: ", adult_present)
print("----------------------------")
#final personalized messages
print(check_premium)
print(special_message)
print("THANK YOU FOR VISITING AWESOME SAUCE PARK")
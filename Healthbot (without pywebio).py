import math
import time
print("Welcome to Virtual Medical Check-Up")
print("Kindly Note: This virtual health check-up is not for Athletes, Pregant Womens, Baby with less than 5 years and Old Person with more than 85 years. Under above cases, check-up report will be inappropriate.")
print("This Virtual Check-Up will give result based on your choices and it doesn't guarantee the medical opinion. Check-Up is for informational purpose. In case of emergency, call your local emergency number immediately.")
print("So, Let's start with the check-up. Before that I need some of your basic details.")
name=input("What is your good name? ")
print("*"*20)
age=int(input("How old are you? "))
if age<5:
	print("Sorry! This check-up isn't for babies.")
elif age>85:
	print("Sorry! This check-up isn't for old peoples.")
else:
	age=age

print("*"*25)
#Asking user for height.
while True:
	height=float(input("Please enter your height in meter(not cm): "))
	if height>2.75 or height<0.1:
		print("Humans can't have such height. Please enter correct height. Make sure you are entering height in meters.")
		continue
	break
print("*"*30)
weight=float(input("Please enter your weight in kg: "))

#Gender
print("*"*35)
print("Please specify your gender. Enter M/F to indicate whether you are Male or Female.")
while True:
  gender=str(input("Enter M for Male and F for Female: "))
  if gender=="M" or gender=="m" or gender=="F" or gender=="f":
    print(gender)
  else:
    print("Please enter either M or F to indicate gender.")
    continue
  break

#Initialize the points as zero
points=0
print("*"*40)
#Asking for Temperature. Increasing points if Temperature is low or high else no points will be given for normal temperature.
while True:
  temp = input("Please enter your Body Temperature in Celcius: ")
  try:
    temp = float(temp)
  except ValueError:
    print("This is not a valid number, Please enter your temperature in numbers.")
    continue
  if temp > 45 or temp <25:
    print("Humans can't tolerate such temperature. Make sure you are entering temperature in Celcius.")
    continue
  break
if temp > 37.6:
  points += 1
  tempr= "Your temperature is quite high than normal."
elif temp < 36.4:
  points += 1
  tempr= "Your temperature is quite low than normal."
else:
  tempr="Great! Your temperature is normal."
  points=points

print("*"*45)
#Asking for Respiratory Rate
print("What is your Respiratory or Breath Rate?")
print("Respiratory Rate is the number of Breath you take per minute. You can calculate if you don't know.")

#Asking for Breathe Rate and then giving points if it is greater than 20.
while True:
  resprate = input("Please enter your Respiratory Rate: ")
  try:
    resprate = int(resprate)
  except ValueError:
    print("This is not a valid number, Please enter your temperature in numbers.")
    continue
  break
if resprate > 20:
  points += 1
  print("It seems you are breating fast.")
else:
  points=points

#Since there is positive relation with heart and breathe rate, we will calculate the breate rate using resprate.
heartrate=math.ceil(5.67*resprate)
if heartrate>100 or heartrate<60:
	points+=1
else:
	points=points

#Calculating Body Mass Index using h and w.
bmi=weight/height**2

#Getting BMI Status
if bmi<18.5:
	points+=1
	bmi_status="Your Body to Mass Index is Low. That means you are Underweighted"
elif bmi>25 and bmi<=30:
	points+=1
	bmi_status="Your Body to Mass Index is High. That means you are Overweight"
elif bmi>30:
	points+=2
	bmi_status="Your Body to Mass Index is Very High. That means you are Obese"
else:
	points=points
	bmi_status="Your Body to Mass Index is normal. That means you are fit"

#Calculating Lean Body Mass
if gender=="M" or gender=="m":
	lbm=(0.32810*weight)+(33.929*height)-29.5336
elif gender=="F" or gender=="f":
	lbm==(0.29569*weight)+(41.813*height)-43.2933

#Calculating Basal Metabolic rate
if gender=="M" or gender=="m":
	bmr=5+(10*weight)+(625*height)-(5*age)
else:
	bmr=(10*weight)+(625*height)-(5*age)-161

print("*"*50)
#Asking for Breath Hold rate?
print("How long can you hold your breath?")
breath=int(input("Enter number of seconds you can hold your breath: "))
if breath<30 or breath>240:
	points+=1
else:
	points=points

print("*"*55)
#Exercise Habitat
print("How often you do Exercise/Work-outs?")
while True:
	print("Enter 1 if you do Little/No Exercise.")
	print("Enter 2 if you do Moderate/Regular Exercise.")
	print("Enter 3 if you do Active/High Exercise.")
	exercise=int(input("Enter 1, 2 or 3 based on your exercise habitat: "))
	if exercise==1:
		points+=1
		calories=bmr*1.2
	elif exercise==2:
		points-=1
		calories=bmr*1.55
	elif exercise==3:
		points-=2
		calories=bmr*1.9
	else:
		print("The given number is not valid. Try Again")
		continue
	break

print("*"*60)
#Calculating the chances of Type - 2 Diabetes
print("How many of your family members have Diabetes?")
print("Enter 0 if none of your member has Diabetes.")
diabetes=int(input("Number of people(s) in your family having Diabetes: "))
if bmi>25:
	dscore= 19
elif bmi>25 and age>65:
	dscore=52
elif bmi>25 and age>65 and exercise==1:
	dscore=65
elif age<65 or age>45:
	dscore=19
elif diabetes==1 or diabetes==2 and age>45:
	dscore=22
elif diabetes>2 and age>45:
	dscore=28
else:
	dscore=0

#Increasing points based on chances of dscore
if dscore>33:
	points+=1
else:
	points=points

print("*"*65)
print("Please answer the following question accurately. Enter Y for Yes and N for No")

#CoronaVirus Points (CPoints)
cpoints=0
while True:
	q1=input("Do you have cholesterol? ")
	if q1=="Y" or q1=="y":
		points+=1
	elif q1=="N" or q1=="n":
		points=points
	else:
		print("Enter only Y or N to answer the questions.")
		continue
	q2=input("Do you have White spots on your nails? ")
	if q2=="Y" or q2=="y":
		points+=1
	elif q2=="N" or q2=="n":
		points=points
	else:
		print("Enter only Y or N to answer the questions.")
		continue
	q3=input("Have you got new or strange rashes? ")
	if q3=="Y" or q3=="y":
		points+=1
	elif q3=="N" or q3=="n":
		points=points
	else:
		print("Enter only Y or N to answer the questions.")
		continue
	q4=input("You feel tired all the time? ")
	if q4=="Y" or q4=="y":
		points+=1
	elif q4=="N" or q4=="n":
		points=points
	else:
		print("Enter only Y or N to answer the questions.")
		continue
	q5=input("Do you get headache or fever frequently? ")
	if q5=="Y" or q5=="y":
		points+=1
	elif q5=="N" or q5=="n":
		points=points
	else:
		print("Enter only Y or N to answer the questions.")
		continue
	q6=input("Have you got cold and cough within last month? ")
	if q6=="Y" or q6=="y":
		cpoints+=1
	elif q6=="N" or q6=="n":
		cpoints=cpoints
	else:
		print("Enter only Y or N to answer the questions.")
	q7=input("Have you experienced Difficuly in breathing within the last month? ")
	if q7=="Y" or q7=="y":
		cpoints+=1
	elif q7=="N" or q7=="n":
		cpoints=cpoints
	else:
		print("Enter only Y or N to answer the questions.")
	q8=input("Have you experienced fever in the last month? ")
	if q8=="Y" or q8=="y":
		cpoints+=1
	elif q8=="N" or q8=="n":
		cpoints=cpoints
	else:
		print("Enter only Y or N to answer the questions.")
	q9=input("Do you have/had Lung or Heart or Kidney Diease? ")
	if q9=="Y" or q9=="y":
		cpoints+=2
	elif q9=="N" or q9=="n":
		cpoints=cpoints
	else:
		print("Enter only Y or N to answer the questions.")
	q10=input("Have you traveled anywhere internationally in the last 28-45 days? ")
	if q10=="Y" or q10=="y":
		cpoints+=2
	elif q10=="N" or q10=="n":
		cpoints=cpoints
	else:
		print("Enter only Y or N to answer the questions.")
	q11=input("Do you work in Hospitals/NGO/Healthcare/Nursing Home? ")
	if q11=="Y" or q11=="y":
		cpoints+=2
	elif q11=="N" or q11=="n":
		cpoints=cpoints
	else:
		print("Enter only Y or N to answer the questions.")
	q12=input("Have you got in contact with COVID-19 Person or Doctors? ")
	if q12=="Y" or q12=="y":
		cpoints+=2
	elif q12=="N" or q12=="n":
		cpoints=cpoints
	else:
		print("Enter only Y or N to answer the questions.")
	break

if age>40 and cpoints>6:
	cresult="High"
elif age>40 and cpoints>3:
	cresult="Moderate"
elif age<40 and cpoints>6:
	cresult="Moderate"
else:
	cresult="Low"

#Calculating average protien, fats a person needs based on thier weight.
protein=math.ceil(0.8*weight)
fat_min=math.ceil(0.882*weight)
fat_max=math.ceil(1.102*weight)
water=math.ceil((1.55*weight)/33.8)

print("*"*100)
print("Analyzing your Virtual Health Check-Up Report. Please wait.....")
while True:
	time.sleep(6)
	print("Name: ",name)
	print("Age: ",age)
	print("Height: ",height,"m")
	print("Weight: ",weight,"kg")
	if gender=="M" or gender=="m":
		print("Gender: Male")
	else:
		print("Gender: Female")
	print("Temperature: ",temp,"Celcius")
	print(">> ",tempr)
	print("Respiratory Rate: ",resprate,"breath per minute")
	print("Heart Rate: ",heartrate,"heartbeats per minute")
	print("BMI: ",bmi)
	print(">> ", bmi_status)
	print("LBM: ",lbm,"kg")
	print("BMR: ",bmr,"calories/day")
	print(">> Based on your Basal Metabolic Rate, you need {} calories intake to maintain the current weight.".format(calories))
	print("Diabetes Score: ",dscore)
	print(">> You have {}% chances of developing Type-II Daibetes.".format(dscore))
	print(">> You need {}gm protein on daily basis.".format(protein))
	print(">> You need to consume {}gm to {}gm of fats on daily basis.".format(fat_min, fat_max))
	print(">> You need to drink {} liters of water daily to stay fit.".format(water))
	print("Corona Virus Score: ",cresult)
	if cresult=="High":
		print(">> Well, it doesn't mean you have COVID-19 but it is highly recommended that you get your COVID-19 Checkup. Stay Home and get yourself quarantined for 14 days and monitor your symptoms regularly.")
	elif cresult=="Moderate":
		print(">> You are somewhat exposed to COVID-19. It's better if you get yourself checked for COVID-19. Stay home and get yourself quarantined and wash hands regularly. Don't forget to monitor your symptoms on daily basis.")
	elif cresult=="Low":
		print(">> Your infection risk is low. But it is recommended to stay home and avoid public contact. Wash Hands and Monitor your symptoms on regular basis.")

	print("Fitness Score: ",points)
	if points<2:
		print(">> Great, Your score is good. You are fit and live a healthy life. Make sure to continue your exercise and take the suggested protein and fats intake.")
	elif points<6:
		print(">> You're somewhat fit, but if you continue to live like this, you will develop some of the serious symptoms in your old age.")
	elif points<10:
		print(">> You're unhealthy and if live like this you will develop serious symptoms soon. Take the suggested proteins and fats and do some regular exercise to get fit.")
	else:
		print(">> You're already unfit and you need to start exercising from now! Living the same life will lead you very serious issues in the future and your life expectancy will be reduced too. You need to wake up and start to work-out from now!")
	break

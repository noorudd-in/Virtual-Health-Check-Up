from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from pywebio.exceptions import SessionClosedException
import argparse

import math
import time

def virtualcheckup():
    put_html('<center><h2><br>Created by <a href="https://www.linkedin.com/in/nooruddin-shaikh/">Nooruddin Shaikh</a>'
             '<br>Source code: <a href="https://github.com/noor12401/Virtual-Health-Check-Up">GitHub</a></h2></center>')
    put_text("Welcome to Virtual Medical Check-Up. \n"
             "This Virtual Check-Up will give result based on your choices and it doesn't guarantee the medical opinion. \n"
             "Kindly Note: This virtual health check-up is not for Athletes, Pregant Womens, Baby with less than 5 years and Old Person with more than 85 years. \n"
             "Under above cases, check-up report will be inappropriate." )
    checkbox('User Terms', options=['I understand that Check-Up is for informational purpose.',
                                    'In case of emergency, I will call the local emergency number and will consult the doctor.'])
    put_text("So, Let's start with the check-up. Before that I need some of your basic details.")


    def check_age(a):
        if a < 5:
            return 'Sorry! You are too young for this checkup'
        if a > 75:
            return 'Sorry! You are too old for this checkup'


    def check_height(b):
        if b < 0.1 or b > 2.75:
            return 'Please enter height in meters not in cm'

    basic_info = input_group('Basic Information',
                             [input('Enter your name: ', name='name'),
                              input('Enter your age', name='age', type=NUMBER, validate=check_age),
                              input('Enter your height (in meters)', name='height', type=FLOAT, validate=check_height),
                              input('Enter you weight (in kg)', name='weight', type=NUMBER),
                              ])
    gender = select('What is your gender', options=['Male', 'Female'])


    def check_temp(c):
        if c > 45 or c < 25:
            return 'Humans cannot tolerate such temperature. Enter correct temperature in celcius.'

    #Starting Points so calculate score
    points = 0

    #Main Program Starts
    rate = input_group('Some more info', [
        input("Please enter your Body Temperature in Celcius: ", name='temp', type=FLOAT, validate=check_temp),
        input('What is your Respiratory or Breath Rate?', name='resp', type=NUMBER,
              help_text="Respiratory Rate is the number of Breath you take per minute. You can calculate if you don't know."),
        input('How long can you hold your breath?', name='breathhold', type=NUMBER,
              help_text='Enter number of seconds you can hold your breath')])

    #If breath rate is not normal, increase the point
    if rate['resp'] > 20:
        points += 1
    else:
        points = points

    #If person cannot hold breath for atleast more than 30 seconds, means has a bad lung so increase a point
    if rate['breathhold'] < 30 or rate['breathhold'] > 240:
        points += 1
    else:
        points = points

    #If temperature is not normal, increase the point
    if rate['temp'] > 37.6:
        points += 1
        tempr = "Your temperature is quite high than normal."
    elif rate['temp'] < 36.4:
        points += 1
        tempr = "Your temperature is quite low than normal."
    else:
        tempr = "Great! Your temperature is normal."
        points = points

    #If heart rate is too high or too low, increase the point
    heartrate = math.ceil((5.67 * rate['resp']))
    if heartrate > 100 or heartrate < 60:
        points += 1
    else:
        points = points

    #If BMI is Obese or Underweight means bad deit so increase a point
    bmi = basic_info['weight'] / basic_info['height'] ** 2
    if bmi < 18.5:
        points += 1
        bmistatus = "Your Body to Mass Index is Low. That means you are Underweighted"
    elif bmi > 25 and bmi <= 30:
        points += 1
        bmistatus = "Your Body to Mass Index is High. That means you are Overweight"
    elif bmi > 30:
        points += 2
        bmistatus = "Your Body to Mass Index is Very High. That means you are Obese"
    else:
        bmistatus = "GYour Body to Mass Index is normal. That means you are fit"
        points = points

    #Calculating LBM for different genders
    if gender == 'Male':
        lbm = (0.32810 * basic_info['weight']) + (33.929 * basic_info['height']) - 29.5336
    else:
        lbm = (0.29569 * basic_info['weight']) + (41.813 * basic_info['height']) - 43.2933

    # Calculating BMR for different genders
    if gender == 'Male':
        bmr = 5 + (10 * basic_info['weight']) + (625 * basic_info['height']) - (5 * basic_info['age'])
    else:
        bmr = (10 * basic_info['weight']) + (625 * basic_info['height']) - (5 * basic_info['age']) - 161

    popup('Rapid Fire', 'Get ready for rapid fire questions.')

    q1 = radio('How often you do Exercise/Work-outs?',
               options=['I do Little/No Exercise', 'I do Moderate/Regular Exercise',
                        'I do Active/High Exercise'])
    if q1 == 'I do Little/No Exercise':
        points += 1
        calories = bmr * 1.2
    elif q1 == 'I do Moderate/Regular Exercise':
        points -= 1
        calories = bmr * 1.55
    else:
        points -= 2
        calories = bmr * 1.9

    #If person is overweight and has daibetes then it's worse case.
    q2 = input("How many people(s) in your family have Diabetes?", type=NUMBER)
    if bmi > 25:
        dscore = 19
    elif bmi > 25 and basic_info['age'] > 65:
        dscore = 52
    elif bmi > 25 and basic_info['age'] > 65 and exercise == 1:
        dscore = 65
    elif basic_info['age'] < 65 or basic_info['age'] > 45:
        dscore = 19
    elif q2 == 1 or q2 == 2 and basic_info['age'] > 45:
        dscore = 22
    elif q2 > 2 and basic_info['age'] > 45:
        dscore = 28
    else:
        dscore = 0

    #Based on different condition calculate dscore and identify person is health or not
    if dscore > 33:
        points += 1
    else:
        points = points

    q3 = radio("Do you have cholesterol?", options=['Yes', 'No'])
    if q3 == 'Yes':
        points += 1
    else:
        points = points
    q4 = radio("Do you Smoke or Drink?", options=['Yes', 'No'])
    if q4 == 'Yes':
        points += 1
    else:
        points = points
    q5 = radio("Have you gone through major surgeries related to heart or brain?", options=['Yes', 'No'])
    if q5 == 'Yes':
        points += 1
    else:
        points = points
    q6 = radio("Do you feel tired all the time?", options=['Yes', 'No'])
    if q6 == 'Yes':
        points += 1
    else:
        points = points
    q7 = radio("Do you get headache or fever frequently?", options=['Yes', 'No'])
    if q7 == 'Yes':
        points += 1
    else:
        points = points

    popup('COVID-19 Test',
          'Thanks for answering the rapid fire questions. You now need to answer below questions for virtual COVID test.')

    #All the questions were taken by Arogya Setu App
    cpoints = 0
    q8 = radio("Have you got cold and cough within last month?", options=['Yes', 'No'])
    if q8 == 'Yes':
        cpoints += 1
    else:
        cpoints = cpoints
    q9 = radio("Have you experienced Difficuly in breathing within the last month?", options=['Yes', 'No'])
    if q9 == 'Yes':
        cpoints += 1
    else:
        cpoints = cpoints
    q10 = radio("Have you experienced fever in the last month?", options=['Yes', 'No'])
    if q10 == 'Yes':
        cpoints += 1
    else:
        cpoints = cpoints
    q11 = radio("Do you have/had Lung or Heart or Kidney Diease?", options=['Yes', 'No'])
    if q11 == 'Yes':
        cpoints += 1
    else:
        cpoints = cpoints
    q12 = radio("Have you traveled anywhere internationally in the last 28-45 days?", options=['Yes', 'No'])
    if q12 == 'Yes':
        cpoints += 1
    else:
        cpoints = cpoints
    q13 = radio("Do you work in Hospitals/NGO/Healthcare/Nursing Home?", options=['Yes', 'No'])
    if q13 == 'Yes':
        cpoints += 1
    else:
        cpoints = cpoints
    q14 = radio("Have you got in contact with COVID-19 Person or Doctors?", options=['Yes', 'No'])
    if q14 == 'Yes':
        cpoints += 1
    else:
        cpoints = cpoints

    if basic_info['age'] > 40 and cpoints > 6:
        cresult = "High"
    elif basic_info['age'] > 40 and cpoints > 3:
        cresult = "Moderate"
    elif basic_info['age'] < 40 and cpoints > 6:
        cresult = "Moderate"
    else:
        cresult = "Low"

    protein = math.ceil(0.8 * basic_info['weight'])
    fat_min = math.ceil(0.882 * basic_info['weight'])
    fat_max = math.ceil(1.102 * basic_info['weight'])
    water = math.ceil((1.55 * basic_info['weight']) / 33.8)

    put_text('Analyzing your Virtual Health Check-Up Report. Please wait.....')
    put_processbar('bar1')
    for i in range(1, 11):
        set_processbar('bar1', i / 10)
        time.sleep(1)

    put_text('Name: ', basic_info['name'])
    put_text('Age: ', basic_info['age'])
    put_text('Height: ', basic_info['height'], 'meter')
    put_text('Weight: ', basic_info['weight'], 'kg')
    put_text('Gender: ', gender)
    put_text("Respiratory Rate: ", rate['resp'], "breath per minute")
    put_text("Heart Rate: ", heartrate, "heartbeats per minute")
    put_text("BMI: ", bmi)
    put_text(">> ", bmistatus)
    put_text("LBM: ", lbm, "kg")
    put_text("BMR: ", bmr, "calories/day")
    put_text(
        ">> Based on your Basal Metabolic Rate, you need {} calories intake to maintain the current weight.".format(
            calories))
    put_text("Diabetes Score: ", dscore)
    put_text(">> You have {}% chances of developing Type-II Daibetes.".format(dscore))
    put_text(">> You need {}gm protein on daily basis.".format(protein))
    put_text(">> You need to consume {}gm to {}gm of fats on daily basis.".format(fat_min, fat_max))
    put_text(">> You need to drink {} liters of water daily to stay fit.".format(water))
    put_text("Corona Virus Score: ", cresult)
    if cresult == "High":
        put_text(
            ">> Well, it doesn't mean you have COVID-19 but it is highly recommended that you get your COVID-19 Checkup. Stay Home and get yourself quarantined for 14 days and monitor your symptoms regularly.")
    elif cresult == "Moderate":
        put_text(
            ">> You are somewhat exposed to COVID-19. It's better if you get yourself checked for COVID-19. Stay home and get yourself quarantined and wash hands regularly. Don't forget to monitor your symptoms on daily basis.")
    elif cresult == "Low":
        put_text(
            ">> Your infection risk is low. But it is recommended to stay home and avoid public contact. Wash Hands and Monitor your symptoms on regular basis.")
    put_text("Fitness Score: ", points)
    if points < 2:
        put_text(
            ">> Great, Your score is good. You are fit and live a healthy life. Make sure to continue your exercise and take the suggested protein and fats intake.")
    elif points < 6:
        put_text(
            ">> You're somewhat fit, but if you continue to live like this, you will develop some of the serious symptoms in your old age.")
    elif points < 10:
        put_text(
            ">> You're unhealthy and if live like this you will develop serious symptoms soon. Take the suggested proteins and fats and do some regular exercise to get fit.")
    else:
        put_text(
            ">> You're already unfit and you need to start exercising from now! Living the same life will lead you very serious issues in the future and your life expectancy will be reduced too. You need to wake up and start to work-out from now!")

#Calling the above function as main function
def main():
    return virtualcheckup()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()

    start_server(main, port=args.port)

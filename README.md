# Virtual-Health-Check-Up
Description: This projects aims to provide the basic details such as BMI, BMR, Diabetes Prediction, Average Protein and Fats Intake, Fitness Score using common details such as Body Temperature, Age, Height, Weight, etc. This project is for informational purpose and it doesn't gurantte the medical opinion. All the result shown is based on Proved Mathematics and Researched Medicals Statistics. All the formulas for calculating different scores is given below.

# Project Demo
Project is Live [See Demo](https://virtual-health-checkup.herokuapp.com/)

### Body Mass Index
Body mass index (BMI) is a measure of body fat based on height and weight that applies to adult men and women.
BMI is a measurement of a person's leanness or corpulence based on their height and weight, and is intended to quantify tissue mass.
It is widely used as a general indicator of whether a person has a healthy body weight for their height.
Specifically, the value obtained from the calculation of BMI is used to categorize whether a person is underweight, normal weight, overweight, or obese depending on what range the value falls between.
These ranges of BMI vary based on factors such as region and age, and are sometimes further divided into subcategories such as severely underweight or very severely obese.
Being overweight or underweight can have significant health effects, so while BMI is an imperfect measure of healthy body weight, it is a useful indicator of whether any additional testing or action is required.
BMI is calculated as Weight/(Height)^2. Here we increase the fitness score if BMI is less than 18.5 or greater than 25 indicating that person is either Underweight or Overweight.

### Lean Body Mass
The Lean Body Mass Calculator computes a person's estimated lean body mass (LBM) based on body weight, height, gender, and age. There are various formulas to calculate LBM and in our project we will be using Hume's Formula.
There are different formula for different gender. For males, LBM is calculated as  0.32810W + 0.33929H - 29.5336 whereas For females, LBM is calculated as 0.29569W + 0.41813H - 43.2933

### Basal Metabolic Rate
The Basal Metabolic Rate (BMR) Calculator estimates your basal metabolic rate—the amount of energy expended while at rest in a neutrally temperate environment, and in a post-absorptive state (meaning that the digestive system is inactive, which requires about 12 hours of fasting).
The BMR for males is calculated as 5+(10*weight)+(625*height)-(5*age) whereas for females the formula is (10*weight)+(625*height)-(5*age)-161. 
BMR also defines how much calories you need per day to stay fit or keep your weight same. Well there are various factors that can affect BMR such as region, environment, deit, time-range, etc that can sometime given approximate result.

### Risk Factors
All the questions that are designed are research based and they will predict the risk factor of the scores given to each question.
Common questions which can related to different symptoms with different situations are eliminated. All the questions asked are quality based and it defins the core symptoms of a human body.
The risk factor is a great way to identify the body's sign before getting into serious trouble. It helps you to maintain physic and food balance in life.
Various factors like Happiness, depression, Anxiety and other social-economical factors can be taken into consideration to predict the risk factor more accurately. But since one cannot measure such factors, It is not included in this project. But you can implement on your own.
A person can extend the project by adding crucial information such as red blood cell and white blood cells and can identify the SIRS and many such information in the medical feilds.

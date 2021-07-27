# Add your code here

# Create the analyze_smoker() function
def analyze_smoker(smoker_status):
  if smoker_status == 1:
    print("To lower your cost, you should consider quitting smoking.")
  else:
    print("Smoking is not an issue for you.")
 
 # Create the analyze_bmi() function
def analyze_bmi(bmi_value):
  if bmi_value > 30:
    print("Your BMI is in the obese range. To lower your cost, you should significantly lower your BMI." + "\n" + "To lower your BMI, start by lowering your calories by 500 each day.Eat more fruits and vegetables, drink more water and start going to the gym.")
  elif bmi_value >= 25 and bmi_value <= 30:
    print("Your BMI is in the overweight range. To lower your cost, you should lower your BMI." + "\n" + "To lower your BMI, start by lowering your calories by 500 each day.Eat more fruits and vegetables, drink more water and start going to the gym.")
  elif bmi_value >= 18.5 and bmi_value < 25:
    print("Your BMI is in a healthy range.")
  else:
    print("Your BMI is in the underweight range. Increasing your BMI will not help lower your cost, but it will help improve your health.")

# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  analyze_smoker(smoker)
  analyze_bmi(bmi)
  return estimated_cost
 
# Estimate Keanu's insurance cost
try:
  keanu_insurance_cost = estimate_insurance_cost(name = 'Keanu', age = 29, sex = 1, bmi = 26.2, num_of_children = 3, smoker = 1)
except Exception as e:
  print("Please enter a valid data ||", e)

# Estimate my own insurance cost
print("\n")
try:
  emmanuel_insurance_cost = estimate_insurance_cost(name = "Emmanuel", age = 26, sex = 1, bmi = 24.9, num_of_children = 0, smoker = 0)
except Exception as e:
  print("Please enter a valid data ||", e)

# Estimate Ruth's insurance cost (wrong name type)
print("\n")
try:
  ruth_insurance_cost = estimate_insurance_cost(name = Ruth, age = 23, sex = 0, bmi = 19.5, num_of_children = 0, smoker = 0)
except Exception as e:
  print("Please enter a valid data ||", e)


# Create calculate_bmi() function to calculate the BMI of a new person
# weight in pounds and height in inches
def calculate_bmi(weight, height, name):
    my_bmi = weight / (height**2) * 703
    my_bmi_value = round(my_bmi, 2)
    if my_bmi > 30:
        print(name + "'s" + " Body Mass Index is " + str(my_bmi_value) + " >> This is considered Obese." + "\n" + "Please take a good action towards a better health condition by lowering your BMI.")
    elif my_bmi >= 25 and my_bmi <= 30:
        print(name + "'s" + " Body Mass Index is " + str(my_bmi_value) + " >> This is considered Overweight." + "\n" + "Please take a good action towards a better health condition by lowering your BMI.")
    elif my_bmi >= 18.5 and my_bmi < 25:
        print(name + "'s" + " Body Mass Index is " + str(my_bmi_value) + " >> This is considered Normal and Healthy.")
    else:
        print(name + "'s" + " Body Mass Index is " + str(my_bmi_value) + " >> This is considered Underweight." + "\n" + "Please take a good action towards a better health condition by increasing your BMI to a noraml value.")
    return my_bmi_value 

print("\n")
# Calculate Yaa's BMI value
try:
    yaa_bmi = calculate_bmi(weight = 168, height = 69, name ="Yaa")
except Exception as e:
  print("Please enter a valid data ||", e)

print("\n")
# Calculate Lucy's BMI value
try:
    yaa_bmi = calculate_bmi(weight = 170, height = 68, name ="Lucy")
except Exception as e:
  print("Please enter a valid data ||", e)

print("\n")
# Calculate Ama's BMI value (with wrong data type)
try:
    yaa_bmi = calculate_bmi(weight = 128, height = 0, name ="Ama")
except Exception as e:
  print("Please enter a valid data ||", e)
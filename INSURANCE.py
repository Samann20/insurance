health= str(input("enter your health (good, bad, excellent): "))
age= int(input("enter your age: "))
residence= str(input("enter yur residence(city, not in city): "))
gender= str(input("enter gender(male, female): "))

insurance_status= "not insured"
premium_rate= 0
max_amount= 0

if health == "excellent" and 25 <= age <= 34 and residence == "city":
  if gender == "male":
    insurance_status= "insured"
    premium_rate= 4
    max_amount= 200000
  elif gender == "female":
    insurance_status= "insured"
    premium_rate= 3
    max_amount= 100000
  elif health == "poor" and 25 <= age <= 35 and residence == "village" and gender == "male":
    insurance_status= "insured"
    premuim_rate= 6
    max_amount= 10000

print(f"insurance status: {insurance_status} \n premuim rate: {premium_rate} \n per thousand\n max amount: Rs. {max_amount}")


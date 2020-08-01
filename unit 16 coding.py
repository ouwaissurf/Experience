def main () :

    output = input('What would you like to use? (1)BMR , (2)BMI , (3)Daily Kilocalorie or (4)Help: ')
      
                


    # BMR
    if output == '1':
    
        bmr = 0
        while True:
            weight = int(input('Please enter your weight in kg: '))
            if weight > 250:
                print("Please enter an appropriate weight from 30-250kg")
            if weight < 30 :
                print("Please enter an appropriate weight from 30-250kg")
            else:
                break
            
        while True:
            height = int(input('Please enter your height in cm: '))
            if height > 210:
                print("Please enter an appropriate height from 120-210cm")
            if height < 120 :
                print("Please enter an appropriate height from 120-210cm")
            else:
                break
            
        while True:
            age = int(input('Please enter your age in years: '))
            if age > 100:
                print("Please enter an appropriate age from 14-100")
            if age < 14 :
                print("Please enter an appropriate age from 14-100")
            else:
                break
        
        gender = str(input("What is your gender (m) or (f)?"))
        if gender == 'm':
            bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
        if gender == 'f':
            bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

        print ("Your BMR is: " + str(float(format(bmr, '.2f'))))
        

    # BMI
    if output == '2':
        
         while True:
            weight = int(input('Please enter your weight in kg: '))
            if weight > 250:
                print("Please enter an appropriate weight from 30-250kg")
            if weight < 30 :
                print("Please enter an appropriate weight from 30-250kg")
            else:
                break
            
         while True:
            height = float(input('Please enter your height in m: '))
            if height > 2.1:
                print("Please enter an appropriate height from 1.2-2.1m")
            if height < 1.2:
                print("Please enter an appropriate height from 1.2-2.1m")
            else:
                break
    
         bmi = weight / height **2

         if bmi < 18.5:
             print ('Underweight')
             print ('Your target BMI is 18.5')

         elif bmi <= 24.9:
             print ('Normal weight')
             print ('Your target BMI is 22')

         elif bmi <= 29.9:
             print('Overweight')
             print ('Your target BMI is 24.9 ')

         elif bmi <= 30:
             print ('Obese')
             print ('Your target BMI is 25 ')

         print ("Your BMI is: " + str(float(format( bmi, '.1f'))))

    #Daily Kilocalorie 
    if output == '3':
        
        bmr = 0
        while True:
            weight = int(input('Please enter your weight in kg: '))
            if weight > 250:
                print("Please enter an appropriate weight from 30-250kg")
            if weight < 30 :
                print("Please enter an appropriate weight from 30-250kg")
            else:
                break
            
        while True:
            height = int(input('Please enter your height in cm: '))
            if height > 210:
                print("Please enter an appropriate height from 120-210cm")
            if height < 120 :
                print("Please enter an appropriate height from 120-210cm")
            else:
                break
            
        while True:
            age = int(input('Please enter your age in years: '))
            if age > 100:
                print("Please enter an appropriate age from 14-100")
            if age < 14 :
                print("Please enter an appropriate age from 14-100")
            else:
                break
        
        gender = str(input("What is your gender (m) or (f)?"))
        if gender == 'm':
            bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
        if gender == 'f':
            bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
            
        
        excercise = int(input('How many times do you excercise per week?'))
        if excercise == 0:
            print ("Your daily calorie intake needs to be: " + str(int(round(bmr*1.2))))
        elif excercise > 1:
            print ("Your daily calorie intake needs to be: " + str(int(round(bmr*1.375))))
        elif excercise > 3:
            print ("Your daily calorie intake needs to be: " + str(int(round(bmr*1.55))))
        elif excercise > 6:
            print ("Your daily calorie intake needs to be: " + str(int(round(bmr*1.725))))
        elif excercise >14:
            print ("Your daily calorie intake needs to be: " + str(int(round(bmr*1.9))))

    #help
    if output == '4':

        help = str(input('What do you need assistance on (1)what does the programme do? or (2)How to use it?'))
        if help == '1':
            print("This programme was created for gym members, so that they can maintain their current weight accurately")
            print("BMR stands for basal metabolic rate, this works out how much energy the user would burn if they rested for the whole day")
            print("BMI stands for body mass index, this works out the weight of the user in correlation to their height, it can also provide the ideal weight for the users height")
            print ("The Daily kilocalorie will work out how many calories the user needs to eat to maintain their weight")
        if help == '2':
            print ("To use this programme the user must select the what they want to use first")
            print ("Entering 1 will prompt the user to BMR")
            print ("Entering 2 will prompt the user to BMI")
            print ("Entering 3 will prompt the user to Daily Kilocalorie")
            print ("Entering 4 will prompt the user back to help")
            
        
            

        
    restart = input('do you wish to start again (yes) or (no)?: ')
    if restart == 'yes':
        main()     

    if restart == 'no':
        exit()
main()



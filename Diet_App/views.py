from django.shortcuts import render,redirect
from .models import*
from django.contrib import messages
from django.contrib.sessions.models import Session
from django.db import connection
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

# Create your views here.
def Home(request):
	return render(request,"Home.html",{})

def Admin_Login(request):
	if request.method == "POST":
		A_username = request.POST['aname']
		A_password = request.POST['apass']
		if AdminDetails.objects.filter(username = A_username,password = A_password).exists():
			ad = AdminDetails.objects.get(username=A_username, password=A_password)
			print('d')
			messages.info(request,'Admin login is Sucessfull')
			request.session['type_id'] = 'Admin'
			request.session['UserType'] = 'Admin'
			request.session['login'] = "Yes"
			return redirect("/")
		else:
			print('y')
			messages.error(request, 'Error wrong username/password')
			return render(request, "Admin_Login.html", {})
	else:
		return render(request, "Admin_Login.html", {})


def User_Login(request):
	if request.method == "POST":
		C_name = request.POST['aname']
		C_password = request.POST['apass']
		if userDetails.objects.filter(Username=C_name,Password=C_password).exists():
			users = userDetails.objects.all().filter(Username=C_name,Password=C_password)
			messages.info(request,C_name +' logged in')
			request.session['UserId'] = users[0].id
			request.session['type_id'] = 'User'
			request.session['UserType'] = C_name
			request.session['login'] = "Yes"
			return redirect('/')
		else:
			messages.info(request, 'Please Register')
			return redirect("/User_Registration")
	else:
		return render(request,'User_Login.html',{})

def User_Registration(request):
	if request.method == "POST":
		Name= request.POST['name']
		Age= request.POST['age']
		Phone= request.POST['phone']
		Email= request.POST['email']
		Address= request.POST['address']
		Username= request.POST['Username']
		Password= request.POST['Password']
		if userDetails.objects.all().filter(Username=Username).exists():
			messages.info(request,"Username Taken")
			return redirect('/User_Registeration')
		else:
			obj = userDetails(
			Name=Name
			,Age=Age
			,Phone=Phone
			,Email=Email
			,Address=Address
			,Username=Username
			,Password=Password)
			obj.save()
			messages.info(request,Name+" Registered")
			return redirect('/User_Login')
	else:
		return render(request,"User_Registration.html",{})

def View_User(request):
	details = userDetails.objects.all()
	return render(request,"View_User.html",{'details':details})

def Profile(request):
	if request.method == "POST":
		userid = request.POST['userid']
		Name= request.POST['name']
		Age= request.POST['age']
		Phone= request.POST['phone']
		Email= request.POST['email']
		Address= request.POST['address']
		userDetails.objects.filter(id=userid).update(
			Name=Name
			,Age=Age
			,Phone=Phone
			,Email=Email
			,Address=Address)
		messages.info(request,"Profile Updated")
		return redirect('/Profile')
	else:
		userid = request.session['UserId']
		details = userDetails.objects.filter(id=userid)
		return render(request,"Profile.html",{'details':details})


def Ask_Help(request):
	if request.method == "POST":
		user_id = request.session['UserId']
		query = request.POST['feedback']
		obj = Queries(User_id=user_id,Query=query)
		obj.save()
		return redirect('/Ask_Help')
	else:
		return render(request,"Ask_Help.html",{})


def View_Query(request):
	details = Queries.objects.all()
	return render(request,"View_Query.html",{'details':details})

def Answer(request):
	if request.method=="POST":
		query_id = request.POST['query_id']
		answer = request.POST['answer']
		Queries.objects.filter(id=query_id).update(Answer=answer)
		messages.info(request,"Query Answered")
	return redirect('/View_Query')

def Add_Information(request):
	if request.method == "POST":
		Specialization = request.POST['Specialization']
		Qualifications = request.POST['qualification']
		Name = request.POST['name']
		Email = request.POST['email']
		Age = request.POST['age']
		Number = request.POST['number']
		Gender = request.POST['Gender']
		Years = request.POST['years']
		selected_languages = request.POST.getlist('languages')
		Consultation_Hours = request.POST['hours']
		Consultation_Fees = request.POST['fees']
		Venue = request.POST['venue']
		Image  = request.FILES['image']
		obj = Information(Specialization=Specialization,Qualifications=Qualifications,Name=Name,Email=Email
			,Age=Age
			,Number=Number
			,Gender=Gender
			,Years=Years
			,Languages_Spoken=selected_languages
			,Consultation_Hours=Consultation_Hours
			,Consultation_Fees=Consultation_Fees
			,Venue=Venue,Image=Image)
		obj.save()
		messages.info(request,"Information Added")
		return redirect('/Add_Information')
	else:
		return render(request,"Add_Information.html",{})



# Load the dataset from the CSV file
df = pd.read_csv("C:/workspace/AI_Dietician/all_meals.csv")

# Define a mapping between user input and column names in the dataset
meal_type_mapping = {'Breakfast': 'Breakfast', 'Lunch': 'Lunch', 'Snack': 'Snack', 'Dinner': 'Dinner'}

def calculate_nutrient_calories(meal_type, calories, carb_ratio, protein_ratio, fat_ratio, vitamin_ratio):
    carb_calories = round(calories * carb_ratio)
    protein_calories = round(calories * protein_ratio)
    fat_calories = round(calories * fat_ratio)
    vitamin_calories = round(calories * vitamin_ratio)

    # Calculate hydration calories as 20% of the calories allocated for the meal type
    hydration_calories = round(calories * 0.2)

    return {
        'meal_type': meal_type,
        'calories': calories,
        'carbohydrates': carb_calories,
        'protein': protein_calories,
        'fats': fat_calories,
        'vitamins': vitamin_calories,
        'hydration': hydration_calories,
    }

def calculate_meal_calories(total_calories):
    # Example division: 25% for breakfast, 35% for lunch, 15% for snacks, and 25% for dinner
    breakfast_calories = round(0.25 * total_calories)
    lunch_calories = round(0.35 * total_calories)
    snacks_calories = round(0.15 * total_calories)
    dinner_calories = round(0.25 * total_calories)

    return {
        'Breakfast': breakfast_calories,
        'Lunch': lunch_calories,
        'Snack': snacks_calories,
        'Dinner': dinner_calories
    }

def calculate_bmr(age, gender, height, weight):
    # Harris-Benedict equation for BMR
    if gender == 'male':
        bmr = round(88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age))
    elif gender == 'female':
        bmr = round(447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age))
    else:
        raise ValueError("Invalid gender. Use 'male' or 'female'.")

    return bmr

def calculate_calories(bmr, activity):
    activity_multipliers = {
        'sedentary': 1.2,
        'light': 1.375,
        'moderate': 1.55,
        'active': 1.725,
        'very active': 1.9,
        'extra active': 2.1
    }

    if activity not in activity_multipliers:
        raise ValueError("Invalid activity level.")

    total_calories = round(bmr * activity_multipliers[activity])
    return total_calories

def get_recommended_foods(meal_type, nutrient_calories):
    # Get the nutrient values from the nutrient_calories dictionary
    calories = nutrient_calories['calories']
    carb_ratio = 0.5
    protein_ratio = 0.3
    fat_ratio = 0.15
    vitamin_ratio = 0.05

    # Calculate nutrient calories for the meal type
    nutrient_calories = calculate_nutrient_calories(meal_type, calories, carb_ratio, protein_ratio, fat_ratio, vitamin_ratio)

    # Filter the dataset based on the user's meal type
    user_dataset = df[df['Meal Type'] == meal_type]

    # Reset the index of the user_dataset
    user_dataset.reset_index(drop=True, inplace=True)

    # Select relevant columns for clustering and nutrient comparison
    X = user_dataset[['Calories', 'Carbohydrates (g)', 'Proteins (g)', 'Fats (g)', 'Vitamins (%)', 'Hydration (%)']].values

    # Normalize the data (optional but recommended for K-means)
    X = (X - X.mean(axis=0)) / X.std(axis=0)

    # Number of clusters (you can adjust this based on your dataset and needs)
    n_clusters = 1

    # Apply K-means clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(X)

    # Find the cluster closest to the user's desired nutrient values and calories
    user_nutrients_normalized = np.array([calories, nutrient_calories['carbohydrates'], nutrient_calories['protein'], nutrient_calories['fats'], nutrient_calories['vitamins'], nutrient_calories['hydration']])
    user_nutrients_normalized = (user_nutrients_normalized - X.mean(axis=0)) / X.std(axis=0)
    user_cluster = kmeans.predict([user_nutrients_normalized])

    # Get the cluster centroid for the user cluster
    user_cluster_centroid = kmeans.cluster_centers_[user_cluster]

    # Calculate Euclidean distance to compare nutrient values
    distances = np.linalg.norm(X - user_cluster_centroid, axis=1)

    # Sort food items based on similarity to the user's desired nutrient values and calories
    food_indices = np.argsort(distances)[:7]
    recommended_foods = user_dataset.iloc[food_indices]

    # Breakfast= []

    # if meal_type == "Breakfast":
    # 	example = recommended_foods[['Food Name','Meal Type']].values.tolist()
    # 	Breakfast.append(example)
    # print("Breakfast",Breakfast)


    

    print(recommended_foods[['Food Name','Meal Type']])
    return recommended_foods[['Food Name','Meal Type']]

def Calculator(request):
    if request.method == 'POST':
        age = int(request.POST.get('age'))
        gender = request.POST.get('gender')
        height = int(request.POST.get('height'))
        weight = float(request.POST.get('weight'))
        activity = request.POST.get('activity')

        # Perform calculations (use the calculate_bmr and calculate_calories functions from the previous code)
        bmr = calculate_bmr(age, gender, height, weight)
        total_calories = calculate_calories(bmr, activity)

        # Divide total calories into meals
        meal_calories = calculate_meal_calories(total_calories)

        # Calculate nutrient calories for each meal type
        nutrient_calories_list = []
        for meal_type, calories in meal_calories.items():
            nutrient_calories = calculate_nutrient_calories(meal_type, calories, 0.5, 0.3, 0.15, 0.05)
            nutrient_calories_list.append(nutrient_calories)
        print("Nutrient_calories",nutrient_calories)

        # # Get recommended foods for each meal type
        # recommended_foods_list = []
        # for meal_type, nutrient_calories in zip(meal_calories.keys(), nutrient_calories_list):
        #     recommended_foods = get_recommended_foods(meal_type, nutrient_calories)
        #     recommended_foods_list.append(recommended_foods)
         # Initialize dictionaries for each meal type
        Breakfast = []
        Lunch = []
        Dinner = []
        Snack = []

        # Iterate through the recommended foods and append them to the corresponding meal type list
        for meal_type, nutrient_calories in zip(meal_calories.keys(), nutrient_calories_list):
            recommended_foods = get_recommended_foods(meal_type, nutrient_calories)

            # Convert DataFrame to a list of dictionaries
            food_list = recommended_foods[['Food Name', 'Meal Type']].to_dict(orient='records')

            if meal_type == "Breakfast":
                Breakfast.extend(food_list)
            elif meal_type == "Lunch":
                Lunch.extend(food_list)
            elif meal_type == "Dinner":
                Dinner.extend(food_list)
            elif meal_type == "Snack":
                Snack.extend(food_list)

        print("Breakfast_List",Breakfast)
        print("___________________________")

        print("Dinner_List",Dinner)

        # Combine all the meal type dictionaries into a single list
        recommended_foods_list = Breakfast + Lunch + Snack + Dinner

        # print("recommended_foods_list",recommended_foods_list)

        # B = {**recommended_foods_list[0],**recommended_foods_list[7],**recommended_foods_list[14],**recommended_foods_list[21]}
        # print("Breakfast_List",B)

        userid = request.session['UserId']
        # Try to retrieve the existing Breakfast_List object for the given userid
        breakfast_obj, created = Breakfast_List.objects.get_or_create(userid=userid)
        # Save the values of the first key-value pair of each dictionary into the database
        for i in range(7):  # Iterate 7 times (for Food1 to Food7)
        	if i < len(Breakfast):
        		breakfast_item = Breakfast[i]
        		food_name = breakfast_item.get('Food Name', '')
        		setattr(breakfast_obj, f'Food{i+1}', food_name)
        # Save the modified Breakfast_List object with the updated fields into the database
        breakfast_obj.save()

        #Lunch 

        lunch_obj, created = Lunch_List.objects.get_or_create(userid=userid)
        # Save the values of the first key-value pair of each dictionary into the database
        for i in range(7):  # Iterate 7 times (for Food1 to Food7)
        	if i < len(Lunch):
        		lunch_item = Lunch[i]
        		food_name = lunch_item.get('Food Name', '')
        		setattr(lunch_obj, f'Food{i+1}', food_name)
        # Save the modified Breakfast_List object with the updated fields into the database
        lunch_obj.save()

        #Snack

        snack_obj, created = Snack_List.objects.get_or_create(userid=userid)
        # Save the values of the first key-value pair of each dictionary into the database
        for i in range(7):  # Iterate 7 times (for Food1 to Food7)
        	if i < len(Snack):
        		snack_item = Snack[i]
        		food_name = snack_item.get('Food Name', '')
        		setattr(snack_obj, f'Food{i+1}', food_name)
        # Save the modified Breakfast_List object with the updated fields into the database
        snack_obj.save()

        #Dinner
        dinner_obj, created = Dinner_List.objects.get_or_create(userid=userid)
        # Save the values of the first key-value pair of each dictionary into the database
        for i in range(7):  # Iterate 7 times (for Food1 to Food7)
        	if i < len(Dinner):
        		dinner_item = Dinner[i]
        		food_name = dinner_item.get('Food Name', '')
        		setattr(dinner_obj, f'Food{i+1}', food_name)
        # Save the modified Breakfast_List object with the updated fields into the database
        dinner_obj.save()





        





        details = Breakfast_List.objects.filter(userid=userid)
        data = Lunch_List.objects.filter(userid=userid)
        snackdata = Snack_List.objects.filter(userid=userid)
        dinnerdata = Dinner_List.objects.filter(userid=userid)

        context = {
            'bmr': bmr,
            'total_calories': total_calories,
            'meal_calories': meal_calories,
            'nutrient_calories_list': nutrient_calories_list,
            'Breakfast':Breakfast,
            'details':details,'data':data,'snackdata':snackdata,'dinnerdata':dinnerdata
        }
        return render(request, 'Dashboard.html', context)
    else:
        return render(request, 'Calculator.html')

import datetime

def determine_day_of_week(counter):
    # Get the current date
    today = datetime.date.today()
    # Calculate the offset based on the counter
    offset = counter % 7
    # Calculate the date for the specific day of the week
    target_date = today + datetime.timedelta(days=offset)
    # Get the day of the week as a string (e.g., 'Monday', 'Tuesday', etc.)
    day_of_week = target_date.strftime('%A')
    return day_of_week




def View_Information(request):
	details = Information.objects.all()
	return render(request,"View_Information.html",{'details':details})

def Dashboard(request):
	return render(request,"Dashboard.html",{})

def ViewUser_Query(request):
    userid = request.session['UserId']
    details = Queries.objects.filter(User_id=userid)
    return render(request,"ViewUser_Query.html",{'details':details})

def Logout(request):
	Session.objects.all().delete()
	return redirect("/")
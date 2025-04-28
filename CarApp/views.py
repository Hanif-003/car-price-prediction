from django.shortcuts import render

from joblib import load
model=load("./savedModels/model.joblib")

import locale
# Set Indian style commas
locale.setlocale(locale.LC_ALL, 'en_IN')

def predictor(request):
    if request.method=="POST":
         brand=request.POST["brand"]
         year=request.POST["year"]
         km_driven=request.POST["km_driven"]
         fuel=request.POST["fuel"]
         seller_type=request.POST["seller_type"]
         transmission=request.POST["transmission"]
         owner=request.POST["owner"]
         mileage=request.POST["mileage"]
         engine=request.POST["engine"]
         max_power=request.POST["max_power"]
         seats=request.POST["seats"]


         y_pred=model.predict([[brand, year, km_driven,fuel , seller_type,transmission,owner ,mileage , engine , max_power, seats]])
        

        # Get first prediction and format with commas
         y_pred_value = int(y_pred[0])  # Convert to int if not already
         y_pred_formatted = locale.format_string("%d", y_pred_value, grouping=True)
         
         return render(request,"result.html",{"result":y_pred_formatted})

    return render(request,"main.html")     

    
    



   


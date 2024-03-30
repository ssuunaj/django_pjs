from django.shortcuts import render,redirect
from .models import Food,Consume


def index(request):

    if request.method == "POST":
        food_consumed = request.POST.get("food_consumed")
        food_macro = Food.objects.get(name=food_consumed)
        #user that is currently logged in 
        user = request.user
        consume = Consume(user=user,food_consumed=food_macro)
        consume.save()
        foods= Food.objects.all()
    else:
        foods= Food.objects.all()

    user_consumed_food = Consume.objects.filter(user=request.user)
    
    return render(request,'myapp/index.html',{'foods':foods,'user_consumed_food':user_consumed_food})


def delete_consume(request,id):
    consumed_food = Consume.objects.get(id=id)

    if request.method == "POST":
        consumed_food.delete()
        return redirect('/')
    return render(request,'myapp/delete.html')



    



from . import views
from django.urls import path
from . import class_views


#name spacing urls to avoid conflicts 

app_name = 'food'


urlpatterns = [
    #food
    path('',class_views.IndexClassView.as_view(), name="index"),
       #food/1
    # path('<int:item_id>/',views.detail,name="detail"),
    #for class based view, can directly pass in the pk in the route
    path('<int:pk>/',class_views.DetailClassView.as_view(),name="detail"),
    path('item',views.item, name="item"),
    #add items
    path('add',class_views.CreateItemView.as_view(), name="create_item"),
    #edit items
    path('update/<int:id>/', views.update_item, name="update_item"),
    #delete_item
    path('delete/<int:id>/', views.delete_item,name='delete_item'),
 
]
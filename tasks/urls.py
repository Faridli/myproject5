from django.urls import path
from tasks.views import ( 
    Dashboard,
    Br,  
    Address,
     # -----------------------------
     # Bn HQ
     # -----------------------------
    Force_bio,
    Force_detail,

   
)
# app_name = "tasks"  
urlpatterns = [
    # -----------------------------
    # Manager & User Dashboards
    # -----------------------------
    path('manager-dashboard/', Dashboard, name='manager-dashboard'),
    path('br/', Br, name='br'),
    path('address/<int:member_id>', Address, name='address'),
    # path('user-dashboard/', user_dashboard, name='user-dashboard'),

    # -----------------------------
    # Force Bio  and Bn-HQ
    # -----------------------------
    path('bio/', Force_bio, name='force-bio'),

    path('force/',Force_detail, name='force-detail'),

    # path('br/',  List_of_All_Branch, name='allbr'),
 
    # -----------------------------
    # Company Views
    # -----------------------------
    

    # Optional old path


    # -----------------------------
    # Member Posting View
    # -----------------------------
    # path('member-posting/', member_posting_view, name='member-posting'), 

    # ..................................
    # ALL Company history..............
   


]




















# python manage.py shell 
# from django.template.loader import get_template
# get_template('bnhq/list.html')
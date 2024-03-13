from django.urls import path
from main.views import show_main, create_anime, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user
from main.views import edit_anime
from main.views import delete_anime
from main.views import add_anime_ajax
app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-anime', create_anime, name='create_anime'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('edit-anime/<int:id>', edit_anime, name='edit_anime'),
    path('add-anime-ajax/', add_anime_ajax, name='add_anime_ajax'),
    path('delete/<int:id>', delete_anime, name='delete_anime')
]
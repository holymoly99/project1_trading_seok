from django.urls import path
from .views import base_views, sell_views, comment_views, vote_views


app_name = 'joonggo'

urlpatterns = [
    path('', base_views.index, name='index'),
    path('<int:sell_id>/', base_views.detail, name='detail'),

    path('comment/create/sell/<int:sell_id>/', comment_views.comment_create_sell, name='comment_create_sell'),
    path('comment/modify/sell/<int:comment_id>/', comment_views.comment_modify_sell, name='comment_modify_sell'),
    path('comment/delete/sell/<int:comment_id>/', comment_views.comment_delete_sell, name='comment_delete_sell'),
    

    path('question/create/', sell_views.sell_create, name='sell_create'),
    path('question/modify/<int:sell_id>/', sell_views.sell_modify, name='sell_modify'),
    path('question/delete/<int:sell_id>/', sell_views.sell_delete, name="sell_delete"),

    path('vote/question/<int:sell_id>/', vote_views.vote_sell, name='vote_sell'),

]

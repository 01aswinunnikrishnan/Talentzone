from django.urls import path
from talent_app.user_views import user_index_view ,view_pdt,pdt_buy,feed_back,add_ratings,artist_search







urlpatterns = [
     path('',user_index_view.as_view()),
     path('view_pdt',view_pdt.as_view()),
     path('pdt_buy',pdt_buy.as_view()),
     path('feedback',feed_back.as_view()),
     path('add_ratings',add_ratings.as_view()),
     path('artist_search',artist_search.as_view()),
]

def urls():
    return urlpatterns, 'user', 'user'
from django.urls import path
from talent_app.artist_views import artist_index_view ,booking, delete_pdtdata, edit_pdtdata,pay_event,product_add,view_products,feedback_view,view_event,view_ratings,event_search







urlpatterns = [
    path('',artist_index_view.as_view()),
    path('product_add',product_add.as_view()),
    path('view_products',view_products.as_view()),
    path('view_feedback', feedback_view.as_view()),
    path('view_ratings',view_ratings.as_view()),
    path('event_search',event_search.as_view()),
    path('view_event', view_event.as_view()),
    path('pay_event', pay_event.as_view()),
    path('booking', booking.as_view()),
    path('edit', edit_pdtdata.as_view()),
    path('delete', delete_pdtdata.as_view()),

]
def urls():
    return urlpatterns, 'artist', 'artist'
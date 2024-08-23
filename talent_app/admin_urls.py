from django.urls import path
from talent_app.admin_views import admin_index_view ,user_ApproveView,user_RejectView,user_reg_view,artist_view,artist_ApproveView,artist_RejectView,organisation_view,organisation_ApproveView,organisation_RejectView,view_events,view_products







urlpatterns = [
    path('',admin_index_view.as_view()),
     path('user_reg_view',user_reg_view.as_view()),
    path('user_ApproveView',user_ApproveView.as_view()),
    path('user_RejectView',user_RejectView.as_view()),
    path('artist_view',artist_view.as_view()),
    path('artist_ApproveView',artist_ApproveView.as_view()),
    path('artist_RejectView',artist_RejectView.as_view()),
    path('organisation_view',organisation_view.as_view()),
    path('organisation_ApproveView',organisation_ApproveView.as_view()),
    path('organisation_RejectView',organisation_RejectView.as_view()),
    path('view_events',view_events.as_view()),
    path('view_products',view_products.as_view()),
    
]
def urls():
    return urlpatterns, 'admin', 'admin'
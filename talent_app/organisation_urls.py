from django.urls import path
from talent_app.organisation_views import delete_eventdata, edit_eventdatas, organisation_index_view ,event_add,view_event,booking







urlpatterns = [
    path('',organisation_index_view.as_view()),
    path('event_add',event_add.as_view()),
    path('view_event',view_event.as_view()),
    path('booking', booking.as_view()),
    path('edit', edit_eventdatas.as_view()),
    path('delete', delete_eventdata.as_view()),


]
def urls():
    return urlpatterns, 'organisation', 'organisation'
from urllib import request
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.views.generic.base import View


from talent_app.models import organisation_register,Add_Events,payment_event


class organisation_index_view(TemplateView):
    template_name = 'organisation/index.html'

class event_add(TemplateView):
    template_name = 'organisation/add_events.html'
    def post(self , request,*args,**kwargs):
         com=organisation_register.objects.get(user_id=self.request.user.id)
         name= request.POST['eventname']
         ven= request.POST['venue']
         add= request.POST['address']
         date= request.POST['date']
         tim= request.POST['time']
         event=  Add_Events()
         event.event_name = name
         event.venue = ven
         event.address= add
         event.date= date
         event.time= tim
         event.organisation_id=com.id
         event.save()

         messages = "successfully added"
        
         return render(request,'organisation/index.html',{'message':messages})    
    

class view_event(TemplateView):
      template_name = 'organisation/view_events.html'
      def get_context_data(self, **kwargs):
            
            
        context = super(view_event,self).get_context_data(**kwargs)
        org=organisation_register.objects.get(user_id=self.request.user.id)


        event_list = Add_Events.objects.filter(organisation_id=org.id)

        context['event_list'] = event_list
        return context
      

class booking(TemplateView):
    template_name = 'organisation/view_booking.html'
    def get_context_data(self, **kwargs):
        context = super(booking,self).get_context_data(**kwargs)
        com=organisation_register.objects.get(user_id=self.request.user.id)

        cart =payment_event .objects.filter(status='registered',organisation_id=com.id)

        context['cart'] = cart
        return context
    


class edit_eventdatas(TemplateView):
    template_name = 'organisation/eventdata_edit.html'
    # def post(self,request,*args,**kwargs):
    #     id = self.request.GET['id']
    #     edit = Add_Events.objects.get(pk=id)
     
    #     edit.event_name= request.POST['eventname']
    #     edit.venue= request.POST['venue']
    #     edit.address= request.POST['address']
    #     edit.date= request.POST['date']
    #     edit.time= request.POST['time']
    #     edit.save()
    #     return render(request,'organisation/index.html',{'message':"Details editted"})
    def get_context_data(self, **kwargs):
            context = super(edit_eventdatas,self).get_context_data(**kwargs)
            id = self.request.GET['id']

            list = Add_Events.objects.get(id=id)
            context['e'] = list
            return context
    def post(self,request,*args,**kwargs):
           id = self.request.GET['id']
           edit = Add_Events.objects.get(pk=id)
           edit.event_name = request.POST['eventname']
           edit.venue = request.POST['venue']
           edit.address = request.POST['address']
           edit.date = request.POST['date']
           edit.time = request.POST['time']
           edit.save()
           return render(request,'artist/index.html',{'message':"Details editted"})
class delete_eventdata(View):
    def dispatch(self,request,*args,**kwargs):
        id = request.GET['id']
        Add_Events.objects.get(id=id).delete()

        return render(request,'organisation/index.html',{'message':"Details Removed"})
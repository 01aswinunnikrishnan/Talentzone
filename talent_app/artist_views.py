from urllib import request
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.views.generic.base import View

from django.core.files.storage import FileSystemStorage
from talent_app.models import Add_Products,artist_register,feedback,Add_Events,rating,payment_event,Buy_Product


class artist_index_view(TemplateView):
    template_name = 'artist/index.html'

class product_add(TemplateView):
    template_name = 'artist/add_products.html'
    def post(self , request,*args,**kwargs):
         id=request.POST['id'] 
         com=artist_register.objects.get(user_id=self.request.user.id)
         name= request.POST['workname']
         price= request.POST['rate']
         descrip= request.POST['description']
         image = request.FILES['iimage']
         fii = FileSystemStorage()
         filesss = fii.save(image.name, image)
         pdt=  Add_Products()
         pdt.work_name = name
         pdt.rate = price
         pdt.description= descrip
         pdt.product_image=filesss
         pdt.artist_id=com.id
         pdt.save()

         messages = "successfully added"
        
         return render(request,'artist/index.html',{'message':messages})    
    
class view_products(TemplateView):
    template_name = 'artist/product_view.html'
    def get_context_data(self, **kwargs):
        context = super(view_products,self).get_context_data(**kwargs)

        a=artist_register.objects.get(user_id=self.request.user.id)
        pdt_list = Add_Products.objects.filter(artist_id=a.id)

        context['pdt_list'] = pdt_list
        return context
    
class feedback_view(TemplateView):
        template_name = 'artist/view_feedbacks.html'
        def get_context_data(self, **kwargs):
             context = super( feedback_view,self).get_context_data(**kwargs)
             a=artist_register.objects.get(user_id=self.request.user.id)
             fee = feedback.objects.filter(artist_id=a.id)

             context['fee'] = fee
             return context
        

class view_event(TemplateView):
      template_name = 'artist/view_events.html'
      def get_context_data(self, **kwargs):
        context = super(view_event,self).get_context_data(**kwargs)

        event_list = Add_Events.objects.all()

        context['event_list'] = event_list
        return context
        

    
class view_ratings(TemplateView):
    template_name = 'artist/view_ratings.html'
    def get_context_data(self, **kwargs):
        context = super(view_ratings,self).get_context_data(**kwargs)
        a=artist_register.objects.get(user_id=self.request.user.id)
        rate = rating.objects.filter(product__artist_id=a.id)

        context['rate'] = rate
        return context



class event_search(TemplateView):
    template_name = 'artist/search_event.html'
    def get_context_data(self, **kwargs):
        context = super( event_search,self).get_context_data(**kwargs)

        eventsrc = Add_Events.objects.all()

        context['eventsrc'] = eventsrc
        return context
    
    def post(self, request, *args, **kwargs):
        address=request.POST['address']
        host = Add_Events.objects.filter(address__icontains = address)
        return render(request, 'artist/search_event.html', {'eventsrc': host})
    

class pay_event(TemplateView):
    template_name = 'artist/pay.html'
    def get_context_data(self, **kwargs):
        context = super(pay_event,self).get_context_data(**kwargs)
        eid =self.request.GET['id']
        context['id'] = eid
        return context
    
    def post(self , request,*args,**kwargs):
        co=artist_register.objects.get(user_id=self.request.user.id)
        eid = request.POST['id']                        
        cardname= request.POST['cardname']
        cardnumber= request.POST['cardno']
        expirydate= request.POST['expiry']
        cvv= request.POST['cvv']
        oid=Add_Events.objects.get(id=eid)
        o=oid.organisation_id
        buy = payment_event()
        buy.artist_id=co.id
        # buy.idea = ideas_add.objects.get(pk=iid)
        buy.cardname =cardname 
        buy. cardno= cardnumber
        buy.expiry= expirydate
        buy.cvv= cvv
        buy.event_id= eid
        buy.organisation_id=o
        buy.status= "registered"
        buy.save()
        return render(request, 'artist/pay.html', {'message': "successfully registered"})
    
class booking(TemplateView):
    template_name = 'artist/view_booking.html'
    def get_context_data(self, **kwargs):
        com=artist_register.objects.get(user_id=self.request.user.id)


        context = super(booking,self).get_context_data(**kwargs)
        cart = Buy_Product.objects.filter(status='paid',artist_id=com.id)

        context['cart'] = cart
        return context
    
class edit_pdtdata(TemplateView):
    template_name = 'artist/edit_prdtdata.html'
    def get_context_data(self, **kwargs):
        context = super(edit_pdtdata,self).get_context_data(**kwargs)
        id = self.request.GET['id']

        list = Add_Products.objects.get(id=id)

        context['p'] = list
        return context
    def post(self,request,*args,**kwargs):
        id = self.request.GET['id']
        edit = Add_Products.objects.get(pk=id)
     
        edit.work_name = request.POST['workname']
        edit.rate = request.POST['rate']
        
        edit.description = request.POST['description']
        
        image = request.FILES['iimage']
        fii = FileSystemStorage()
        filesss = fii.save(image.name, image)  
        edit.product_image=filesss
     
        edit.save()
        return render(request,'artist/index.html',{'message':"Details editted"})
    
class delete_pdtdata(View):
    def dispatch(self,request,*args,**kwargs):
        id = request.GET['id']
        Add_Products.objects.get(id=id).delete()

        return render(request,'artist/index.html',{'message':"Details Removed"})
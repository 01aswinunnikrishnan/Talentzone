from urllib import request
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from django.contrib.auth import login
from talent_app.models import Add_Products,Buy_Product,user_register,feedback,rating,artist_register


class user_index_view(TemplateView):
     template_name = 'user/index.html'

class view_pdt(TemplateView):
  template_name = 'user/view_product.html'
  def get_context_data(self, **kwargs):
        context = super(view_pdt,self).get_context_data(**kwargs)
        id=self.request.GET['id']
        com=artist_register.objects.get(id=id)
        pdt_list = Add_Products.objects.filter(artist_id=com.id)

        context['pdt_list'] = pdt_list
        return context
  
class pdt_buy(TemplateView):
    template_name = 'user/buy_product.html'
    def get_context_data(self, **kwargs):
        context = super(pdt_buy,self).get_context_data(**kwargs)
        pid =self.request.GET['id']
        context['id'] = pid
        return context
    
    def post(self , request,*args,**kwargs):
        com=user_register.objects.get(user_id=self.request.user.id)
        pid = request.POST['id']
        cardname= request.POST['cardname']
        cardnumber= request.POST['cardno']
        expirydate= request.POST['expiry']
        cvv= request.POST['cvv']
        aid=Add_Products.objects.get(id=pid)
        a=aid.artist_id
        buy = Buy_Product()
        buy.user_id=com.id
        buy.cardname =cardname 
        buy. cardno= cardnumber
        buy.expiry= expirydate
        buy.cvv= cvv
        buy.artist_id=a
        buy.product_id= pid

        buy.status= "paid"
        buy.save()
        return render(request, 'user/buy_product.html', {'message': "successfully paid"})
    

  
class feed_back(TemplateView):
    template_name='user/feedback.html'
    # def get_context_data(self, **kwargs):
    #     context = super(feed_back,self).get_context_data(**kwargs)
    #     feed = artist_register.objects.all()
    #     context['feed'] = feed
    #     return context
    def post(self , request,*args,**kwargs):
        # com=artist_register.objects.get(user_id=self.request.user.id)
        user = User.objects.get(pk=self.request.user.id)
        # nam = request.POST['artist']
        aid =self.request.GET['id']

        feed= request.POST['feedback']
        
        fee =feedback()
        
        fee.user = user
        fee.artist_id=aid
        
        fee.feedback = feed
        fee.save()

        return render(request, 'user/index.html', {'message':"successfully Submit Your Feedback"})
    
class add_ratings(TemplateView):
    template_name = 'user/add_rating.html'

     
    # def get_context_data(self, **kwargs):
    #     context = super(add_ratings,self).get_context_data(**kwargs)
    #     rate = Add_Products.objects.all()
    #     context['rate'] = rate
    #     return context
    
    def post(self , request,*args,**kwargs):

        user=User.objects.get(pk=self.request.user.id)
    
        # nam = request.POST['Product']
        pid =self.request.GET['id']

        mail = request.POST['rating']
        ph= request.POST['feedback']
   
        appr =  rating()
        appr.rate = mail
        appr.comment = ph
        # appr.product_id = nam
        appr.user_id=user.id
        appr.product_id=pid

        appr.save()
        return render(request, 'user/index.html', {'message': "rating successfully added"})
    

    
class artist_search(TemplateView):
    template_name = 'user/search_artist.html'
    def get_context_data(self, **kwargs):
        context = super( artist_search,self).get_context_data(**kwargs)

        artistsrc = artist_register.objects.all()

        context['artistsrc'] = artistsrc
        return context
    
    def post(self, request, *args, **kwargs):
        first_name=request.POST['first_name']
        host = artist_register.objects.filter(user__first_name__icontains=first_name)
        return render(request, 'user/search_artist.html', {'artistsrc':host})
    

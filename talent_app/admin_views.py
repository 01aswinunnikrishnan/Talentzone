from urllib import request
from django.contrib.auth.models import User
from django.views.generic import TemplateView,View
from django.shortcuts import render,redirect
from django.contrib.auth import login


from talent_app.models import user_register,artist_register,organisation_register,Add_Products,Add_Events


class admin_index_view(TemplateView):
    template_name = 'admin/index.html'

class user_reg_view(TemplateView):
    template_name = 'admin/user_view.html'
    
    
    def get_context_data(self, **kwargs):
        context = super(user_reg_view, self).get_context_data(**kwargs)

        doc = user_register.objects.filter(user__last_name='0', user__is_staff='0', user__is_active='1')

        context['doc'] = doc
        return context
    
class user_ApproveView(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name = '1'
        user.save()
        return render(request, 'admin/user_view.html', {'message': " Account Approved"})


class user_RejectView(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name = '0'
        user.is_active = '0'
        user.save()
        return render(request, 'admin/index.html', {'message': "Account Removed"})
    
class artist_view(TemplateView):
    template_name = 'admin/artist_view.html'
    
    
    def get_context_data(self, **kwargs):
        context = super(artist_view, self).get_context_data(**kwargs)

        doc = artist_register.objects.filter(user__last_name='0', user__is_staff='0', user__is_active='1')

        context['doc'] = doc
        return context
    
class artist_ApproveView(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name = '1'
        user.save()
        return render(request, 'admin/index.html', {'message': " Account Approved"})


class artist_RejectView(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name = '0'
        user.is_active = '0'
        user.save()
        return render(request, 'admin/index.html', {'message': "Account Removed"})
    

class organisation_view(TemplateView):
    template_name = 'admin/organisation_view.html'
    
    
    def get_context_data(self, **kwargs):
        context = super(organisation_view, self).get_context_data(**kwargs)

        doc = organisation_register.objects.filter(user__last_name='0', user__is_staff='0', user__is_active='1')

        context['doc'] = doc
        return context
    
class organisation_ApproveView(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name = '1'
        user.save()
        return render(request, 'admin/index.html', {'message': " Account Approved"})


class organisation_RejectView(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name = '0'
        user.is_active = '0'
        user.save()
        return render(request, 'admin/index.html', {'message': "Account Removed"})
    

class view_events(TemplateView):
    template_name = 'admin/event_view.html'
    def get_context_data(self, **kwargs):
        context = super(view_events,self).get_context_data(**kwargs)

        event_list = Add_Events.objects.all()

        context['event_list'] = event_list
        return context
    
class view_products(TemplateView):
        template_name = 'admin/product_view.html'
        def get_context_data(self, **kwargs):
          context = super(view_products,self).get_context_data(**kwargs)
          pd_list = Add_Products.objects.all()
          context['pd_list'] = pd_list
          return  context
    
        

    
    
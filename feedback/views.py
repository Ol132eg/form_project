from django.shortcuts import render
from django.http import HttpResponseRedirect


from.forms import FeedbackForm
from.models import Feedback
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView,CreateView, UpdateView



# Create your views here.
#class FeedBackView(View):
#    def get(self, request):
#        form = FeedbackForm()
#        return render(request, 'feedback/feedback.html', context={'form': form})
#
#    def post(self, request):
#        form = FeedbackForm(request.POST)
#        if form.is_valid():
#            print(form.cleaned_data)
#            form.save()
#            return HttpResponseRedirect('/done')
#        else:
#            form = FeedbackForm()
#        return render(request, 'feedback/feedback.html', context={'form': form})

class FeedBackViewUpdate(UpdateView):
    model = Feedback
    form_class = FeedbackForm
    template_name ='feedback/feedback.html'
    success_url = '/done'
class FeedBackView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name ='feedback/feedback.html'
    success_url = '/done'

#    def form_valid(self, form):
#        form.save()
#        return super(FeedBackView,self).form_valid()

#def index(request):
#    if request.method =='POST':
#        form = FeedbackForm(request.POST)
#        if form.is_valid():
#            print(form.cleaned_data)
#            #feed=Feedback(
#            #    name=form.cleaned_data['name'],
#            #    surname=form.cleaned_data['surname'],
#            #    feedback=form.cleaned_data['feedback'],
#            #    rating=form.cleaned_data['rating']
#            #)
#            #feed.save()
#            form.save()
#            return HttpResponseRedirect('/done')
#    else:
#        form = FeedbackForm()
#    return render(request,'feedback/feedback.html',context={'form':form})

#def update_feedback(request,id_feedback):
#    feed=Feedback.objects.get(id=id_feedback)
#    if request.method == 'POST':
#        form = FeedbackForm(request.POST,instance=feed)
#        if form.is_valid():
#            print(form.cleaned_data)
#            form.save()
#            return HttpResponseRedirect(f'/{id_feedback}')
#    else:
#        form = FeedbackForm(instance=feed)
#    return render(request,'feedback/feedback.html',context={'form':form})

class UpdateFeedbackView(View):
    def get(self, request, id_feedback):
        feed = Feedback.objects.get(id=id_feedback)
        form = FeedbackForm(instance=feed)
        return render(request, 'feedback/feedback.html', context={'form': form})

    def post(self, request, id_feedback):
        feed = Feedback.objects.get(id=id_feedback)
        form = FeedbackForm(request.POST, instance=feed)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/done')
        form = FeedbackForm(instance=feed)
        return render(request, 'feedback/feedback.html', context={'form': form})








#def done(request):
#
#    return render(request,'feedback/done.html')

class DoneView(TemplateView):
#    def get(self, request):
#        return render(request, 'feedback/done.html')
    template_name = 'feedback/done.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['name']='Иванов И.И.'
        context['date'] = '21.02.24'
        return context

#class ListFeedBack(TemplateView):
#    template_name = 'feedback/list_feedback.html'
#    def get_context_data(self,**kwargs):
#        context=super().get_context_data(**kwargs)
#        context['all_feed'] = Feedback.objects.all()
#        return context

class ListFeedBack(ListView):
    template_name = 'feedback/list_feedback.html'
    model = Feedback
    context_object_name = 'feedback'

    def get_queryset(self):
        queryset = super().get_queryset()
#        filter_qs=queryset.filter(rating__gt=4)
#        return filter_qs
        return queryset



#class DetailFeedBack(TemplateView):
#    template_name = 'feedback/detail_feedback.html'
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['id_feedback'] = Feedback.objects.get(id=kwargs.get('id_feedback'))
#        return context

class DetailFeedBack(DetailView):
    template_name = 'feedback/detail_feedback.html'
    model = Feedback
#    context_object_name = 'feedbacks'

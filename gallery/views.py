from django.shortcuts import render
from django.views import View
from.forms import GalleryUploadForm
from django.http import HttpResponseRedirect
from.models import Gallery
from django.views.generic.edit import CreateView
from django.views.generic import ListView


# Create your views here.
class ListGallery(ListView):
    model = Gallery
    template_name = 'gallery/list_file.html'
    context_object_name = 'records'



#def storage_file(file):
#    with open ("C:\\Users\\ADMIN\\myDjangoProjects\\form_project\\gallery_tmp\\new_image.jpg", "wb+") as new_file:
#    with open ("gallery_tmp/new_image.jpg", "wb+") as new_file:
#        for chunk in file.chunks():
#            new_file.write(chunk)


class CreateGalleryView(CreateView):
    model = Gallery
    template_name = "gallery/load_file.html"
    fields="__all__"
    success_url = '/load_image'
#class GalleryView(View):
#
#    def get(self, request):
#        form = GalleryUploadForm()
#        return render(request, 'gallery/load_file.html', {'form': form })
#    def post(self, request):
#        form = GalleryUploadForm(request.POST, request.FILES)
#        if form.is_valid():
#            new_image =Gallery(image =form.cleaned_data['image'])
##            storage_file(request.FILES['image'])
#            new_image.save()
#
#            return HttpResponseRedirect('load_image')
#        return render(request, 'gallery/load_file.html',{'form':form})

# Create your views here.


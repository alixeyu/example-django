from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic.edit import FormView

from .forms import PictureForm
from .models import Picture


def test(request):
    return JsonResponse(status=200, data={"message": "Hello, world!"})

def home(request):
    context = {}

    context['images'] = Picture.objects.all()

    return render(request, template_name='home.html', context=context)


class LoadPicture(FormView):
    form_class = PictureForm
    template_name = 'home.html'

    def form_valid(self, form):
        form.save()
        return redirect('home')

    def form_invalid(self, form):
        return redirect('home')

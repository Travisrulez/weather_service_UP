from django.shortcuts import redirect, render
from django.views import View

class dash(View):

    def get(self, request, *args, **kwargs):
        return redirect('weather:login')


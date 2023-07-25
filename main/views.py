from django.shortcuts import render
from django.views import View


class Index(View):
    def get(self, request):
        context = {
            'title': 'Index'
        }
        return render(request, '../templates/index.html')

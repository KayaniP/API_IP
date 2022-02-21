from django.shortcuts import render
import ipapi


# Create your views here.


def Index(request):

        search = request.POST.get('search')
     
        data = ipapi.location(ip=search, output='json')

        context = {"data": data}

        return render(request, 'index.html', context)
from unicodedata import name
from django.shortcuts import render
from .models import Section

def index(request):
    
    if request.method == 'POST':
        get_the_value = request.POST.get('section_name')
        selected_parent = request.POST.get('parents')
        if selected_parent == None:
            Section.objects.create(name=get_the_value)
        else:
            parent = Section.objects.get(name=selected_parent)
            Section.objects.create(name=get_the_value, parent=parent)
    return render(request,'create_section/index.html',{'sections': Section.objects.all()})
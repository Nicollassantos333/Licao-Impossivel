# Abra o userprofile/views.py e mude de:
def home(request):
    return render(request, 'index.html')

# Para:
def home_view(request):
    return render(request, 'index.html')

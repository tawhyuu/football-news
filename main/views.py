from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406361536',
        'name': 'Tangguh Ambha Wahyuga',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
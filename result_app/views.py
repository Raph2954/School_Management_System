from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from result_app.forms import ResultForm


@login_required
def ResultView(request):
    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'secondary/result_success.html', {'form':form} )
    else:
        form = ResultForm()
        return render(request, 'secondary/result.html', {'form':form})


def ResultsuccessView(request):
    return render(request, 'secondary/result_success.html')

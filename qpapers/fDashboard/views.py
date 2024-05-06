from django.shortcuts import render
from django.shortcuts import render, redirect
from core.forms import QuestionForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def dash_view(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.added_by = request.user
            question.save()
            return redirect('fdash:index')  # Replace with a valid view name
    else:
        form = QuestionForm()

    context = {
        'form': form,
    }
    return render(request, 'fDash/index.html',context)



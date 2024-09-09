from django.shortcuts import render, get_object_or_404, redirect
from .models import Study
from .forms import StudyForm

def study_list(request):
    studies = Study.objects.all()
    return render(request, 'studies/study_list.html', {'studies': studies})

def study_detail(request, pk):
    study = get_object_or_404(Study, pk=pk)
    return render(request, 'studies/study_detail.html', {'study': study})

def study_create(request):
    if request.method == "POST":
        form = StudyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('study_list')
    else:
        form = StudyForm()
    return render(request, 'studies/study_form.html', {'form': form})

def study_update(request, pk):
    study = get_object_or_404(Study, pk=pk)
    if request.method == "POST":
        form = StudyForm(request.POST, instance=study)
        if form.is_valid():
            form.save()
            return redirect('study_list')
    else:
        form = StudyForm(instance=study)
    return render(request, 'studies/study_form.html', {'form': form})

def study_delete(request, pk):
    study = get_object_or_404(Study, pk=pk)
    if request.method == "POST":
        study.delete()
        return redirect('study_list')
    return render(request, 'studies/study_confirm_delete.html', {'study': study})
def delete_selected_studies(request):
    if request.method == "POST":
        selected_studies = request.POST.getlist('selected_studies')
        for study_id in selected_studies:
            study = get_object_or_404(Study, pk=study_id)
            study.delete()
        return redirect('study_list')
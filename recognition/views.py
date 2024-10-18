from django.shortcuts import render, redirect
from .models import Student, Achievement, Batch
from .forms import StudentForm, AchievementForm

# Create your views here.

# View to create a student
def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            student = form.save(commit=False)
            student.calculate_weighted_score()
            student.save()
            return redirect('student-list')
    else:
        form = StudentForm()
    return render(request, 'recognition/student_form.html', {'form': form})

# View to list all students
def student_list(request):
    batches = Batch.objects.all();
    top_students = {}
    for batch in batches:
        students = Student.objects.filter(batch=batch).order_by('-weighted_score')[:3]
        top_students[batch] = students
    return render(request, 'recognition/student_list.html', {'top_students': top_students})

# View to create an achievement
def create_achievement(request):
    if request.method == 'POST':
        form = AchievementForm(request.POST)
        if form.is_valid():
            achievement = form.save()
            student = achievement.student
            student.calculate_weighted_score()
            form.save()
            return redirect('achievement-list')
    else:
        form = AchievementForm()
    return render(request, 'recognition/achievement_form.html', {'form': form})

# View to list all achievements
def achievement_list(request):
    achievements = Achievement.objects.all()
    return render(request, 'recognition/achievement_list.html', {'achievements': achievements})
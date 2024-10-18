from django.db import models

# Create your models here.

class Batch(models.Model):
    batch_year = models.IntegerField()
    total_students = models.IntegerField()
    
    def __str__(self):
        return f"Batch {self.batch_year}"
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    gpa = models.FloatField()
    core_course_score = models.FloatField()
    hackathon_score = models.FloatField()
    paper_presentation_score = models.FloatField()
    teaching_assistance_score = models.FloatField()
    weighted_score = models.FloatField(default=0.0, editable=False)
    
    def save(self, *args, **kwargs):
        # Automatically calculate the weighted score based on other scores
        self.weighted_score = (self.gpa * 0.4 +  # Example weight
                               self.core_course_score * 0.3 +
                               self.hackathon_score * 0.1 +
                               self.paper_presentation_score * 0.1 +
                               self.teaching_assistance_score * 0.1)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class Achievement(models.Model):
    ACHIEVEMENT_TYPES = [
        ('hackathon', 'Hackathon'),
        ('paper', 'Paper Presentation'),
        ('ta', 'Teaching Assistance'),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    achievement_type = models.CharField(max_length=20, choices=ACHIEVEMENT_TYPES)
    score = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f"{self.achievement_type} - {self.student.name}"
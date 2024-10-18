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
    
    def __str__(self):
        return self.name

    # Add the calculate_weighted_score method
    def calculate_weighted_score(self):
        # Example weight values
        gpa_weight = 0.4
        core_course_weight = 0.3
        hackathon_weight = 0.1
        paper_weight = 0.1
        teaching_assistance_weight = 0.1
        
        # Calculate weighted score
        self.weighted_score = (self.gpa * gpa_weight +
                               self.core_course_score * core_course_weight +
                               self.hackathon_score * hackathon_weight +
                               self.paper_presentation_score * paper_weight +
                               self.teaching_assistance_score * teaching_assistance_weight
        )
        
    def save(self, *args, **kwargs):
        # Calculate the weighted score before saving
        self.calculate_weighted_score()
        super().save(*args, **kwargs)

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
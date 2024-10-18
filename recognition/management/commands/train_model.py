
from django.core.management.base import BaseCommand
from sklearn.linear_model import LinearRegression
from recognition.models import Student
import numpy as np

class Command(BaseCommand):
    help = 'Train a machine learning model to rank students'

    def handle(self, *args, **kwargs):
        # Prepare the data for training
        students = Student.objects.all()
        X = np.array([[s.gpa, s.core_course_score, s.hackathon_score, s.paper_presentation_score, s.teaching_assistance_score] for s in students])
        y = np.array([s.weighted_score for s in students])  # Target values (currently the weighted score)

        # Train a simple linear regression model
        model = LinearRegression()
        model.fit(X, y)

        # Save the model coefficients as new weights (for illustration)
        new_weights = model.coef_

        self.stdout.write(self.style.SUCCESS(f'New Weights: {new_weights}'))

        # Optionally, update the model to use these new weights dynamically in your system

"""
Script for processing a students grades.
"""
from grades.predict import predict_score as p
from grades.result import get_grade as g

score_history = [50, 90, 100, 29]
predicted_score = p(score_history, 50) 

predicted_grade = g(predicted_score)
print(f'The students predicted grade is: {predicted_grade}')

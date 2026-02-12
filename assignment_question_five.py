#assignment_question_five.py

import pandas as pd

data_frame = pd.read_csv('student.csv')

def assign_grade_band(grade):
    if grade <= 9:
        return 'Low'
    elif 10 <= grade <= 14:
        return 'Medium'
    else:
        return 'High'

data_frame['grade_band'] = data_frame['grade'].apply(assign_grade_band)

summary = data_frame.groupby('grade_band').agg(
    number_of_students=('grade', 'count'),
    average_absences=('absences', 'mean'),
    percentage_internet=('internet', 'mean')
)

summary['percentage_internet'] = summary['percentage_internet']*100

summary.to_csv('student_bands.csv')

print(summary)

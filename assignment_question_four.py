#assignment_question_four.py

import pandas as pd

data_frame = pd.read_csv('student.csv')
filtered_data_frame = data_frame[(data_frame['studytime'] >= 3) & (data_frame['internet'] == 1) & (data_frame['absences'] <= 5)]

filtered_data_frame.to_csv('high_engagement.csv')

print(len(filtered_data_frame))
print(filtered_data_frame['grade'].mean())
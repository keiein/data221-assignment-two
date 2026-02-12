#assignment_question_six.py
import pandas as pd


data_frame = pd.read_csv('crime.csv')

def get_risk(crime_rate):
    if crime_rate >= 0.50:
        return "HighCrime"
    else:
        return "LowCrime"

data_frame['risk'] = data_frame['ViolentCrimesPerPop'].apply(get_risk)

average_unemployment = data_frame.groupby('risk')['PctUnemployed'].mean()

print(f"Average unemployment rate: \n{average_unemployment}")
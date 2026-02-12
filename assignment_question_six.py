#assignment_question_six.py
import pandas as pd


data_frame = pd.read_csv('crime.csv') #read csv

def get_risk(crime_rate): #function to determine high crime and low crime
    if crime_rate >= 0.50:
        return "HighCrime"
    else:
        return "LowCrime"

data_frame['risk'] = data_frame['ViolentCrimesPerPop'].apply(get_risk) #create a new column into the data frame

average_unemployment = data_frame.groupby('risk')['PctUnemployed'].mean() #grouping, averaging

print(f"Average unemployment rate: \n{average_unemployment}")
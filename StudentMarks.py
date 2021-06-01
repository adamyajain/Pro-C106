import plotly.express as px
import csv

with open('/data/StudentMarks.csv') as csv_file : 
    df = DictReader(csv_file)
    fig = px.scatter(df, x = "Roll No", y = "Marks In Percentage,Days Present")
    fig.show()
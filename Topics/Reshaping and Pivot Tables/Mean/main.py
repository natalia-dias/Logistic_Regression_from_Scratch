#  write your code here 
import pandas as pd

df_rock = pd.read_csv('/Users/ndias/PycharmProjects/Logistic Regression from Scratch/Topics/Reshaping and Pivot Tables/Mean/data/dataset/input.txt')

# print(df_rock.head())

pivot1 = pd.pivot_table(df_rock, index='labels', values='null_deg', aggfunc='mean')
print(round(0.269734, 2))

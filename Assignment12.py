import webbrowser as wb
import os

# Question 1
# Print the current day using Datetime module.
import datetime as dt
days = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
a = dt.datetime.today()
b = dt.date.weekday(a)
print("The day today is : "+days[b])

# Question 2
# Open your browser and play a video using web browser module in python.
Search = input("Please Enter The Title of The Video You Wanna See : ")
wb.open_new_tab('https://www.youtube.com/results?search_query={}'.format(Search))


# Question 3
# Write a program to rename all the files in a directory and convert them into .jpg file format.

Dir = os.listdir()
for i in range(1, len(Dir)-1):
    Dir[i], ext = os.path.splitext(Dir[i])
    os.rename(Dir[i]+'.txt', Dir[i]+'.jpg')
print(Dir)

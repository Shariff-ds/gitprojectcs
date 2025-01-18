import os
from random import randint
from datetime import datetime, timedelta

# Start date (January 19)
start_date = datetime(2025, 1, 19)
# End date (today)
end_date = datetime.today()

# Calculate the number of days between start_date and end_date
days_difference = (end_date - start_date).days

# Loop through the days from start_date to end_date
for i in range(days_difference + 1):
    # Calculate the current date for the commit
    commit_date = start_date + timedelta(days=i)
    # Format the date as a string
    commit_date_str = commit_date.strftime('%Y-%m-%d %H:%M:%S')

    # Random number of commits for each day
    for j in range(0, randint(1, 10)):
        with open('file.txt', 'a') as file:
            file.write(commit_date_str + '\n')
        # Add and commit changes with the specific date
        os.system('git add .')
        os.system(f'git commit --date="{commit_date_str}" -m "Commit on {commit_date_str}"')

# Push all commits to the remote repository
os.system('git push -u origin main')

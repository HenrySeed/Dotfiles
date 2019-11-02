import os

os.system("clear")
print("\n\n    Good Morning Henry")
print("    Pulling the latest version of AmI from git")

# Make sure the current Git is up to date
os.system("cd ~/AmI; git pull;")
print("    Done")

# Run the Good Morning script
os.system("osascript ~/Morning/GoodMorning.scpt")

# Facebook-Duplicate-Checker
Facebook Duplicate Checker

This is a basic Facebook fake account checker.

This software checks for accounts in the format
[firstname].[lastname].[number]

I have built here a simple program that scans through Facebook profiles in a certain
range (that you specify) that have the format [firstname].[lastname].[number] using an
exterior browser. This then checks each profile whether they have a default profile picture
or not. If they do then, it is highly likely a fake account. It is then flagged and
outputted into a text file.

ReadMe!
1. Please make sure that the chromedriver.exe is in the same folder as this script
2. Please do not delete any file that is in this folder
3. The script CAN run in the background just do not close this script and the browser
4. This will generate a text file containing a list of possible fake accounts based on your search
5. This DOES NOT collect / send information about ANYTHING

Disclaimer: This program is intended for informational and personal use only.
This program is released as-is. I do not take any responsibility for anything you
do and happens to your account / device while using this program.

FAQ:

1. Why does this require me to login to my facebook?
  - Some fake accounts are private, hence you could not see them when you are not logged in. 

2. What is the criteria for a facebook profile to be flagged as fake
  - the format of the facebook account link is [firstname].[lastname].[number]
  - there is no profile picture
  
3. Can I download your code and run it myself? 
  - Yes! You could


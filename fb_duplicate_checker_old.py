from selenium import webdriver
import time, os, getpass, sys
from msvcrt import getch

print('''
This is a basic Facebook fake account checker.

This software checks for accounts in the format
<firstname>.<lastname>.<number>

ReadMe!
1. Please make sure that the chromedriver.exe is in the same folder as this script
2. Please do not delete any file that is in this folder
3. The script CAN run in the background just do not close this script and the browser
4. This will generate a text file containing a list of possible fake accounts based on your search
5. This DOES NOT collect / send information about ANYTHING

Disclaimer: This program is intended for informational and personal use only.
This program is released as-is. I do not take any responsibility for anything you
do and happens to your account / device while using this program. \n\n''')

#asterisk password maker
def pyssword(prompt='Password: '):
    '''
        Prompt for a password and masks the input.
        Returns:
            the value entered by the user.
    '''

    if sys.stdin is not sys.__stdin__:
        pwd = getpass.getpass(prompt)
        return pwd
    else:
        pwd = ""
        sys.stdout.write(prompt)
        sys.stdout.flush()
        while True:
            key = ord(getch())
            if key == 13: #Return Key
                sys.stdout.write('\n')
                return pwd
                break
            if key == 8: #Backspace key
                if len(pwd) > 0:
                    # Erases previous character.
                    sys.stdout.write('\b' + ' ' + '\b')
                    sys.stdout.flush()
                    pwd = pwd[:-1]
            else:
                # Masks user input.
                char = chr(key)
                sys.stdout.write('*')
                sys.stdout.flush()
                pwd = pwd + char

#path chromedriver
path = str(os.path.dirname(os.path.abspath(__file__))) + '\chromedriver.exe'
if os.path.isfile(path) == True:

    #inpits
    fname = input('First Name: ').lower()
    lname = input('Last Name: ').lower()
    ran = int(input('Lower Bound Search: '))
    ran1 = int(input('Upper Bound Search: '))
    temail = input('Email: ')
    tpass = pyssword()

    print(f'\nChecking Facebook accounts from {fname}.{lname}.{ran} to {fname}.{lname}.{ran1}')

    #errors
    error1 = "Sorry, this content isn't available right now"
    error2 = "The link you followed may have expired, or the page may only be visible to an audience you're not in."
    error3 = "This page isn't available"
    error4 = "The link you followed may be broken, or the page may have been removed."

    driver = webdriver.Chrome(path)
    driver.get("http://www.facebook.com/")

    #logging in
    driver.find_element_by_id('email').send_keys(temail)
    time.sleep(1)
    driver.find_element_by_id('pass').send_keys(tpass)
    time.sleep(1)
    driver.find_element_by_id('u_0_b').click()
    time.sleep(5)

    #output text file
    output = open('possible_fake_accounts.txt','a')

    #run range
    for i in range(ran,ran1+1):
        driver.get("http://www.facebook.com/{}.{}.{}".format(fname,lname,str(i)))
        source = driver.page_source
        if  error1 in source or error2 in source or error3 in source or error4 in source:
            pass
        else:
            print("ACCOUNT EXISTS: {}.{}.{}".format(fname,lname,str(i)))

            photo1 = "5F05BCF4"
            photo2 = "5F03FCA4"

            if photo1 in source or photo2 in source:
                print("POSSIBLY A FAKE ACCOUNT: {}.{}.{}".format(fname,lname,str(i)))
                output.write("http://www.facebook.com/{}.{}.{}".format(fname,lname,str(i)))

    output.close()
    driver.quit()

    exit = input('\nPress ENTER to EXIT')

else:
    print('Please check that the chromedriver.exe is in the same folder as this program')
    exit = input('\nPress ENTER to EXIT')
    sys.exit()

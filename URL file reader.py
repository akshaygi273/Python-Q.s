# 4. Provide a program to read the file from URL and display the content
# in terminal.
# • The file URL has to be input by the user.
# • The program has to work from the terminal. The input and output have been taken/displayed
# on the terminal.


import requests
import sys

while True:
    try:    
        # link = 'http://google.com/'
        link = input('Enter the url (starting with http://)  '  ).strip()
        var = input('To close enter - X \nTo Continue enter - C   ').strip()
        if var == 'X' or var == 'x':
            break
        f = requests.get(link)
        print(f.text)
        var = input('To close enter - X \nTo Continue enter - C   ').strip()
        if var == 'X' or var == 'x':
            break

    except Exception as e:
        print(e)
        print('Error while connecting url, please enter valid URL.')
        var = input('To close enter - X \nTo Continue enter - C   ').strip()
        if var == 'X' or var == 'x':
            break
            sys.exit()


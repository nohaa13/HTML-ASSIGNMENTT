Python 3.11.6 (tags/v3.11.6:8b6ee5b, Oct  2 2023, 14:57:12) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> create timer                                                                                                                                                    import time
... def countdown(t): 
...     
...     while t: 
...         mins, secs = divmod(t, 60) 
...         timer = '{:02d}:{:02d}'.format(mins, secs) 
...         print(timer, end="\r") 
...         time.sleep(1) 
...         t -= 1
...       
...     print('Fire in the hole!!') 
...   
...   
... # input time in seconds 
... t = input("Enter the time in seconds: ") 
...   
... # function call 

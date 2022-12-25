import pywhatkit 
n=input('enter number with  country code: ')
msg= str(input('enter the msg  : '))
m= int(input('enter the timespan , hours '))
s = int(input('enter the timespan ,  minutes '))
pywhatkit.sendwhatmsg(n ,  msg , m, s ) 


from .models import *
import pywhatkit

def whtatsapp():
    obj = Student.objects.get(pk=1).filter('phone'='phone')

    pywhatkit.sendwhatmsg('obj', 'ok', 13,20)

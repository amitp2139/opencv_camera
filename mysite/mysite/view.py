# i have created this website
from django.http import HttpResponse
from django.shortcuts import render
import cv2


def index(request):
    return render(request,'index.html')
def about(request):
    '''vid = cv2.VideoCapture(0)
    while(True):
        ret, frame = vid.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # After the loop release the cap object
    vid.release() 
    # Destroy all the windows
    cv2.destroyAllWindows()'''
    return HttpResponse('''<button>click for camera</button>''')

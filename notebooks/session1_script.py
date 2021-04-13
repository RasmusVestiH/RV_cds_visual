#Assist for python shortcuts: https://miro.medium.com/max/1400/1*totJoCc3l7BdeY-mEQ6HHQ.png
# Required libraries
import sys 
sys.path.append(os.path.join(".."))
##Import openCV
import cv2
import numpy as np
from utils.imutils import jimshow

#Translate function
def translate(image, x, y):
    #Define translation matrix here 
    M = np.float64([[1,0,x],
                  [0,1,y]])
    #Perform translation on our chosen image
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    
    #Return the translated image
    return shifted

def main():
        #core logic of the programme
        
#if script is being called from command line 
if __name__ == "__main__":
    #then execute the function called main()
    main()
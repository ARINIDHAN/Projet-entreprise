#last modification date: 06/01/2022
#created by:ARICH
import cv2
#from datetime import datetime
from datetime import date
#times = datetime.now()
cam = cv2.VideoCapture(0)
cv2.namedWindow("test")
img_counter = 0
DATE= date.today()

while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k % 256 == 27:
            # 27=Echap
        print("Escape hit, closing...")
        break
    elif k % 256 == 32:
        # 32=ESPACE
        img_name = input ('Nom image : ')+'_'+input('Nom employer:')
        #Avec le temps le nom du fichier est trop volumineux donc dificile de l'enregister
        img_name = format(DATE)+"_"+img_name +"_"+ format(img_counter) # + format(times)
        #{} represente le nom a mettre devant le .png, se qui vient derriere est le nom a mettre.
        img_name = "{}.png".format(img_name)
        print("{} written!".format(img_name))
        img_counter += 1
        sauvegarde = input('save_or_not:')

        if sauvegarde == format(987654321):
            # not cv2.imwrite( img_name, frame)
            print("not saved!".format(img_name))

        elif sauvegarde == format(123456789):
            cv2.imwrite(img_name, frame)
            #cv2.imshow(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1
            # Probleme: si on a 2 foix le meme nom ancien image se supprime

cam.release()

cv2.destroyAllWindows()
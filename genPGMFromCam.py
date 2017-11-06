import os
import cv2

datapath = "C:/Users/weisuzhong/PycharmProjects/testforme/face_data/"

def mkdirectory(perDirToFaces):
    perdir = datapath + str(perDirToFaces)
    if not os.path.exists(perdir):
        os.mkdir(perdir)
    return perdir + '/'


def generate(perDirToFaces):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    camera = cv2.VideoCapture(0)
    count = 0
    while (True):
        ret, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            f = cv2.resize(gray[y:y+h, x:x+w], (200, 200))
            perdir = mkdirectory(perDirToFaces)
            cv2.imwrite(perdir + '%s.pgm' % str(count), f)
            print count
            count += 1

        if(count >= 20):
            break

        cv2.imshow("camera", frame)

        if cv2.waitKey(1000 / 12) & 0xff == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    generate('zyf')
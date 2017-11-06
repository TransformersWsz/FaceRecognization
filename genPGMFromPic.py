import os
import cv2

datapath = "C:/Users/weisuzhong/PycharmProjects/testforme/face_data/"

def mkdirectory(perDirToFaces):
    perdir = datapath + str(perDirToFaces)
    if not os.path.exists(perdir):
        os.mkdir(perdir)
    return perdir + '/'


def generate(dirofSourcePic,perDirToFaces):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    count = 0
    # while count <= 28:
    #     img = cv2.imread(dirofSourcePic + '45-%s.jpg'%str(count))
    #     # img = cv2.imread(dirofSourcePic + '3-1.jpeg')
    #     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #     faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    #     for (x, y, w, h) in faces:
    #         img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    #         f = cv2.resize(gray[y:y + h, x:x + w], (200, 200))
    #         perdir = mkdirectory(perDirToFaces)
    #         cv2.imwrite(perdir + '%s.pgm' % str(count), f)
    #         print count
    #         count += 1

    while count <= 0:
        img = cv2.imread(dirofSourcePic + '2-7.jpeg')
        # img = cv2.imread(dirofSourcePic + '3-1.jpeg')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            f = cv2.resize(gray[y:y + h, x:x + w], (200, 200))
            perdir = mkdirectory(perDirToFaces)
            cv2.imwrite(perdir + '%s.pgm' % str(count), f)
            print count
            count += 1

if __name__ == "__main__":
    generate('C:/Users/weisuzhong/Desktop/image/','lry')
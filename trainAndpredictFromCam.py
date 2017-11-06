import cv2
import csv
import numpy as np

# get data from csv file
def getCSVData(csvFile):
    csvfile = open(csvFile,'r')
    reader = csv.reader(csvfile)
    imagespaths = []
    strlabels = []
    for line in reader:
        imagespaths.append(line[0])
        strlabels.append(line[1])
    csvfile.close()
    return (imagespaths,strlabels)

# train data and predict
def trainAndPredict(csvFile):
    imagespaths,strlabels = getCSVData(csvFile)
    model = cv2.createEigenFaceRecognizer()

    images = []
    intlabels = []
    for i in range(len(imagespaths)):
        images.append(cv2.imread(imagespaths[i],0))
        intlabels.append(int(strlabels[i]))
    model.train(np.asarray(images),np.asarray(intlabels))
    model.save('model.xml')

    # predict face
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    webcam = cv2.VideoCapture(0)
    while True:
        ret, frame = webcam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            f = cv2.resize(gray[y:y+h, x:x+w], (200, 200))
            prediction = model.predict(f)
            print type(prediction)
            print prediction

        cv2.imshow('camera', frame)
        if cv2.waitKey(1000 / 12) & 0xff == ord("q"):
            break
    webcam.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    trainAndPredict('train.csv')





import cv2

def genRGBPic():
    camera = cv2.VideoCapture(0)
    count = 0
    while True:
        ret, frame = camera.read()

        if cv2.waitKey(1000 / 12) & 0xff == ord("q"):
            break
        cv2.imshow("camera", frame)
        cv2.imwrite('45-%s.jpg'%(str(count)),frame)
        count += 1
        if count > 29:
            break
    camera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    genRGBPic()
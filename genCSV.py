# import os
#
# # datapath = 'C:/Users/weisuzhong/PycharmProjects/testforme/face_data/'
# def genCSV(datapath):
#     dirList = os.listdir(datapath)
#     label = -1
#
#     f = open('train.csv','wb')
#     for name in dirList:
#         path = datapath + str(name) + '/'
#         print path  # C:/Users/weisuzhong/PycharmProjects/testforme/face_data/wsz
#         cpath = str(path)[len(datapath):str(path).rfind('/')+1] # wsz/
#
#         label += 1
#
#         fileList = os.listdir(path) # 0.pgm,1.pgm ......
#         for fileName in fileList:
#             print datapath + cpath + fileName + ',' + str(label)
#             f.write(datapath + cpath + fileName + ',' + str(label) + '\n')
#     f.close()
#
# if __name__ == '__main__':
#     genCSV('C:/Users/weisuzhong/PycharmProjects/testforme/face_data/')









import os
import csv

# datapath = 'C:/Users/weisuzhong/PycharmProjects/testforme/face_data/'
def genCSV(datapath):
    dirList = os.listdir(datapath)
    label = -1

    f = open('train.csv','wb')
    csvwriter = csv.writer(f)
    for name in dirList:
        path = datapath + str(name) + '/'
        print path  # C:/Users/weisuzhong/PycharmProjects/testforme/face_data/wsz
        cpath = str(path)[len(datapath):str(path).rfind('/')+1] # wsz/

        label += 1

        fileList = os.listdir(path) # 0.pgm,1.pgm ......
        for fileName in fileList:
            print datapath + cpath + fileName + ',' + str(label)
            csvwriter.writerow([datapath + cpath + fileName,str(label)])
            # f.write(datapath + cpath + fileName + ',' + str(label) + '\n')
    f.close()

if __name__ == '__main__':
    genCSV('C:/Users/weisuzhong/PycharmProjects/testforme/face_data/')
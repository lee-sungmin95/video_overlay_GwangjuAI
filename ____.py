import os
import cv2
import Rotate_function as rf

def VedioCapture ():
    vidcap = cv2.VideoCapture(r'C:\Users\user\vs_space\intflow_homework_1024\drive-download-20211024T024937Z-001\h264_01_20211001162059677_1\h264_01_20211001162059677_1.mp4')
    count = 0
    while True:
        success,image = vidcap.read()
        if not success:
            break
        cv2.imwrite(os.path.join(folder,"frame{:d}.jpg".format(count)), image)     # save frame as JPEG file
        count += 1
    print("{} images are extacted in {}.".format(count,folder))

def writetxt_file():
    f = open("drive-download-20211024T024937Z-001\h264_01_20211001162059677_1\h264_01_20211001162059677_1_det.txt", 'r')
    lines = f.readlines()
    text_line = []
    test_line =[text_line.strip().split(',') for text_line in lines[1:6]]
    for text_line in lines[1:6]:
        text_line.append(text_line.strip().split(','))
        # print(line, type(line))
    f.close()
    print(text_line)

def main():

    pass

if __name__ == '__main__':
    writetxt_file()
    
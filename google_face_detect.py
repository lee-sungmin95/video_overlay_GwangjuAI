import cv2
import matplotlib.pyplot as plt
import pandas as pd

def sub_2_main():
    VIDEO_FILE_PATH = 'drive-download-20211024T024937Z-001/mounting_000/mounting_000.mp4'
    cap = cv2.VideoCapture(VIDEO_FILE_PATH)   # 동영상 파일 열기
    if cap.isOpened() == False:                                     #잘 열렸는지 확인
        print ('Can\'t open the video (%d)' % (VIDEO_FILE_PATH))
        exit()

    titles = ['orig']
    
    for t in titles:                    #윈도우 생성 및 사이즈 변경
        cv2.namedWindow(t)

    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)        #재생할 파일의 넓이 얻기
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)        #재생할 파일의 높이 얻기
    fps = cap.get(cv2.CAP_PROP_FPS)                    #재생할 파일의 프레임 레이트 얻기
    
    print('width {0}, height {1}, fps {2}'.format(width, height, fps))

    #XVID가 제일 낫다고 함.
    #linux 계열 DIVX, XVID, MJPG, X264, WMV1, WMV2.
    #windows 계열 DIVX

    fourcc = cv2.VideoWriter_fourcc(*'DIVX')      #저장할 비디오 코덱
    filename = 'sprite_with_face_detect.avi'      #저장할 파일 이름                  ####이름 내가 수정하면됨

    out = cv2.VideoWriter(filename, fourcc, fps, (int(width), int(height)))   #파일 stream 생성
                                            #filename : 파일 이름, fourcc : 코덱, fps : 초당 프레임 수, width : 넓이, height : 높이

    #얼굴 인식용
    face_cascade = cv2.CascadeClassifier()
    face_cascade.load(r'C:\Users\user\vs_space\intflow_homework_1024\venv\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')


    while(True):
        ret, frame = cap.read()    #파일로 부터 이미지 얻기
        if frame is None:       #더 이상 이미지가 없으면 종료
            break;               #재생 다 됨

        grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)    #얼굴인식 영상 처리
        # dst(출력이미지) = cv2.cvtcolor(src, code, dstCn)는 입력 이미지(src), 색상 변환 코드(code), 출력 채널(dstCn)으로 출력 이미지(dst)을 생성합니다.
        blur =  cv2.GaussianBlur(grayframe,(5,5), 0)
        faces = face_cascade.detectMultiScale(blur, 1.8, 2, 0, (50, 50))
        
          #blurscale 이미지 입력, 
        for (x,y,w,h) in faces:                              #원본 이미지에 얼굴 인식된 부분 표시
            cx = int(x+(w/2))
            cy = int(y+(h/2))
            cr = int(w/2)
            cv2.circle(frame,(cx,cy),cr,(0,255,0),3)
            # cv2.ellipse(img= frame, center= (xc,yc), axes= (width_half,height_half), angle=theta,
            #                                          startAngle= 0, endAngle=360, color=(0, 255, 0), thickness=2)

        cv2.imshow(titles[0],frame)      # 얼굴 인식된 이미지 화면 표시

        out.write(frame)                 # 인식된 이미지 파일로 저장
        if cv2.waitKey(1) == 27:         #1ms 동안 키입력 대기
            break;

    cap.release()    #재생 파일 종료
    out.release()    #저장 파일 종료
    cv2.destroyAllWindows()    #윈도우 종료

def sub_main():
    face_cascade = cv2.CascadeClassifier()
    face_cascade.load(r'C:\Users\user\vs_space\intflow_homework_1024\venv\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
    print(face_cascade)
if __name__ == '__main__':
    # sub_2_main()
    sub_main()
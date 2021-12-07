import cv2
from typing import List
import Rotate_function as rf
import os


def explore_get_coordinates() -> List[List[List[int]]]:
    path = '../drive-download-20211024T024937Z-001/h264_01_20211001162059677_1/h264_01_20211001162059677_1_det.txt'

    with open(file=path, mode='r') as file:
        strings = file.readlines()
        # print(f'가져온 데이터 개수 : {len(strings[1:4])} 개 / Data Type : {type(strings[1])}')
        # print(f'가져온 데이터 List : {strings[1:4]}')
        temps = [str_line[:-2].split(',')[:6]
                 for str_line in strings[1:]
        ]

    rotated_xy: List[List[List[int]]] = [
        [int(temp[0]), rf.rotate_box_dot(x_cen=float(temp[1]), y_cen=float(temp[2]), width=float(temp[3]), height=float(temp[4]), theta=float(temp[5]))]
        for temp in temps
    ]
    # print('회전한 값 x1, 회전한 값 y1, ..., x4, y4')
    # print(f'회전된 데이터 List : {rotated_xy}')

    return rotated_xy


def explore_main_get_coordinates() -> List[List[int]]:
    path = '../drive-download-20211024T024937Z-001/h264_01_20211001162059677_1/h264_01_20211001162059677_1_det.txt'

    with open(file=path, mode='r') as file:
        strings = file.readlines()
        # print(f'가져온 데이터 개수 : {len(strings[1:4])} 개 / Data Type : {type(strings[1])}')
        # print(f'가져온 데이터 List : {strings[1:4]}')
        temps = [str_line[:-2].split(',')[1:6]
                 for str_line in strings[1:4]
        ]

    rotated_xy: List[List[int]] = [
        rf.rotate_box_dot(x_cen=float(temp[0]), y_cen=float(temp[1]), width=float(temp[2]), height=float(temp[3]), theta=float(temp[4]))
        for temp in temps
    ]
    # print('회전한 값 x1, 회전한 값 y1, ..., x4, y4')
    # print(f'회전된 데이터 List : {rotated_xy}')

    return rotated_xy


def explore_get_imagelist():
    # script_path = os.path.dirname(__file__)
    # print(script_path)
    # script_path = os.chdir(script_path)
    # print(script_path)

    path = '../test'
    list_data = os.listdir(path=path)
    print(list_data)
    # print(len(list_data))
    return list_data # == os.listdir(path=path)


def get_file_number(img_filename: str) -> int:
    # 정규식 사용하면 더 편하다.
    img_filename = img_filename[:-4]
    number = img_filename[5:]
    return int(number)

def get_imagefile_path():
    imgs_filename = explore_get_imagelist()

    filepaths = [os.path.join('../test', img_fn)
                 for img_fn in imgs_filename
    ]
    return filepaths


def sub_main():
    imgs_filename = explore_get_imagelist()
    rotated_xy = explore_get_coordinates()

    for img_fn in imgs_filename:
        number = get_file_number(img_fn)
        # 탐색 알고리즘 필요 연산 시간 줄여줌
        coordinates = []
        for data in rotated_xy: # data ex) ['18935', [383, 2, 90, 2, 90, 139, 383, 138]], ['18932', [377, 327, 61, 364, 78, 506, 394, 469]]
            if number == data[0]:
                coordinates.append(data[1])

    # 추가작업 해야할 사항
    # 아래 코드 위 반복문에 포함시켜야 함
    filepaths = get_imagefile_path()

    for path in filepaths:
        cap = cv2.VideoCapture(path)

        while cap.isOpened():
            ret, frame = cap.read()

            if ret:
                img = cv2.cvtColor(src=frame, code=cv2.IMREAD_COLOR)

                # draw image
                for xy_list in coordinates:
                    cv2.line(img=img, pt1=(xy_list[0], xy_list[1]), pt2=(xy_list[2], xy_list[3]), color=(0, 200, 0),
                             thickness=2, lineType=cv2.LINE_AA)
                    cv2.line(img=img, pt1=(xy_list[2], xy_list[3]), pt2=(xy_list[4], xy_list[5]), color=(0, 200, 0),
                             thickness=2, lineType=cv2.LINE_AA)
                    cv2.line(img=img, pt1=(xy_list[4], xy_list[5]), pt2=(xy_list[6], xy_list[7]), color=(0, 200, 0),
                             thickness=2, lineType=cv2.LINE_AA)
                    cv2.line(img=img, pt1=(xy_list[6], xy_list[7]), pt2=(xy_list[0], xy_list[1]), color=(0, 200, 0),
                             thickness=2, lineType=cv2.LINE_AA)

                cv2.imshow(winname='Mywindow', mat=img)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

    cv2.destroyAllWindows()


def main():
    path = '../test/frame0.jpg'
    rotated_xy = explore_main_get_coordinates()

    cap = cv2.VideoCapture(path)

    while cap.isOpened():
        ret, frame = cap.read()

        if ret:
            img = cv2.cvtColor(src=frame, code=cv2.IMREAD_COLOR)

            # draw image
            for xy_list in rotated_xy:
                cv2.line(img=img, pt1=(xy_list[0], xy_list[1]), pt2=(xy_list[2], xy_list[3]), color=(0, 200, 0), thickness=2, lineType=cv2.LINE_AA)
                cv2.line(img=img, pt1=(xy_list[2], xy_list[3]), pt2=(xy_list[4], xy_list[5]), color=(0, 200, 0), thickness=2, lineType=cv2.LINE_AA)
                cv2.line(img=img, pt1=(xy_list[4], xy_list[5]), pt2=(xy_list[6], xy_list[7]), color=(0, 200, 0), thickness=2, lineType=cv2.LINE_AA)
                cv2.line(img=img, pt1=(xy_list[6], xy_list[7]), pt2=(xy_list[0], xy_list[1]), color=(0, 200, 0), thickness=2, lineType=cv2.LINE_AA)

            img = cv2.resize(img, dsize=(640, 480), interpolation=cv2.INTER_AREA)
            cv2.imshow(winname='Mywindow', mat=img)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
    # sub_main()
    # explore_get_coordinates()
    # explore_get_imagelist()
    # get_imagefile_path()
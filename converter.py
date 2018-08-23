
'''
Multiple Camera H264 files logging python script

example:
    >>python3 converter.py --num 3
out:
    ./IMAGE/video_first, ./IMAGE/video_second, ./IMAGE/video_thrid, ./IMAGE/video_merge

made by Yeacheol Kim
'''


import cv2
import pdb
import pathlib
import argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--num', type=int, default=1, help='Number of Camera')
args = parser.parse_args()

name = ['video_first', 'video_second', 'video_third']
x_ = [[0, 604], [604, 1208]]
y_ = [[0, 960], [960, 1920]]

cap = []
pathlib.Path('./IMAGE').mkdir(exist_ok=True)
pathlib.Path('./IMAGE/video_merge').mkdir(exist_ok=True)
for i in range(args.num):
    pathlib.Path('./IMAGE/%s' % name[i]).mkdir(exist_ok=True)
    cap.append(cv2.VideoCapture('./%s.h264' % name[i]))

cnt = 0
while(cap[0].isOpened()):
    print('%d' % cnt)
    ret, frame = [], []
    for i in range(args.num):
        a, b = cap[i].read()
        frame.append(b)
        ret.append(a)

    if ret[0] is False:
        break

    merge_image = np.zeros((1208,1920,3))
    for i in range(args.num):
        cv2.imwrite('./IMAGE/%s/%06d.png' % (name[i],cnt), frame[i])
        merge_image[x_[i//2][0]:x_[i//2][1], y_[i%2][0]:y_[i%2][1]] = \
                cv2.resize(frame[i], None, fx=0.5, fy=0.5)
    cv2.imwrite('./IMAGE/video_merge/%06d.png' % cnt, merge_image)
    cnt = cnt +1

for i in range(args.num):
    cap[i].release()

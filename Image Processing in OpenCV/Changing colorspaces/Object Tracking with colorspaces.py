import cv2
import numpy as np

def main():

    # We use trackbar to define range of intensity level in frame
    cv2.namedWindow('trackbars', cv2.WINDOW_NORMAL)

    def nothing(x):
        pass

    cv2.createTrackbar('H1', 'trackbars', 0, 359, nothing)
    cv2.createTrackbar('H2', 'trackbars', 0, 359, nothing)
    cv2.createTrackbar('S1', 'trackbars', 0, 255, nothing)

    cv2.createTrackbar('S2', 'trackbars', 0, 255, nothing)
    cv2.createTrackbar('V1', 'trackbars', 0, 255, nothing)
    cv2.createTrackbar('V2', 'trackbars', 0, 255, nothing)

    cam = cv2.VideoCapture(0)

    while cam.isOpened:
        ret, frame = cam.read()

        if not ret:
            break

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        v1 = cv2.getTrackbarPos('V1', 'trackbars')
        s1 = cv2.getTrackbarPos('S1', 'trackbars')
        h1 = int(cv2.getTrackbarPos('H1', 'trackbars') / 2)

        v2 = cv2.getTrackbarPos('V2', 'trackbars')
        s2 = cv2.getTrackbarPos('S2', 'trackbars')
        h2 = int(cv2.getTrackbarPos('H2', 'trackbars') / 2)

        lower_values = np.array([h1, s1, v1])
        upper_values = np.array([h2, s2, v2])

        mask = cv2.inRange(hsv, lower_values, upper_values)
        result_frame = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow('trackbars', mask)
        cv2.imshow('result frame', result_frame)
        cv2.imshow('original frame', frame)

        if cv2.waitKey(16) == ord('q'):
            break

    cv2.destroyAllWindows()
    cam.release()

if __name__ == '__main__':
    main()
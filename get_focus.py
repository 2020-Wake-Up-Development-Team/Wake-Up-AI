import cv2
from focus import GazeTracking

gaze = GazeTracking()
is_watching={0:"not_focusing",1:"focusing"}
watch = -1
def get_focus_result(frame):
    gaze.refresh(frame)
    if gaze.is_center():
        text = "focusing"
        watch = 1
    else:
        watch = 0
        text = "not looking"
    return watch

import numpy as np



def eye_aspect_ratio(eye):
    
    A = np.linalg.norm(eye[1] - eye[5])
    B = np.linalg.norm(eye[2] - eye[4])

    
    C = np.linalg.norm(eye[0] - eye[3])

    
    ear = (A + B) / (2.0 * C)

    
    return ear



def mouth_aspect_ratio(mouth):
    
    A = np.linalg.norm(mouth[13] - mouth[19])
    B = np.linalg.norm(mouth[14] - mouth[18])
    C = np.linalg.norm(mouth[15] - mouth[17])

    
    D = np.linalg.norm(mouth[12] - mouth[16])

    
    mar = (A + B + C) / (2 * D)

    
    return mar



def direction(nose_point, anchor_point, w, h, multiple=1):
    nx, ny = nose_point
    x, y = anchor_point

    if nx > x + multiple * w:
        return 'right'
    elif nx < x - multiple * w:
        return 'left'

    if ny > y + multiple * h:
        return 'down'
    elif ny < y - multiple * h:
        return 'up'

    return 'none'

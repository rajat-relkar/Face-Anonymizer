import cv2
import mediapipe as mp
import os
import argparse


def process_image(img, face_detection):
    H, W, _ = img.shape

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # face_detection requires img to be in RGB format

    out = face_detection.process(img_rgb)


    # print(out.detections) # use relative_bounding_box

    k_size = 50 # kernel size used for blurring face

    if out.detections is not None: # there exists a face
        for detection in out.detections:
            location_data = detection.location_data
            bbox = location_data.relative_bounding_box 

            # relative_bounding_box gives normalized values(between 0 and 1) of x1, y1, w, h
            # so multiply them with image's height and width to get values in pixels

            x1, y1, w, h = bbox.xmin, bbox.ymin, bbox.width, bbox.height

            # print(x1, y1, w, h)

            x1 = int(x1 * W)
            y1 = int(y1 * H)
            w = int(w * W)
            h = int(h * H)

            # img = cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 5)

            # Blur faces
            img[y1:y1 + h, x1:x1 + w, :] = cv2.blur(img[y1:y1 + h, x1:x1 + w, :], (k_size, k_size))
    
    return img

args = argparse.ArgumentParser()

args.add_argument("--mode", default='webcam')
args.add_argument("--filePath", default=None) #./data/testvideo1.mp4

args = args.parse_args()


output_dir = './data/output'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Detect faces
mp_face_detection = mp.solutions.face_detection

#model_selection - 0 if faces to detect are within 2 meters else 1 for within 5 meters range
with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
    
    if args.mode in ["image"]:
        # Read image
        img_path = './data/myimg.png'

        img = cv2.imread(img_path)

        img = process_image(img, face_detection)

        # save image
        cv2.imwrite(os.path.join(output_dir, 'output.png'), img)


    elif args.mode in ['video']:

        cap = cv2.VideoCapture(args.filePath)
        ret, frame = cap.read()

        output_video = cv2.VideoWriter(os.path.join(output_dir, 'output.mp4'),
                                       cv2.VideoWriter_fourcc(*'mp4v'), 
                                       25, # fps
                                       (frame.shape[1], frame.shape[0])) # window size

        while ret:

            frame = process_image(frame, face_detection)

            output_video.write(frame)

            ret, frame = cap.read()

        cap.release()
        output_video.release()

    elif args.mode in ['webcam']:
        cap = cv2.VideoCapture(0)

        ret, frame = cap.read()
        while ret:
            frame = process_image(frame, face_detection)

            cv2.imshow('frame', frame)
            cv2.waitKey(25)

            ret, frame = cap.read()

        cap.release()


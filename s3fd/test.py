from sfd_detector import SFDDetector as FaceDetector
import cv2

device = 'cpu'
detector = FaceDetector(device, path_to_detector='s3fd.pth')
image = 'p.jpg'
bboxes = detector.detect_from_image(image)

for i, bbox in enumerate(bboxes):
    x1, y1, x2, y2, score = bbox

    # Load the image as a numpy array
    img = cv2.imread(image)

    # Crop the face from the image
    face = img[int(y1):int(y2), int(x1):int(x2)]

    # Write the cropped face image to file
    output_path = f"face_{i}.jpg"
    cv2.imwrite(output_path, face)
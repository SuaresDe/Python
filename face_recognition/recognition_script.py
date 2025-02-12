import cv2
import face_recognition
import os

FACES_FOLDER = r"C:/Users/tikil/Desktop/Python/projects/face_recognition/faces"

# Store known faces and their names
known_face_encodings = []
known_face_names = []

# Load all images in the folder
for file_name in os.listdir(FACES_FOLDER):
    if file_name.endswith(('.jpg', '.jpeg', '.png')):  # Ensure it's an image
        image_path = os.path.join(FACES_FOLDER, file_name)
        image = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(image)
        if len(encodings) > 0:
            known_face_encodings.append(encodings[0])
            known_face_names.append(os.path.splitext(file_name)[0])  # Extract name from filename

print(f"{len(known_face_encodings)} faces loaded from '{FACES_FOLDER}'")

# Start webcam
video_capture = cv2.VideoCapture(0)

# Default window size
FRAME_WIDTH = 800
FRAME_HEIGHT = 600
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

# Create OpenCV window
cv2.namedWindow("Face Recognition", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Face Recognition", FRAME_WIDTH, FRAME_HEIGHT)

while True:
    ret, frame = video_capture.read()
    if not ret:
        print("Error accessing the camera")
        break

    # Check if the window is maximized
    win_state = cv2.getWindowProperty('Face Recognition', cv2.WND_PROP_FULLSCREEN)
    if win_state == 1:  # If maximized, get screen resolution
        screen_width = 1920  # Adjust to your screen resolution if necessary
        screen_height = 1080
        cv2.resizeWindow("Face Recognition", screen_width, screen_height)

    # Convert frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect faces
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Compare detected faces with known ones
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.5)
        name = "Unknown"
        distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        if len(distances) > 0:
            best_match_index = distances.argmin()
            if matches[best_match_index]: 
                name = known_face_names[best_match_index]

        # Draw rectangle around face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 255), 2)

        # Add name label
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.8
        thickness = 2
        text_size, _ = cv2.getTextSize(name, font, font_scale, thickness)
        text_width, text_height = text_size
        text_x = left + (right - left - text_width) // 2
        text_y = top - 10
        text_y = max(text_y, text_height + 5)
        cv2.putText(frame, name, (text_x, text_y), font, font_scale, (0, 255, 255), thickness)

    # Show the frame
    cv2.imshow('Face Recognition', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # Press ESC to exit
        break
    if cv2.getWindowProperty('Face Recognition', cv2.WND_PROP_VISIBLE) < 1:  
        break

# Release webcam and close windows
video_capture.release()
cv2.destroyAllWindows()
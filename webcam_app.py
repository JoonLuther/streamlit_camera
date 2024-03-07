import streamlit as st
import cv2

def main():
    st.title("Webcam Feed")

    # Open webcam
    cap = cv2.VideoCapture(cv2.CAP_DSHOW)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        st.error("Error: Unable to open webcam.")
        return

    # Set the width and height of the webcam feed
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # Create a placeholder for the webcam feed
    video_placeholder = st.empty()

    # Continuously read and display frames from the webcam
    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("Error: Unable to read frame.")
            break

        # Display frame in Streamlit
        video_placeholder.image(frame, channels="BGR")

    # Release the webcam and close the OpenCV window
    cap.release()

if __name__ == "__main__":
    main()

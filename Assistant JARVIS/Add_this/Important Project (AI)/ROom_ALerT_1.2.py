import cv2
import numpy as np
import smtplib
from playsound import playsound
import time
import os
import logging

# Configure logging
logging.basicConfig(filename='motion_detection.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Configuration Variables
CAMERA_URL = "http://192.168.79.51:4747/video"  # Replace with your camera stream URL
MIN_CONTOUR_AREA = 500
EMAIL_RECIPIENT = "sarvendrasingh2020@gmail.com"  # Change to your recipient email
EMAIL_SUBJECT = "Motion Detected!"
EMAIL_BODY = "Alert: Motion detected in your room!"
RECORD_VIDEO = True
VIDEO_OUTPUT = "output.avi"
COOLDOWN_TIME = 30  # seconds

# Global variables
running = True
alert_triggered = False
alert_sent_time = time.time()  # Initialize this here
video_writer = None
fourcc = cv2.VideoWriter_fourcc(*'XVID')
roi = (100, 100, 400, 400)  # Region of Interest


        
# Email alert function
def send_email_alert():
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(os.getenv('zalimsk2023@gmail.com'), os.getenv('Zalimsk@1919'))
        message = f"Subject: {EMAIL_SUBJECT}\n\n{EMAIL_BODY}"
        server.sendmail(os.getenv('zalimsk2023@gmail.com'), EMAIL_RECIPIENT, message)
        server.quit()
        logging.info("Email alert sent.")
        print("Email alert sent.")
    except Exception as e:
        logging.error(f"Email sending failed: {e}")
        print(f"Email sending failed: {e}")

# Main function for motion detection
def run_motion_detection():
    global alert_triggered, alert_sent_time, video_writer
    cap = cv2.VideoCapture(CAMERA_URL)

    if not cap.isOpened():
        logging.error("Error: Unable to open video stream")
        print("Error: Unable to open video stream")
        return

    backSub = cv2.createBackgroundSubtractorMOG2()

    while running:
        try:
            ret, frame = cap.read()
            if not ret:
                logging.error("Failed to capture video")
                print("Failed to capture video")
                break
            
            # Apply ROI
            roi_frame = frame[roi[1]:roi[3], roi[0]:roi[2]]
            fgMask = backSub.apply(roi_frame)
            contours, _ = cv2.findContours(fgMask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            motion_detected = False
            for contour in contours:
                if cv2.contourArea(contour) < MIN_CONTOUR_AREA:
                    continue
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (roi[0] + x, roi[1] + y), (roi[0] + x + w, roi[1] + y + h), (0, 255, 0), 2)
                motion_detected = True

            if motion_detected:
                if not alert_triggered and time.time() - alert_sent_time > COOLDOWN_TIME:
                    print("Motion detected! Sending alert...")
                    path = "J:\\Assistant JARVIS\\Add_this\\Important Project (AI)\\alert.mp3"
                    playsound(path)  # Ensure alarm.mp3 is in the same directory
                    send_email_alert()
                    logging.info('Motion detected and alert sent.')
                    alert_triggered = True
                    alert_sent_time = time.time()  # Reset the timer

                if video_writer is None and RECORD_VIDEO:
                    video_writer = cv2.VideoWriter(VIDEO_OUTPUT, fourcc, 20.0, (frame.shape[1], frame.shape[0]))
                if video_writer:
                    video_writer.write(frame)
            else:
                alert_triggered = False
                if video_writer is not None:
                    video_writer.release()
                    video_writer = None

            cv2.imshow("Motion Detection", frame)

            if cv2.waitKey(10) == ord('q'):
                break

        except Exception as e:
            logging.error(f"An error occurred: {e}")
            print(f"An error occurred: {e}")
            break

    # Cleanup
    cap.release()
    if video_writer is not None:
        video_writer.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    try:
        run_motion_detection()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        print(f"An error occurred: {e}")

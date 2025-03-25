import cv2
import numpy as np
import smtplib
from playsound import playsound
import time
import os
import logging

# Configure logging
logging.basicConfig(filename='motion_detection.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Email alert function
def send_email_alert():
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(os.getenv('zalimsk2023@gmail.com'), os.getenv('Zalimsk@1919'))  # Use environment variables for security
        message = "Alert: Aapke room mein motion detect hua hai!"
        server.sendmail(os.getenv('zalimsk2023@gmail.com'), 'sarvendrasingh2020@gmail.com', message)
        server.quit()
        logging.info("Email alert sent.")
    except Exception as e:
        logging.error(f"Email sending failed: {e}")

def run_motion_detection():
    # Initialize webcam
    cap = cv2.VideoCapture('http://192.168.79.51:4747/video')  # Replace with your mobile camera stream URL
    if not cap.isOpened():
        logging.error("Error: Unable to open video stream")
        return

    backSub = cv2.createBackgroundSubtractorMOG2()
    alert_triggered = False
    alert_sent_time = time.time()
    video_writer = None
    output_file = 'output.avi'
    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    while True:
        ret, frame = cap.read()
        if not ret:
            logging.error("Failed to capture video")
            break

        fgMask = backSub.apply(frame)
        contours, _ = cv2.findContours(fgMask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        motion_detected = False

        for contour in contours:
            if cv2.contourArea(contour) < 500:  # Adjust this threshold as needed
                continue
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            motion_detected = True

        if motion_detected:
            if not alert_triggered and time.time() - alert_sent_time > 30:  # 30 seconds cooldown
                print("Motion detected! Sending alert...")
                playsound('Add_this\\Important Project (AI)\\security_alarm.mp3')  # Ensure alert.mp3 is in the same directory
                send_email_alert()
                logging.info('Motion detected and alert sent.')
                alert_triggered = True
                alert_sent_time = time.time()

            if video_writer is None:
                video_writer = cv2.VideoWriter(output_file, fourcc, 20.0, (frame.shape[1], frame.shape[0]))
            video_writer.write(frame)
        else:
            alert_triggered = False
            if video_writer is not None:
                video_writer.release()
                video_writer = None

        cv2.imshow("Motion Detection", frame)

        if cv2.waitKey(10) == ord('q'):
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

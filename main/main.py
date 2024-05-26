import os
import schedule
from data.generate_simulated_data import generate_simulated_data
from utils.write_csv import write_csv
from utils.send_email_immediate import send_email
from config import config

# Configuration
CSV_FILE_PATH = config.CSV_FILE_PATH
EMAIL_HOST = config.EMAIL_HOST
EMAIL_PORT = config.EMAIL_PORT
EMAIL_USER = config.EMAIL_USER
EMAIL_PASS = config.EMAIL_PASS
DEANS_EMAILS = config.DEAN_EMAILS


def main():
    # -------------------------------------------------------------#
    # Generated random student data

    # num_students = 10
    # report_data = generate_simulated_data(num_students)
    # -------------------------------------------------------------#

    report_data = generate_simulated_data()
    write_csv(report_data, CSV_FILE_PATH)
    print("report created successfully!")

    # -------------------------------------------------------------#
    # make email sending scheduled
    # schedule.every().day.at("08:00").do()

    # -------------------------------------------------------------#

    send_email(
        subject='Student Last Activity Report',
        body='Please find the attached report below:',
        to=DEANS_EMAILS,
        file_path=CSV_FILE_PATH,
        email_user=EMAIL_USER,
        email_pass=EMAIL_PASS,
        email_host=EMAIL_HOST,
        email_port=EMAIL_PORT
    )
    print("Email sent successfully!")


if __name__ == "__main__":
    main()

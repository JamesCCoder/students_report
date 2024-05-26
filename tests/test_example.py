import unittest
from unittest.mock import patch
from main import main

class TestMain(unittest.TestCase):
    @patch('main.generate_simulated_data')
    @patch('main.write_csv')
    @patch('main.send_email')
    def test_main(self, mock_send_email, mock_write_csv, mock_generate_simulated_data):
        mock_generate_simulated_data.return_value = [
            ['a', 'b', 'a.b@test.com', 'aaa', '2024-05-20T14:30:00Z']
        ]
        main()
        mock_write_csv.assert_called_once_with(
            [['a', 'b', 'a.b@test.com', 'aaa', '2024-05-20T14:30:00Z']],
            'student_last_activity_report.csv'
        )
        # mock_send_email.assert_called_once_with(
        #     'Student Last Activity Report',
        #     'Please find the attached report.',
        #     ['dean1@example.com', 'dean2@example.com'],
        #     'student_last_activity_report.csv',
        #     'your_email@example.com',
        #     'your_email_password',
        #     'smtp.your_email_host.com',
        #     587
        # )

if __name__ == '__main__':
    unittest.main()

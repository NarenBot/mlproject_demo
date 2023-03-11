import sys
import logging

# from src.logger import logging


def error_message_detail(error_info, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_no = exc_tb.tb_lineno
    error_message = f"Error occured in script name [{file_name}] in line number [{line_no}] with message [{error_info}]"

    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message


# if __name__ == "__main__":
#     try:
#         val = 1 / 0
#         print(val)
#     except Exception as e:
#         logging.info("Divide by Zero Error.")
#         raise CustomException(e, sys)

import traceback

def log_exception():
    try:
        raise Exception("Custom exception")
    except Exception as e:
        with open("error_log.txt", "a") as log_file:
            log_file.write("Exception occurred:\n")
            traceback.print_exc(file=log_file)

log_exception()

from log_setup import logger

# log!
def send_response(msg):
    print(msg)

def somefunction():
    try:
        1/0
    except ZeroDivisionError as e:
        send_response('You cant divide 1 by 0')
        logger.exception(e)

somefunction()

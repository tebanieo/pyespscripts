import sys
import logging
import traceback
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    '''Demostration on how to simply but effectively print log messages.'''
    try:
        logger.info(f'event: {event}')
        contact_id = event['Details']['ContactData']['ContactId']
        logger.info(f'We have a new call with ContactId : {contact_id}')
        return {"status": "success", "response": {'contact_id': contact_id}

    except Exception as exp:
        exception_type, exception_value, exception_traceback = sys.exc_info()
        traceback_string = traceback.format_exception(exception_type, exception_value, exception_traceback)
        error_msg = json.dumps({
            "errorType": exception_type.__name__,
            "errorMessage": str(exception_value),
            "stackTrace": traceback_string
        })
        logger.error(error_msg)

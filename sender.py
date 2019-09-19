import greengrasssdk
import logging
import greengrasssdk
import platform
from threading import Timer

client = greengrasssdk.client('iot-data')

my_platform = platform.platform()

OUTPUT_TOPIC = 'test/topic_results'

def greengrass_hello_world_run():
    if not my_platform:
        client.publish(
            topic=OUTPUT_TOPIC,
            payload='Hello world! Sent from Greengrass Core.')
    else:
        client.publish(
            topic=OUTPUT_TOPIC,
            payload='Hello world! Sent from '
                    'Greengrass Core running on platform: {}'
                    .format(my_platform))

    # Asynchronously schedule this function to be run again in 5 seconds
    Timer(5, greengrass_hello_world_run).start()


# Start executing the function above
greengrass_hello_world_run()

def function_handler(event, context):
    return
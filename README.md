# sample code for sending message to another lambda function in the same gg

- sender.py 
it is the sender sample code, which create a timer to send message out.

- recv.py
it is the receiver sample code, and will be triggered by receiving message, this rule is defined by subscription.

In this sample code, sender will send message to receiver via topic "test/topic_results", which is set up in greengrass group.
For sender, this is a timer function, so you need to set Lambda lifecycle to "Make this function long-lived and keep it running indefinitely". Besides, the message format is not json format in this example, thus you need to configure Input payload data type to Binay in recv lambda setting.

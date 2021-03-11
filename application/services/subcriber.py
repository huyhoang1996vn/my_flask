import time

def callback(ch, method, properties, body):
    print(" [x] Received %s" % body)

    cmd = body.decode()

    if cmd == 'hey':
        print("hey there")
    elif cmd == 'hello':
        print("well hello there")
    else:
        print("sorry i did not understand ", body)
    

    if body == 'delay':
        time.sleep(20)
    print(" [x] Done ", body)

    ch.basic_ack(delivery_tag=method.delivery_tag)

def callback2(ch, method, properties, body):
    print(" [x] Received %s" % body)
    try:

        cmd = body.decode()

        if cmd == 'hey':
            print("hey there")
        elif cmd == 'hello':
            print("well hello there")
        else:
            print("sorry i did not understand ", body)
        

        # if body == 'delay':
        #     time.sleep(20)
        print(" [x] Done ", body1)

        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        print(" [x] Done in error ", e)
        ch.basic_ack(delivery_tag=method.delivery_tag)

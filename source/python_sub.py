#!/usr/bin/env python
"""Simple example of publish/subscribe illustrating topics.

Publisher and subscriber can be started in any order, though if publisher
starts first, any messages sent before subscriber starts are lost.  More than
one subscriber can listen, and they can listen to  different topics.

Topic filtering is done simply on the start of the string, e.g. listening to
's' will catch 'sports...' and 'stocks'  while listening to 'w' is enough to
catch 'weather'.
"""

# -----------------------------------------------------------------------------
#  Copyright (c) 2010 Brian Granger, Fernando Perez
#
#  Distributed under the terms of the New BSD License.  The full license is in
#  the file LICENSE.BSD, distributed as part of this software.
# -----------------------------------------------------------------------------

import zmq

import cv2
import numpy as np
import base64 # Convert string to image

def main() -> None:
     
    # Sending to 127.0.0.1 port 5555
    connect_to = "tcp://127.0.0.1:5555"

    # Topic handler
    topics = ["msg", "img"]

    ctx = zmq.Context()
    s = ctx.socket(zmq.SUB)
    s.connect(connect_to)

    # manage subscriptions
    if not topics:
        print("Receiving messages on ALL topics...")
        s.setsockopt(zmq.SUBSCRIBE, b'')
    else:
        print("Receiving messages on topics: %s ..." % topics)
        for t in topics:
            s.setsockopt(zmq.SUBSCRIBE, t.encode('utf-8'))
    print
    try:
        while True:
            topic, msg = s.recv_multipart()

            """
            print(msg)

            print(
                '   Topic: {}, msg:{}'.format(
                    topic.decode('utf-8'), msg.decode('utf-8')
                )
            )
            """

            if(topic.decode('utf-8') == "msg"): # When receiving the topic "msg"
                print(msg.decode('utf-8'))
            
            if(topic.decode('utf-8') == "img"): # When receiving the topic "img"
            
                # Save string Base64
                base64_string = msg.decode('utf-8')

                # Convert Base64 string to byte array
                image_data = base64.b64decode(base64_string)

                # Read the byte array as an image
                image = cv2.imdecode(np.frombuffer(image_data, np.uint8), cv2.IMREAD_COLOR)

                # Show images in pop-up
                cv2.imshow('Gambar', image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

    except KeyboardInterrupt:
        pass
    print("Done.")


if __name__ == "__main__":
    main()

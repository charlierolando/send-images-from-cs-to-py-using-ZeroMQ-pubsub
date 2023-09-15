# send-images-from-cs-to-py-using-ZeroMQ-pubsub

>Code to send images (pictures) and messages from c# to py using ZeroMQ pubsub

![Result](https://github.com/charlierolando/send-images-from-cs-to-py-using-ZeroMQ-pubsub/blob/main/images/images1.png)

>Click [this](https://github.com/charlierolando/send-images-from-cs-to-py-using-ZeroMQ-pubsub/blob/main/images/images1.png) when the image doesn't appear

## [Code:](#code)

>Click [this](https://github.com/charlierolando/send-images-from-cs-to-py-using-ZeroMQ-pubsub/blob/main/source/) to see the full code

## [How to use:](#how-to-use)

- Install dotnet. Click [this](https://dotnet.microsoft.com/en-us/download)

- To run the c# code, move to c# dir code and install NetMQ

```bash
dotnet add package NetMQ
```

- To run the py code, install zmq

```bash
pip install zmq
```

- Run [this](https://github.com/charlierolando/send-images-from-cs-to-py-using-ZeroMQ-pubsub/blob/main/source/python_sub.py) py code

- Run [this](https://github.com/charlierolando/send-images-from-cs-to-py-using-ZeroMQ-pubsub/blob/main/source/c_sharp_pub) c# code

## [References:](#references)

[netmq/pubsub](https://github.com/zeromq/netmq/blob/master/docs/pub-sub.md)

[pyzmq/pubsub](https://github.com/zeromq/pyzmq/blob/main/examples/pubsub/topics_sub.py)

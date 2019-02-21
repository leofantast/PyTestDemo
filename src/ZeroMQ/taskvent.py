import zmq
import time
import random

try:
    raw_input
except NameError:
    raw_input = input

context = zmq.Context()
sender = context.socket(zmq.PUSH)
sender.bind("tcp://*:5557")
sink = context.socket(zmq.PUSH)
sink.connect("tcp://localhost:5558")

print("Please enter when workers are ready: ")
_ = raw_input()
print("Sending tasks to workers...")
sink.send(b'0')
random.seed()
total_msec = 0

for task_nbr in range(100):
    workload = random.randint(1, 100)
    total_msec += workload
    sender.send_string(u'%i' % workload)
    print(u'%i' % workload)

print("Total expected cost: %s msec" % total_msec)
time.sleep(1)
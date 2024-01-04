import os 
import socket
import sys
import time
import subprocess
from threading import Thread

dirs = "/home/ap3x/test69/"

def fetch(addr, output_dir=dirs):
    
    print("Current Directory:", os.getcwd())  # Print current working directory
    command = ['wget', addr, '-P', output_dir]
    subprocess.run(command)
    print("File should be saved in:", os.path.abspath(output_dir))  # Print the absolute path of the output directory


sub_dirs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y', 'z']
    
    
for a in sub_dirs:
    for b in sub_dirs:
        for c in sub_dirs:
    
            addr = f"https://inst.eecs.berkeley.edu/~cs194-26/fa17/upload/files/proj6B/cs194-26-{a}{b}{c}/main.py"

            fetch(addr, output_dir=dirs)



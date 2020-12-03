import os,sys,time






pid,fd = os.forkpty()
if pid == 0:
    os.execv("/bin/bash", ["bash"])
    sys.exit(0)
# else:
#     # # output = os.read(fd,1024)
#     # # print(output)
#     # os.write(fd,'ls\n'.encode())
#     # time.sleep(1) # this is new!
#     # output = os.read(fd,1024)
#     # print(output.decode())
#     pass


os.write(fd,'ls\n'.encode())
# os.write(fd,'ping 8.8.8.8\n'.encode())
# time.sleep(4) # this is new!
os.write(fd,'export TERM=xterm\n'.encode())
os.write(fd,'htop\n'.encode())
time.sleep(2) # this is new!
os.write(fd,'\x03\n'.encode())
output = os.read(fd,2048)
print(output.decode())
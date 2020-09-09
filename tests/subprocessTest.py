# import subprocess
#
#
#
# a = subprocess.Popen(["ls"], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
#
# a.stdin.write("echo \"two\"\n".encode())
#
# a.stdin.flush()
#
# output = a.stdout.read()
#
# print(output)
import signal
import subprocess
from time import sleep

# process1 = subprocess.Popen("/bin/bash", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
process1 = subprocess.Popen("/bin/bash", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
process2 = subprocess.Popen("/bin/bash", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, )


# process1.stdin.write("whoami\n")
# process1.stdin.write("su\nmind\n")
# process1.stdin.write("whoami\n")


process1.stdin.write("ping 8.8.8.8\n")
process1.stdin.flush()
#
sleep(1)
process1.send_signal(2)
output = process1.stdout.readline()
output += process1.stdout.readline()
process1.stdout.flush()
while process1.stdout.readable():
    output = process1.stdout.readline()
    process1.send_signal(signal.SIGINT)
    print(output)
process1.stdin.write("whoami\n")
output = process1.stdout.readline()

# process1.stdout.close()




# process1.send_signal(signal.SIGINT)
# print(process1.pid)
#
# stdout, stderr = process1.communicate()
# print(stdout)



# process2.stdin.write("whoami\n")



# stdout, stderr = process2.communicate()
# print(stdout)

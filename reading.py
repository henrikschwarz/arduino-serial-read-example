import serial
import subprocess
import time


def clean_string(string):
    decoded = str(ser_bytes, "utf-8").strip().replace('\n', '').replace('\b','').encode('utf8').decode('utf8')
    
    return decoded

def call_program(program):
    raw_path = r'{}'.format(program)
    try:
        process_code = subprocess.Popen(raw_path, shell=False,
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return process_code
    except e:
        print("Exception:", e)


ser = serial.Serial('/dev/ttyACM0')
program_dict = {}
program_dict["A"] = "/usr/bin/arduino"
program_dict["F"] = "/usr/bin/firefox"

decoded = ""
exit_string = "EE"
while(decoded != exit_string):
    ser_bytes = ser.readline() # read serial
    decoded = clean_string(ser_bytes) # clean string

    # check for exit string and it is a valid command
    if (decoded != exit_string and decoded in program_dict):  
        call_program(program_dict[decoded])
        print("Recieved:", decoded)
    else:
        print("Exit string recieved")

print("Program over")

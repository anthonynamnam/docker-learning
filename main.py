import time

if __name__ == '__main__':
    count = 0
    while count < 60:
        time.sleep(1)
        count = count + 1
        print(count)
        
    print("end now")
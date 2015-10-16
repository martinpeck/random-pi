import time

def blast_off():
    count = 10
    while count > 0:
        print (count)
        time.sleep(1)
        count=count-1
    print("BLAST OFF!")
        
blast_off()

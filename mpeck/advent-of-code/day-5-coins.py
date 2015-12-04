import md5
import sys

secret_key = "bgvyzdsv"
count = 1
found = False
while not found:
    attempt = secret_key + str(count)
    result = md5.new(attempt).hexdigest()
    if result[:6] == "000000":
        found = True
    else:
        #sys.stdout.write('.')
        count += 1

print "attempt: ", attempt
print "result:  ", result
print "count:   ", count

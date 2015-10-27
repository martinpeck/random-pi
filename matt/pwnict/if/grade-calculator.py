def grader(score):

    if score >= 81:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 69:
        return "C"
    elif score >= 63:
        return "D"
    elif score >= 58:
        return "E"
    else:
        return "U"

s = int(input("what score did you get? "))

response = grader(s)
print "Your grade:", response

# tests
grade= grader(81)
if grade == "A":
    print "TEST PASS"
else:
    print "TEST FAIL"

grade= grader(100)
if grade == "A":
    print "TEST PASS"
else:
    print "TEST FAIL"

grade= grader(75)
if grade == "B":
    print "TEST PASS"
else:
    print "TEST FAIL"

grade= grader(80)
if grade == "B":
    print "TEST PASS"
else:
    print "TEST FAIL"

total_area = 0
total_ribbon = 0
count = 0
with open("day-2-presents-for-wrapping.txt", "r") as f:
    for line in f:
        count += 1
        parts = line.split('x')
        l = int(parts[0])
        w = int(parts[1])
        h = int(parts[2])

        dimensions = [l,w,h]
        dimensions.sort()
        
        side1 = dimensions[0] * dimensions[1]
        side1_perim = 2 * (dimensions[0] + dimensions[1])
        side2 = dimensions[1] * dimensions[2]
        side3 = dimensions[2] * dimensions[0]
        extra = side1
        volume = dimensions[0] * dimensions[1] * dimensions[2]
        
        area_of_box =  (2 * side1) + (2 * side2) + (2 * side3) + extra
        ribbon = side1_perim + volume
    
        total_area += area_of_box
        total_ribbon += ribbon


print "total area", total_area
print "total ribbon", total_ribbon

import math
t1 = math.radians(float(input("Enter the latidude of first point")))
t2 = math.radians(float(input("Enter the longitude of first point")))
g1 = math.radians(float(input("Enter the latidude of second point")))
g2 = math.radians(float(input("Enter the longitude of second point")))
dist = 6371.01 *acos (math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1 − g2))
print("The distance between two coordtinates is %.3f"%dist)



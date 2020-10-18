import stdio
import stddraw
import stdarray


male_heights = []
value = stdio.readString()
while not stdio.isEmpty():
	value = stdio.readString()
	new_value = value.split(',')
	stdio.writeln(new_value)
	male_heights.append(float(new_value[1]))

stdio.writeln(male_heights)

stdio.writeln(min(male_heights))
stdio.writeln(max(male_heights))

if value[0] == '"male"': 
    male_hights.append(float(value[1]))
    male_weights.append(float(value[2]))
    for i in range(58, 80):
    	if i <=float(value[1]) < i + 1:
		    sdtio.writeln()
bars = male_heights
n = len(male_heights)
a = stdarray.create1D(n, n+1)
stddraw.setXscale(54, 80)
stddraw.setYscale(0, 100)
stddraw.setPenRadius(0.010)
for i in range(n):
    stddraw.filledRectangle(54, a[i], 80, a[i])
    
stddraw.show()
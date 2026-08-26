current_population =10000
rate=0.1
prev_population=None

for i in range(10):
    prev_population=current_population/(rate+1)
    current_population =prev_population
    print("population of last ",i+1," year is ",int(prev_population))
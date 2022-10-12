import timeit

#Constant time

def take_first(my_list):
    return my_list[0]

short_list = [13,25,42]
tic = timeit.timeit()
first = take_first(short_list)
toc = timeit.timeit()

print(toc - tic)
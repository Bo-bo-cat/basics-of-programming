def sum(a, b=0):
    return a + b

def calc_lists(a, b, op_fn):
    res = []
    li = min(len(a), len(b))
    for i in range(li):
        res.append(op_fn(a[i], b[i]))
    return res
print(calc_lists([1], [2], sum))
#зробити в циклі для кожного нульового елементу та для кожного наступного 



#def function_name( other_fn
    #  return other_fn("Hello")
#function_name(print)/(input)



#def add(x)
    #def add_fn(y):
        #return x+y
    #return add_fn

#add_two = add(2)
#add_two(3)

#def create_counter(42) , inc dec - create_counter(42) , print(inc()) , print(dec()) 

def create_counter(init = 0):
    count = init
    def inc():
        nonlocal count
        count += 1
        return count
    def dec():
        nonlocal count
        count -= 1
        return count
    return inc, dec  
inc, dec = create_counter(42)
print(inc())            
print(dec()) 
print(dec())




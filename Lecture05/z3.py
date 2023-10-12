dises = input('MdN: ').split(' ')
count_value = []
m = 0
n = 0
for dise in dises:
    parts = dise.split('d')
    if len(parts) == 2:
       M, N = parts
       try:
           (M := 1) if M == "" else (M := int(M))
           N = int(N)
           m+=M
           n+=N*M
           count_value.append(CountProp(M, N)[0])
       except ValueError:
            print(-1)
value = list(map(sum, tensor_product(count_value)))
for _ in range(1*m, n+1):
    print(f"{_}: {round(value.count(_)/len(value)*100, 3)} %")

def tensor_product(lists):
    if len(lists) == 1:
        return [(x,) for x in lists[0]]
    else:
        head, *tail = lists
        sub_result = tensor_product(tail)
        return  [(x,) + y for x in head for y in sub_result]

def CountProp (M, N):
    res = [sum(item) for item in tensor_product([range(1,N+1)] * M)]
    return res, [res.count(S)/len(res) for S in range(1*M, N*M+1)]
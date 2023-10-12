# Ввод дайсов
parts = input('MdN: ').split('d')
if len(parts) == 2:
   M, N = parts
   try:
      (M := 1) if M == "" else (M := int(M))
      N = int(N)
   except ValueError:
          print("Что-то плохое вывели")
# Придумал тензорное умнажение, чтобы построить таблицу вероятностей
def tensor_product(lists):
    if len(lists) == 1:
        return [(x,) for x in lists[0]]
    else:
        head, *tail = lists
        sub_result = tensor_product(tail)
        return  [(x,) + y for x in head for y in sub_result]
#Выщитывает вероятности и колличество исходов выподения числа Ы
def CountProp (M, N):
    res = list(map(sum,tensor_product([range(1,N+1)] * M)))
    return [res.count(S) for S in range(1*M, N*M+1)], [res.count(S)/len(res) for S in range(1*M, N*M+1)]

prop = CountProp(M, N)[1]
for _ in range(N*M+1-1*M):
    print(f"{_ + M}: {round( prop[_]*100, 3)} %")
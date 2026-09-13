divida = int(input())
maximo = int(input())
while divida != 0:
  print(f"(antes) {divida}")
  if divida > maximo:
    divida = divida - maximo
    print(f"(depois) {divida}")
  else:
    divida = 0
    print(f"(depois) {divida}")

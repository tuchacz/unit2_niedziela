"""Udowodnij, że w zbiorze liczb z zakresu 1-100, jest 11 liczb, które są
parzyste i jednocześnie większe od 90, a gdy są nieparzyste, to
przynajmniej dzielą się przez 9."""

a = 1
b = 100

for i in range(a, b+1):
    if i % 2 == 0 and i > 90:
        print(i)
    elif i % 2 == 1 and i % 9 == 0:
        print(i)

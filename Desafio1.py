from tkinter import W


print("Programa: Números reversos menores que 1 milhão ( 1.000.000 ) ")
enter = input(" --> Precione qualquer tecla para iniciar o programa <-- ")

print("Os números quando somados resultão em impar são: ")

result = 0
i = 0

while result < 1000000:

    i += 1

    if i >= 10:

        n = i

        nS = str(n)
        reverse = nS[::-1]
        reverse = int(reverse)

        result = n + reverse

        if result % 2 != 0:

            print(n)

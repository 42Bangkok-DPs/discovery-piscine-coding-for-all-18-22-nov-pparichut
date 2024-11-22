import sys

if len(sys.argv) > 1:
    print("none")
    sys.exit(0)

for i in range(11):
    print(f"Table de {i}: ", end="")
    print(" ".join(str(i * j) for j in range(11)))

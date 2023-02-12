def Matrix(M):
# Switching zero keys to "*":
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == 0:
                M[i][j] = "*"

# Setting zeros in horizontal numbers:
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == "*":
                for zero in range(len(M[0])):
                    if M[i][zero] == "*":
                        pass
                    else:
                        M[i][zero] = 0
                    M[i][j] = "*"

# Setting zeros in vertical numbers:
    for j in range(len(M[0])):
        for i in range(len(M)):
            if M[i][j] == "*":
                for zero in range(len(M)):
                    if M[zero][j] == "*":
                        pass
                    else:
                        M[zero][j] = 0
                    M[i][j] = "*"

# Switching our "*" back to zeros:
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == "*":
                M[i][j] = 0

numOfRows = int(input(""))
M = [[int(item) for item in input().split(" ")] for i in range(numOfRows)]
Matrix(M)
print(M)

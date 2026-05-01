def Tabela(Rows, Columns):
    Result = []
    Total = Columns * Rows
    Per_Row = int(Total / Rows)

    Current = 0

    for I in range(Rows):
        key = []
        for i in range(Per_Row):
            Current += 1
            key.append(Current)
        Result.append(key)
    print(Result)


Tabela(3,4)
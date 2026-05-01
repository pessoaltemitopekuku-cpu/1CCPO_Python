def function (Nomes):
    Result = []
    for I,V in enumerate(Nomes):
        for i,v in enumerate(Nomes):
            if i <= I:
                continue
            Result.append([V, v])

    print(Result)
    return Result

function(["Temitope","Igor", "Carlos"])
from getpass import fallback_getpass


def checkAPI(Status):
    Results = []

    def checkStatus(Value):
        if Value > 200 and Value < 299:
            return True
        else:
            return False

    def checkSequence(Table):
        Result = []
        for Index, Value in enumerate(Table):
            Current = 1
            Sequence = 0
            Normalized = Index + Current
            if Normalized >= len(Table):
                Normalized = len(Table) - 1
            while Table[Normalized] == Value:
                Sequence += 1
                Result.append([Current + 1, Sequence])
        return Result


    def checkRequisition(Session):
        Result = []
        for I in Session:
            Boolean = checkStatus(I);

checkAPI(
    [
        [200, 200, 401, 200, 500],
        [200, 200, 200, 200,200],
        [201 , 500, 502, 201, 500],
    ]
)


def checkSequence(table):
    result = []
    for index, value in enumerate(table):
        current = 1
        sequence = 1
        flag = True
        sequenced = False
        while flag:
            normalized = index + current
            if normalized >= len(table):
                break
            if table[normalized] == value:
                current += 1
                sequence += 1
                if normalized-1 <= 0:
                    sequenced = False
                if table[max(0, normalized-1)] == value:
                    sequenced = True
            else:
                flag = False
        if sequence == 1:
            continue
        print(sequenced)
        if not sequenced:
            result.append([current, sequence])
    print(result)

checkSequence([200, 200, 200, 200,200])

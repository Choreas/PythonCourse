def CheckSolution(fields):
    try:
        fields = _ValidateSolution(fields)
    except Exception as e:
        return e.args[0]

    cols = [[] for n in range(9)] 
    row = []
    grids = [[] for n in range(9)]

    for idx, val in enumerate(fields):
        rownum = ((idx // 9))
        colnum = ((idx % 9))
        gridnum = (((idx % 9) // 3) + (((idx // 9) // 3) * 3))
        if row.count(val) > 0:
            return _Wrong(rownum, colnum, gridnum, val, "Row")       
        if cols[colnum].count(val) > 0:
            return _Wrong(rownum, colnum, gridnum, val, "Column")
        if grids[gridnum].count(val) > 0:
            return _Wrong(rownum, colnum, gridnum, val, "Grid")
        row.append(val)
        cols[colnum].append(val)
        grids[gridnum].append(val)
        if idx % 9 == 8:
            row.clear()
    return True

def _Wrong(row, col, grid, val, source):
    return ("(First) incorrect value.\nRow: " + str(row + 1) + "\nCol: " + 
            str(col + 1) + "\nGrid: " + str(grid + 1) + "\nValue: " + str(val) +
            "\nSource: " + source)

def _ValidateSolution(fields):
    try:
        fields = str(fields)
    except:
        raise Exception("Error: Could not parse solution to string.")
    fields = fields.replace(" ", "", -1)
    if not fields.isdigit():
        raise Exception("Error: Solution can only contain integers.")
    if not len(fields) == 81:
        raise Exception("Error: Not all fields are solved.")
    if fields.count("0") > 0:
        raise Exception("Error: Solution can only consist of digits from 1 to 9.")
    return fields
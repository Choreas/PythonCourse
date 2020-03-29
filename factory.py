import csv as _csv_, json as _json_

class csvfactory:
    """Factory for csv operations"""
    def __init__(self, filename):
        self.dir = "data\\"
        if not filename.endswith(".csv"):
            self.file = filename + ".csv"
        else:
            self.file = filename
        try:
            file = open(self.dir + self.file, 'r')
            file.close()
        except:
            raise Exception("Could not open file. Does it exist in data/ ?")
        
    def Readcsv(self):
        csvlist = {"keys":[], "values":[]}
        with open(self.dir + self.file, 'r') as csvfile:
            csvreader = _csv_.reader(csvfile, delimiter=',', quotechar='"')
            for idx, row in enumerate(csvreader):
                if idx == 0:
                    for item in row:
                        csvlist.get("keys").append(item.replace(".", "0", -1))
                    continue
                csvlist.get("values").append([])
                for item in row:
                    csvlist.get("values")[idx - 1].append(item.replace(".", "0", -1))
        return csvlist

    def WriteJson(self, filename):
        filename = filename.replace(" ", "", -1)
        csvlist = self.Readcsv()
        keys = csvlist.get("keys")
        values = csvlist.get("values")
        pairs = {"data":{vidx:{key:value[kidx] for kidx, key in enumerate(keys)} for vidx, value in enumerate(values)}}
        with open(self.dir + filename + ".json", 'w') as jsonfile:
            _json_.dump(pairs, jsonfile)

class jsonfactory:
    """Factory for json operations"""
    def __init__(self, filename):
        self.dir = "data\\"
        if not filename.endswith(".json"):
            self.file = filename + ".json"
        else:
            self.file = filename
        try:
            file = open(self.dir + self.file, 'r')
            file.close()
        except:
            raise Exception("Could not open file. Does it exist in data/ ?")

    def GetJson(self):
        jsonobj = ""
        with open(self.dir + self.file, 'r') as jsonfile:
            jsonobj = _json_.load(jsonfile)
        return jsonobj

class sudokuTemplate(jsonfactory):
    """Load sudoku templates from memory"""
    def __init__(self, filename):
        super().__init__(filename)
        self.jsonobj = self.GetJson()
        self.count = len(self.jsonobj.get("data"))

    def GetSudoku(self, idx):
        return self.jsonobj.get("data").get(idx).get("Puzzle")
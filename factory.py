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
    
    def _validateIdx_(self, idx):
        if not str(idx).isdigit():
            raise Exception("Expected numeric input.")
        idx = str(int(idx) - 1)
        return idx

    def _overwriteJson_(self, data):
        with open(self.dir + self.file, 'w') as jsonfile:
            _json_.dump(data, jsonfile)        

class sudokuTemplate(jsonfactory):
    """Load sudoku templates from memory"""
    def __init__(self, filename: str):
        super().__init__(filename)
        self.jsonobj = self.GetJson().get("data")
        self.count = len(self.jsonobj)

    def GetSudoku(self, idx: str):
        try:
            idx = self._validateIdx_(idx)
        except Exception as e:
            raise Exception(e.args[0])
        if not (int(idx) >= 0 and int(idx) <= self.count):
            raise Exception("This template does not exist: " + idx)
        return self.jsonobj.get(idx).get("Puzzle")

class sudokuSavestate(jsonfactory):
    """Load and save savestates from and to memory"""
    def __init__(self):
        try:
            file = open("data/savestates.json", 'r')
            file.close()
        except:
            file = open("data/savestates.json", 'w')
            _json_.dump({"data":{"recent":"0"}}, file)
            file.close()
        super().__init__("savestates")
        self.jsonobj = self.GetJson()
        self.recentSud = self.jsonobj.get("data").get("recent")

    def GetState(self, idx: str):
        try:
            idx = self._validateIdx_(idx)
        except Exception as e:
            raise Exception(e.args[0])
        if not idx in self.jsonobj.get("data").keys():
            raise Exception("No state for this game.")
        return self.jsonobj.get("data").get(idx)

    def SaveState(self, idx:str, state: str):
        try:
            idx = self._validateIdx_(idx)
        except Exception as e:
            raise Exception(e.args[0])
        try:
            self.jsonobj.get("data")[idx] = state
            self.jsonobj.get("data")["recent"] = idx
            self._overwriteJson_(self.jsonobj)
        except:
            raise Exception("Saving failed.")

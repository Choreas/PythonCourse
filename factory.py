import csv as _csv_, json as _json_

# This module contains classes that can be used to read and write json and csv files.
# They were not intended for general use but more specific to satisfy requirements to save and
# load game states. 
# It was fun writing them and I used it mainly to teach myself pythons implementation of file streams and
# class hierarchy, and to practice some json parsing and basic list / dictionary use.

# This class fulfills only one expectation, it can parse a csv file containing exactly one row of keys
# and n rows of values to a json file. Works only for existing csv files.
class csvfactory:
    """Factory for csv operations"""

    # Constructor: takes a filename and saves it to instance.
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
    
    # Read csv and return it as dictionary consisting of two pairs, first is keys, second values.
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

    # Very specific write method. Specific because it needs its data exactly as served by Readcsv(),
    # that is one dictionary pair "keys" and one "values".
    def WriteJson(self, filename):
        filename = filename.replace(" ", "", -1)
        csvlist = self.Readcsv()
        keys = csvlist.get("keys")
        values = csvlist.get("values")
        pairs = {"data":{vidx:{key:value[kidx] for kidx, key in enumerate(keys)} for vidx, value in enumerate(values)}}
        with open(self.dir + filename + ".json", 'w') as jsonfile:
            _json_.dump(pairs, jsonfile)

# Base class for classes which need to read and write specific information from and to json (see below).
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
    
    # This might be too specific, even in this context. This serves the special needs of the sudoku load and save
    # operations, because it subtracts 1 from user entered input (zero based index).
    def _validateIdx_(self, idx):
        if not str(idx).isdigit():
            raise Exception("Expected numeric input.")
        idx = str(int(idx) - 1)
        return idx

    # Overwrites its file. There must be a way to simply update specific parts where needed, but I didn't research
    # at that point.
    def _overwriteJson_(self, data):
        with open(self.dir + self.file, 'w') as jsonfile:
            _json_.dump(data, jsonfile)        

# This class (derived from jsonfactory) is intended to load game templates from json files.
# It needs the json structure produced by csvfactory.
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

# Load and save game states.
class sudokuSavestate(jsonfactory):
    """Load and save savestates from and to memory"""
    def __init__(self):
        # First try to open game state file. Name is fixed for this one.
        try:
            file = open("data/savestates.json", 'r')
            file.close()
        except:
            # This will create the file and its base structure in case it's not there.
            file = open("data/savestates.json", 'w')
            _json_.dump({"data":{"recent":"0"}}, file)
            file.close()
        super().__init__("savestates")
        self.jsonobj = self.GetJson()

        # This property is used to identify the last game played.
        self.recentSud = self.jsonobj.get("data").get("recent")

    # Returns a string containing values for sudoku fields.
    # Raises exception in case no state is available
    def GetState(self, idx: str):
        try:
            idx = self._validateIdx_(idx)
        except Exception as e:
            raise Exception(e.args[0])
        if not idx in self.jsonobj.get("data").keys():
            raise Exception("No state for this game.")
        return self.jsonobj.get("data").get(idx)

    # Saves state to json by recreating whole file.
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

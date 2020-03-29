import factory

cmds = {"csv":"Operate on a csv file", "exit":"Exit to menu", 
        "help":"Show help", "json":"Operate on a json file"}

def _PrintArgsHelp_(cmd):
    print("\n==help==\n")
    if cmd == "csv":
        cmdList = [["csv (this program)", "Follow instructions for this program"],
                   ["read", "Read contents of file"], ["writejson", "Write file content as json"],
                   ["help", "Show help"], ["exit", "Exit to menu"]]
    elif cmd == "json":
        cmdList = [["json (this program)", "Follow instructions for this program"],
                   ["get", "Get object from json"],
                   ["help", "Show help"], ["exit", "Exit to menu"]]
    else:
        cmdList = [["this program", "Follow instructions for this program"], 
                   ["help", "Show help"], ["exit", "Exit to menu"]]
    for item in cmdList:
        print((item[0] + ": " + item[1]))
    print("\n")

def _PrintHelp():
    cmdList = cmds.items()
    print("\n\n==help==\n")
    for item in cmdList:
        print((item[0] + ": " + item[1]))
    print("\n\n")

def _Server():
    inp = input("Factory: ")
    inp = inp.replace(" ", "", -1).lower()
    if not inp in cmds.keys() and not inp.isdigit():
        return ""
    return inp

def _argServer_(cmd, prompts):
    args = []
    for idx, prompt in enumerate(prompts):
        repeat = True
        while repeat:
            repeat = False
            arg = input(prompt)
            temparg = arg.lower()
            if temparg == "help":
                repeat = True
                _PrintArgsHelp_(cmd)
                continue
            if temparg == "exit":
                raise Exception("exit")
            args.append(arg)
    return args

def _csvFactory_():
    try:
        args = _argServer_("csv", ["Enter existing csv filename (located in data): "])
    except:
        print("\n")
        return
    try:
        csvobj = factory.csvfactory(args[0])
    except Exception as e:
        print(e.args[0])
        return
    while True:
        try:
            args = _argServer_("csv", ["csv: "])
        except:
            print("\n")
            break
        if args[0] == "read":
            print(csvobj.Readcsv())
            continue
        if args[0] == "writejson":
            try:
                args = _argServer_("csv", ["Enter name of json to write: "])
            except:
                print("\n")
                break 
            csvobj.WriteJson(args[0])
            continue

def _jsonFactory_():
    try:
        args = _argServer_("json", ["Enter existing json filename (located in data): "])
    except:
        print("\n")
        return
    try:
        jsonobj = factory.jsonfactory(args[0])
    except Exception as e:
        print(e.args[0])
        return
    while True:
        try:
            args = _argServer_("json", ["json: "])
        except:
            print("\n")
            break
        if args[0] == "get":
            try:
                print(jsonobj.GetJson())
            except Exception as e:
                print(e.args[0])
            continue

def Init():    
    while True:
        inp = _Server()
        if inp == "":
            print("Could not understand your input. help for help.")
            continue
        if inp == "help":
            _PrintHelp()
            continue
        if inp == "csv":
            _csvFactory_()
            continue
        if inp == "json":
            _jsonFactory_()
            continue
        if inp == "exit":
            break
        continue
num = 0
records = []
ttCheck = []
TT = {}
DPT = {}
pageLSN = {}

class LSN:
    def __init__(self, lsn, trans, page, action):
        self.lsn = lsn
        self.trans = trans
        self.page = page
        self.action = action
        if(action==""):
            self.desc ="LSN "+str(lsn)+": T"+str(trans)+" updates P"+str(page)
        elif(action=="commit"):
            self.desc ="LSN "+str(lsn)+": T"+str(trans)+" commit"
        elif(action=="end"):
            self.desc ="LSN "+str(lsn)+": T"+str(trans)+" end"
        elif(action=="disk"):
            self.desc ="LSN "+str(lsn)+": disk P"+str(page)
class ttObj:
    def __init__(self,lsn,p_lsn):
        self.lsn = lsn
        self.p_lsn = p_lsn
        
def printTT():
    global TT
    print("------Transaction Table------")
    print("T_ID\tLSN\tPrev LSN")
    for i in TT:
        print("T"+str(i)+"\t"+str(TT[i].lsn)+"\t"+str(TT[i].p_lsn))
        
def printDPT():
    global DPT
    print("------Dirty Page Table------")
    print("Page No.\tRecLSN")
    for i in DPT:
        print(str(i)+"\t\t"+str(DPT[i]))
        
def createRecords():
    global num,records,pageLSN
    num = 10
    while(1):
        print("*************************************************************")
        print('1.Update\t2.Commit\t3.Disk\t4.End Transaction\t5.System Crash')
        opt=int(input())
        if(opt==1):
            trans = int(input("Enter transaction number\n"))
            page = int(input("Enter page number\n"))
            x = LSN(num,trans,page,"")
            records.append(x)
            print(x.desc)
            num+=10
            if(page not in pageLSN.keys()):
                pageLSN[page] = 0
        elif(opt==2):
            action = "commit"
            trans = int(input("Enter transaction number\n"))
            x = LSN(num,trans,0,action)
            records.append(x)
            print(x.desc)
            num+=10
        elif(opt==2):
            action = "disk"
            page = int(input("Enter page number\n"))
            x = LSN(num,0,page,action)
            records.append(x)
            print(x.desc)
            num+=10
        elif(opt==4):
            action = "end"
            trans = int(input("Enter transaction number\n"))
            x = LSN(num,trans,0,action)
            records.append(x)
            print(x.desc)
            num+=10
        elif(opt==5):
            for i in range(0,len(records)):
                print(records[i].desc)
            print("\n")
            return
        else:
            print("Invalid option")
        
def phaseOne():
    print("\n******PHASE 1 - ANALYSIS******")
    global num,records,TT,ttCheck,DPT,pageLSN
    for i in range(0,len(records)):
        if(records[i].action==""):
            if(records[i].trans not in ttCheck):
                ttCheck.append(records[i].trans)
                x = ttObj(records[i].lsn,0)
                TT[records[i].trans] = (x)
            else:
                TT[records[i].trans].p_lsn = TT[records[i].trans].lsn
                TT[records[i].trans].lsn = records[i].lsn
                
            if(records[i].page not in DPT.keys()):
                DPT[records[i].page] = records[i].lsn
        if(records[i].action=="commit"):
            if(records[i].trans in ttCheck):
                del TT[records[i].trans]
        if(records[i].action=="disk"):
            pageLSN[records[i].page] = records[i].lsn
            
    printTT()         
    printDPT()
    
def phaseTwo():
    print("\n******PHASE 2 - REDO******")
    global num,records,TT,ttCheck,DPT
    for i in range(0,len(records)):
        if(records[i].action==""):
            if(records[i].page in DPT.keys()):
                if(DPT[records[i].page] <= records[i].lsn):
                    if(pageLSN[records[i].page] < records[i].lsn):
                        print("REDO LSN "+str(records[i].lsn))
                
def phaseThree():
    print("\n******PHASE 3 - UNDO******")
    global num,records,TT,ttCheck,DPT
    x = len(records)-1
    for i in range(x,0,-1):
        if(records[i].trans in TT.keys()):
            temp = LSN(num,0,0,"undo")
            temp.desc = "LSN "+str(num)+": CLR undo LSN"+str(records[i].lsn)
            records.append(temp)
            num+=10
    for i in range(0,len(records)):
        print(records[i].desc)
    
    
createRecords()
phaseOne()
phaseTwo()  
phaseThree()
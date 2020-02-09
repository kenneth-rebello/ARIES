# runfile('C:/Users/Kenneth Rebello/Desktop/College/ADMT/five.py', wdir='C:/Users/Kenneth Rebello/Desktop/College/ADMT')
# *************************************************************
# 1.Update        2.Commit        3.Disk  4.End Transaction       5.System Crash

# 1

# Enter transaction number
# 1

# Enter page number
# 5
# LSN 10: T1 updates P5
# *************************************************************
# 1.Update        2.Commit        3.Disk  4.End Transaction       5.System Crash

# 1

# Enter transaction number
# 2

# Enter page number
# 3
# LSN 20: T2 updates P3
# *************************************************************
# 1.Update        2.Commit        3.Disk  4.End Transaction       5.System Crash

# 2

# Enter transaction number
# 2
# LSN 30: T2 commit
# *************************************************************
# 1.Update        2.Commit        3.Disk  4.End Transaction       5.System Crash

# 4

# Enter transaction number
# 2
# LSN 40: T2 end
# *************************************************************
# 1.Update        2.Commit        3.Disk  4.End Transaction       5.System Crash

# 1

# Enter transaction number
# 3

# Enter page number
# 1
# LSN 50: T3 updates P1
# *************************************************************
# 1.Update        2.Commit        3.Disk  4.End Transaction       5.System Crash

# 1

# Enter transaction number
# 3

# Enter page number
# 3
# LSN 60: T3 updates P3
# *************************************************************
# 1.Update        2.Commit        3.Disk  4.End Transaction       5.System Crash

# 5
# LSN 10: T1 updates P5
# LSN 20: T2 updates P3
# LSN 30: T2 commit
# LSN 40: T2 end
# LSN 50: T3 updates P1
# LSN 60: T3 updates P3



# ******PHASE 1 - ANALYSIS******
# ------Transaction Table------
# T_ID    LSN     Prev LSN
# T1      10      0
# T3      60      50
# ------Dirty Page Table------
# Page No.        RecLSN
# 5               10
# 3               20
# 1               50

# ******PHASE 2 - REDO******
# REDO LSN 10
# REDO LSN 20
# REDO LSN 50
# REDO LSN 60

# ******PHASE 3 - UNDO******
# LSN 10: T1 updates P5
# LSN 20: T2 updates P3
# LSN 30: T2 commit
# LSN 40: T2 end
# LSN 50: T3 updates P1
# LSN 60: T3 updates P3
# LSN 70: CLR undo LSN60
# LSN 80: CLR undo LSN50
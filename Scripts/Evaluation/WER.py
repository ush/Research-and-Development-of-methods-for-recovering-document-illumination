import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('-rp', '--ref_path', type=str)
parser.add_argument('-hp', '--hyp_path', type=str)
parser.add_argument('-in', '--img_num', type=str)
parser.add_argument('-op', '--out_path', type=str)
args = parser.parse_args()

with open(args.ref_path) as rf:
	ref = rf.read()
with open(args.hyp_path) as hp:
	hyp = hp.read()

ref = ref.replace("\n", " ")
hyp = hyp.replace("\n", " ")
ref = re.sub(r'[^A-Za-zА-Яа-я\s]', '', ref)
hyp = re.sub(r'[^A-Za-zА-Яа-я\s]', '', hyp)

def wer(ref, hyp ,debug=False):
    r = ref.split()
    h = hyp.split()
    costs = [[0 for inner in range(len(h)+1)] for outer in range(len(r)+1)]
    backtrace = [[0 for inner in range(len(h)+1)] for outer in range(len(r)+1)]
 
    OP_OK = 0
    OP_SUB = 1
    OP_INS = 2
    OP_DEL = 3
    DEL_PENALTY = 1
    INS_PENALTY = 1
    SUB_PENALTY = 1
    
    for i in range(1, len(r)+1):
        costs[i][0] = DEL_PENALTY*i
        backtrace[i][0] = OP_DEL
    
    for j in range(1, len(h) + 1):
        costs[0][j] = INS_PENALTY * j
        backtrace[0][j] = OP_INS
    
    # computation
    for i in range(1, len(r)+1):
        for j in range(1, len(h)+1):
            if r[i-1] == h[j-1]:
                costs[i][j] = costs[i-1][j-1]
                backtrace[i][j] = OP_OK
            else:
                substitutionCost = costs[i-1][j-1] + SUB_PENALTY # penalty is always 1
                insertionCost    = costs[i][j-1] + INS_PENALTY   # penalty is always 1
                deletionCost     = costs[i-1][j] + DEL_PENALTY   # penalty is always 1
                 
                costs[i][j] = min(substitutionCost, insertionCost, deletionCost)
                if costs[i][j] == substitutionCost:
                    backtrace[i][j] = OP_SUB
                elif costs[i][j] == insertionCost:
                    backtrace[i][j] = OP_INS
                else:
                    backtrace[i][j] = OP_DEL

    i = len(r)
    j = len(h)
    numSub = 0
    numDel = 0
    numIns = 0
    numCor = 0
    if debug:
        print("OP\tREF\tHYP")
        lines = []
    while i > 0 or j > 0:
        if backtrace[i][j] == OP_OK:
            numCor += 1
            i-=1
            j-=1
            if debug:
                lines.append("OK\t" + r[i]+"\t"+h[j])
        elif backtrace[i][j] == OP_SUB:
            numSub +=1
            i-=1
            j-=1
            if debug:
                lines.append("SUB\t" + r[i]+"\t"+h[j])
        elif backtrace[i][j] == OP_INS:
            numIns += 1
            j-=1
            if debug:
                lines.append("INS\t" + "****" + "\t" + h[j])
        elif backtrace[i][j] == OP_DEL:
            numDel += 1
            i-=1
            if debug:
                lines.append("DEL\t" + r[i]+"\t"+"****")
    if debug:
        lines = reversed(lines)
        for line in lines:
            print(line)
        print("#cor " + str(numCor))
        print("#sub " + str(numSub))
        print("#del " + str(numDel))
        print("#ins " + str(numIns))
    # return (numSub + numDel + numIns) / (float) (len(r))
    if len(r) != 0:
    	wer_result = round( (numSub + numDel + numIns) / (float) (len(r)), 3)
    else:
    	wer_result = -1
    #return {'WER':wer_result, 'numCor':numCor, 'numSub':numSub, 'numIns':numIns, 'numDel':numDel, "numCount": len(r)}
    return wer_result
    
wer_res = wer(ref, hyp)
line = args.img_num[:-4] + ", " + str(wer_res) + "\n"
with open(args.out_path , 'a') as file:
	file.write(line)


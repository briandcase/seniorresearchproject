'''
Created on Feb 28, 2019

@author: bdcas
'''
import re

def SymbolToNumber(Symbol):
    """
    Converts base to number (in lexicograpical order)

    Symbol: the letter to be converted (str)

    Returns: the number correspondinig to that base (int)
    """
    if Symbol == "A":
        return 0
    elif Symbol == "C":
        return 1
    elif Symbol == "G":
        return 2
    elif Symbol == "T":
        return 3


def NumberToSymbol(index):
    """
    Finds base from number (in lexicographical order)

    index: the number to be converted (int)

    Returns: the base corresponding to index (str)
    """
    if index == 0:
        return str("A")
    elif index == 1:
        return str("C")
    elif index == 2:
        return str("G")
    elif index == 3:
        return str("T")


def HammingDistance(p, q):
    """
    Finds the number of mismatches between 2 DNA segments of equal lengths

    p: first DNA segment (str)

    q: second DNA segment (str)

    Returns: number of mismatches (int)
    """
    return sum(s1 != s2 for s1, s2 in zip(p, q))


def window(s, k):
    for i in range(1 + len(s) - k):
        yield s[i:i+k]


def ProfileMostProbable(Text, k, Profile):
    """
    Finds a k-mer that was most likely to be generated by profile among
    all k-mers in Text

    Text: given DNA segment (str)

    k: length of pattern (int)

    Profile: a 4x4 matrix (list)

    Returns: profile-most probable k-mer (str)
    """
    letter = [[] for key in range(k)]
    
    probable = ""
    hamdict = {}
    index = 1
    for a in range(k):
        for j in "ACGT":
            letter[a].append(Profile[j][a])
    for b in range(len(letter)):
        number = max(letter[b])
        probable += str(NumberToSymbol(letter[b].index(number)))
    for c in window(Text, k):
        for x in range(len(c)):
            y = SymbolToNumber(c[x])
            if x and y is not None: # check if none is present
                index *= float(letter[x][y])
        hamdict[c] = index
        index = 1
    for pat, ham in hamdict.items():
        if ham == max(hamdict.values()):
            final = pat
            break
    return final


def Count(Motifs):
    """
    Documentation here
    """
    count = {}
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for i in range(k):
            count[symbol].append(0)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count


def FindConsensus(motifs):
    """
    Finds a consensus sequence for given list of motifs

    motifs: a list of motif sequences (list)

    Returns: consensus sequence of motifs (str)
    """
    consensus = ""
    for i in range(len(motifs[0])):
        countA, countC, countG, countT = 0, 0, 0, 0
        for motif in motifs:
            if motif[i] == "A":
                countA += 1
            elif motif[i] == "C":
                countC += 1
            elif motif[i] == "G":
                countG += 1
            elif motif[i] == "T":
                countT += 1
        if countA >= max(countC, countG, countT):
            consensus += "A"
        elif countC >= max(countA, countG, countT):
            consensus += "C"
        elif countG >= max(countC, countA, countT):
            consensus += "G"
        elif countT >= max(countC, countG, countA):
            consensus += "T"
    return consensus


def ProfileMatrix(motifs):
    """
    Finds the profile matrix for given list of motifs

    motifs: list of motif sequences (list)

    Returns: the profile matrix for motifs (list)
    """
    Profile = {}
    A, C, G, T = [], [], [], []
    for j in range(len(motifs[0])):
        countA, countC, countG, countT = 0, 0, 0, 0
        for motif in motifs:
            if motif[j] == "A":
                countA += 1
            elif motif[j] == "C":
                countC += 1
            elif motif[j] == "G":
                countG += 1
            elif motif[j] == "T":
                countT += 1
        A.append(countA)
        C.append(countC)
        G.append(countG)
        T.append(countT)
    Profile["A"] = A
    Profile["C"] = C
    Profile["G"] = G
    Profile["T"] = T
    return Profile


def Score(motifs):
    """
    Finds score of motifs relative to the consensus sequence

    motifs: a list of given motifs (list)

    Returns: score of given motifs (int)
    """
    consensus = FindConsensus(motifs)
    score = 0.0000
    for motif in motifs:
        score += HammingDistance(consensus, motif)
    #print(score)
    return round(score, 4)

def GreedyMotifSearch(DNA, k, t):
    """
    Documentation here
    """
    import math
    bestMotifs = []
    bestScore = math.inf
    for string in DNA:
        bestMotifs.append(string[:k])
    base = DNA[0]
    for i in window(base, k):
        # Change here. Should start with one element in motifs and build up.
        # As in the line "motifs <- list with only Dna[0](i,k)"
        # newMotifs = []
        newMotifs = [i]
        # Change here to iterate over len(DNA). 
        # Should go through "for j from 1 to |Dna| - 1"
        # for j in range(t):
        for j in range(1, len(DNA)):
            # Change here. Should build up motifs and build profile using them.
            # profile = ProfileMatrix([i])
            profile = ProfileMatrix(newMotifs)
            probable = ProfileMostProbable(DNA[j], k, profile)
            newMotifs.append(probable)

        # Change to < rather < = to ensure getting the most recent hit. As referenced in the instructions:
        # If at any step you find more than one Profile-most probable k-mer in a given string, use the one occurring **first**.
        if Score(newMotifs) < bestScore:
        #if Score(newMotifs) <= bestScore:
            bestScore = Score(newMotifs)
            bestMotifs = newMotifs
    return bestMotifs

f=open("boundaryleft.fasta", "r")
if f.mode == "r":
    contents = f.read()
    leftSide = re.sub(r"[\n\t\s]*", "", contents)

f=open("boundaryright.fasta", "r")
if f.mode == "r":
    contents = f.read()
    rightSide = re.sub(r"[\n\t\s]*", "", contents)

testDNA = [leftSide, rightSide]
kmers = 4
t = 2
print(GreedyMotifSearch(testDNA, kmers, t))
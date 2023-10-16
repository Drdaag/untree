Authors = '\"Prenom\\nNom\\nLogin\\nMail\\n\"'

def iCount(stri, i):
    leng = len(stri)
    leng2 = len(i)
    k = 0
    res = 0
    while(k < leng - leng2 + 1):
        j = 0
        while(k < leng - leng2 + 1 and i[0] != stri[k]):
            k += 1
        while(j < leng2 and k < leng and i[j] == stri[k]):
            j+=1
            k+=1
        if(j == leng2):
            res += 1
        
    return res


# print(iCount("│   ├── chess.c", "   "), "1") 
# print(iCount("   ", "   "), "1") 
# print(iCount("      ", "   "), "2") 
# print(iCount("   d", "   "), "1") 
# print(iCount("  d ", "   "), "0") 
# print(iCount("   d ", "   "), "1") 
# print(iCount("   d   ", "   "), "2") 
# print(iCount("adbcd d", "abc"), "0") 
# print(iCount("abca", "abc"), "1") 
# print(iCount("abcab cab abcabc abcaabc", "abc"), "5") 



def makefiles():
    s = input("tree : ")
    slist = []
    # print(s)
    while(s):
        # print("->", s)
        slist.append(s)
        s = input("")

    # slist = s.split('\\n')
    # print(slist)

    leng = len(slist)
    ldis = []
    namel = []
    if(slist[0] == '.'):
        slist.pop(0)
        leng -= 1
    # print("The leng is :", leng)
    for i in slist:
        step = iCount(i, "   ")
        ldis.append(step)
        namel.append(getName(i))
        # print(step)
    typ = tellFileOrFolder(ldis)
    # print(typ)
    
    toCreate = mergeInfo(ldis, typ, namel)
    print(toCreate)
    print()
    
    i = 0
    # print(leng)
    # print(len(toCreate))
    
    PATH = "./"
    while(i < leng):
        # print("This is i = ", i)
        if(toCreate[i][1] == "File"):
            # print("CREATE FILE : ", toCreate[i][2])
            print("touch " + "\"" +toCreate[i][2] + "\"")
            if(toCreate[i][2] == 'AUTHORS'):
                print("printf "+ Authors +" > AUTHORS")
            i += 1
        else:
            i = createFolderAndFiles(toCreate, i)
            # i = createFolderAndFiles(toCreate, i, PATH + toCreate[i][2]+"/")
   
def getName(s):
    leng = len(s)
    i = 0
    while(i + 2 < leng):
        if(s[i]=="─" and s[i+1]=="─" and s[i+2]==" "):
            # print("->", s[i+3:])
            return s[i+3:]
        i += 1;
    return ""
        

def createFolderAndFiles(listeFichiers, start):
    print("mkdir "+ "\"" + listeFichiers[start][2] +"\"")
    print("cd " + "\"" + listeFichiers[start][2] + "\"")
    # print("cd " + "\"" + path + "\"")
    indice = listeFichiers[start][0]
    leng = len(listeFichiers)
    i = start + 1
    while(i < leng and listeFichiers[i][0] > indice):
        if(listeFichiers[i][1] == "File"):
            print("touch " + "\"" + listeFichiers[i][2] + "\"")
            # print("CREATE FILE ("+ listeFichiers[start][2] +"): ", listeFichiers[i][2])
            if(listeFichiers[i][2] == 'AUTHORS'):
                print("printf "+ Authors +" > AUTHORS")
            i += 1;
        else:
            i = createFolderAndFiles(listeFichiers, i)
    print("cd ..")        
    return i;

# With path

# def createFolderAndFiles(listeFichiers, start, path):
#     print("mkdir "+ "\"" + listeFichiers[start][2] +"\"")
#     print("cd " + "\"" + listeFichiers[start][2] + "\"")
#     # print("cd " + "\"" + path + "\"")
#     indice = listeFichiers[start][0]
#     leng = len(listeFichiers)
#     i = start + 1
#     while(i < leng and listeFichiers[i][0] > indice):
#         if(listeFichiers[i][1] == "File"):
#             print("touch " + "\"" + listeFichiers[i][2] + "\"")
#             # print("CREATE FILE ("+ listeFichiers[start][2] +"): ", listeFichiers[i][2])
#             i += 1;
#         else:
#             i = createFolderAndFiles(listeFichiers, i, path + listeFichiers[i][2]+"/")
#     print("cd ..")        
#     return i;
    
def tellFileOrFolder(lis):
    leng = len(lis)
    res = []
    for e in range(leng - 1):
        if(lis[e] < lis[e+1]):
            res.append("Folder")
        else:
            res.append("File")
            
    res.append("File")
    return res 

def mergeInfo(list1, list2, list3):
    leng =len(list1)
    res = []
    for i in range(leng):
        res.append([list1[i], list2[i], list3[i]])
    return res
        
        
# def makefiles(s):
#     # s = input("tree : ")

#     slist = s.split('\n')

#     leng = len(slist)
#     for i in slist:
#         step = iCount(i, "   ")
#         print(step)
        
makefiles();

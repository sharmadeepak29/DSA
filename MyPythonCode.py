name="sam"
##for _ in range(3):
##    print(name)

##
##
##for i in range(1,5):
##    print(i)

##def sym(list1, list2):
##    set1 = set(list1)
##    set2 = set(list2)
##    print(set1.symmetric_difference(set2))   
##
##sym([1,2,3], [5,2,1,4])



def sym(list1, list2):
    sym_diff = []
    for num in list1:
        if num not in list2 and num not in sym_diff:
            sym_diff.append(num)
            
    for num in list2:
        if num not in list1 and num not in sym_diff:
            sym_diff.append(num)

    print(sym_diff)
    
sym([1,2,3], [5,2,1,4])
sym([1, 2, 3], [5, 2, 1, 4])
sym([1, 2, 3, 3], [5, 2, 1, 4])
sym([1, 2, 3, 3], [5, 2, 1, 4])
sym([1, 2, 3], [5, 2, 1, 4, 5])
sym([1, 2, 3], [5, 2, 1, 4, 5])




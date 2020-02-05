#!/usr/bin/python

import copy
from collections import Counter

tmp = [2,3,4,5,6,8,9,10,12,15,16,18,20,24,25,27,30,32,36,40,45,48,50,54,60,64,72,75,80,81,90,96]

tpl = "{0:15}\t"


def calculate_add_combination_4_num(n):
    res_list = []
    tmp_list = []
 
    def num_to_n(n,tmp_list, start):
        if n == 1:
            tmp = copy.deepcopy(tmp_list)
            tmp.append(1)
            res_list.append(tmp)
        else:
            for i in range(start,n):
                tmp_list.append(i)
                num_to_n(n-i,tmp_list,i)
                tmp_list.remove(tmp_list[-1])
 
            tmp = copy.deepcopy(tmp_list)
            tmp.append(n)
            res_list.append(tmp)
 
    num_to_n(n,tmp_list, 1)
    # duplicate remove
    res_list = duplicate_remove(res_list, n)
    return res_list
 
 
def duplicate_remove(a_list, n):
    len_list = len(a_list)
    for i in range(len_list - 1, -1, -1):
        # remove list which equal to its own
        if len(a_list[i]) == 1:
            a_list.remove(a_list[i])
            continue
        for j in range(i):
            if set(a_list[i]) == set(a_list[j]):
                a_list.remove(a_list[i])
                break
    return a_list
        

            
def uefind(uenum,rbmax,rblen):
    lst = []#row :uenum col: rblen
    for i in range(uenum):
        lst.append([])
        for j in range(rblen):
            lst[i].append(tmp[j]*(i+1))
    print lst[18][0]

    lst_rst = []

    for i in range(uenum):
        j = uenum - 1  - i#back end
        rem = i # 0 1 2 3 ...
        if rem == 0 :
            for m in range(rblen):
                if lst[j][m] > rbmax:
                    print lst_rst
                    break
                else:
                    lst_rst.append(lst[j][m])

        else:
            tmp_uecom = cal_add_com(uenum,i)
            print j,
            print tmp_uecom

            for k in range(rblen):
                if lst[j][k] > rbmax:
                    break
                else:
                    tmp_rbmax = rbmax - lst[j][k]
                    tmp_uecom = rbsearch(tmp_uecom,tmp_rbmax,lst[j][k],lst)
                     
    #print lst_rst

def rbsearch(uecom,rbmax,rb0,lst):
    #print lst
    
    for item in uecom[:]:
        sumadd = 0
        #print item
        rblst = list(set(item))
        cnt = Counter(item)
        for i in range(len(cnt)):
            
            sumadd += sumadd + sum(lst[rblst[i]-1][:cnt[rblst[i]]])
        if sumadd > rbmax:
            uecom.remove(item)
    return uecom
                


def cal_add_com(uenum,rbidx):
    uecom = calculate_add_combination_4_num(rbidx)
    uecom.append([rbidx])
    for item in uecom[:]:
        if max(item) > (uenum - rbidx):
            uecom.remove(item)
    return uecom
    
        
                

 

if __name__ == "__main__":
    uenum = 20
    rbmax = 96
    rblen = len(tmp)
    uefind(uenum,rbmax,rblen)


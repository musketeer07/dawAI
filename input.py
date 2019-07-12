import pandas as pd
import numpy as np
df=pd.read_csv(r'C:\Users\Kartikay Raheja\Desktop\Testing.csv')
df1=df
df1.set_index(df1['prognosis'],inplace=True)
df1=df1.transpose()
cols=df1.columns
n=2
df1.columns = df1.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, newnode):
        if self.head is None:
            self.head = newnode
        else:
            self.head.next = newnode
    def display(self):
        temp=self.head

        while temp is not None:
            print(temp.data)
            temp=temp.next
    def intersect(self):
        temp=self.head.next
        while temp is not None:
            arr=self.head.data.intersection(temp.data)
            temp=temp.next
        return arr

    def sym_z(self):
        dis_arr = linklist.intersect()
        dis_arr = dis_arr.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
        i = 0
        dis_num = []
        for i in range(len(df1.columns)):
            for j in range(len(dis_arr)):
                if dis_arr[j] == df1.columns[i]:
                    dis_num.append(i)
        dis_symp = np.empty([0, len(dis_num)], dtype=object)
        for i in range(0, len(dis_num)):
            dis_symp = np.union1d(dis_symp, np.array(
                pd.DataFrame(df1.iloc[:, dis_num[i]].where(df1.iloc[:, dis_num[i]] == 1).dropna()).index))

        dis_symp_inters = np.empty([0, len(dis_num)], dtype=object)
        for i in range(0, len(dis_num) - 1):
            dis1 = np.array(pd.DataFrame(df1.iloc[:, dis_num[i]].where(df1.iloc[:, dis_num[i]] == 1).dropna()).index)
            dis2 = np.array(
                pd.DataFrame(df1.iloc[:, dis_num[i + 1]].where(df1.iloc[:, dis_num[i + 1]] == 1).dropna()).index)
            dis_symp_inters = np.union1d(dis_symp_inters, np.intersect1d(dis1, dis2))
        return np.setdiff1d(dis_symp, dis_symp_inters)


linklist=LinkedList()

class Node:
    def __init__(self, data):
        self.data = data
        self.next=None






for i in range(0,n):
    sym=str(input())
    node=linklist.insert(Node(pd.DataFrame(df[sym].where(df[sym] == 1).dropna()).index))

print(linklist.intersect())
sym_arr=linklist.sym_z()
n+=1

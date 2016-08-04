#-*- coding:utf-8 -*-

#堆排序

def adjust_heap(lists, i, size)
   lchild = 2 * i + 1
   rchild = 2 * i + 2

   if i < size / 2
        if lchild < size and lists[lchild] > lists[max]:
            max = lchild

        if rchild < size and lists[rchild] > lists[max]:
            max = rchild





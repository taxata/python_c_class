
# worked with Python 2.7.10
# @ by tChatz
# alpha test
'''
�������� 5� ��������� ����������

������������� 2 / ������ 87
�� ������������� ��� ��������� ��� ����������� �� �������, ���� �� ���������
��� ����� �������� �� �������� �����. ������� ������ �� �� ��������, ����� ��
������ ����� �������� ������ ���� ����� ��������� ��� ������� �� ���� ��� ���-
����; �� �� ��������� ����;
'''
## ������� ���������� ����������� �� �������
# ������ ��� ����� ��� ���������� ��������� ���� ������
# ������ ��� ������ start & end

def findMinPosition(start, end, List):
    position = start
    for i in range(start, end):
        if List[i] < List[position] :
            position = i
    return position

# ���������� ����������� selection sort
def selectionSortAscending(List):
    position = None
    n = len(List)
    for i in range(0,n):
        position = findMinPosition(i, n, List)
        List[i], List[position] = List[position], List [i]
    return List

# � ���� ���� ������ ������ �� ����� �� ���� ���� �������:
# 1�� Pythonic Way �� ����������� ���� ������ ������ ��� �����������
def selectionSortDescending(List):
    position = None
    n = len(List)
    for i in range(0,n):
        position = findMinPosition(i, n, List)
        List[i], List[position] = List[position], List [i]
    List = List.reverse()
    return List

# 2�� ����� ������ ���� ������ ������ ��� �����������
def findMinMaxPosition(start, end, List, AscDesc):
    # ����������� ��� ������� ����� ��� min ���� �� ������� ��� �� ���� ��� max
    # ������� �� ���������� ������� (Ascending) � �������� (Descending) ����������
    position = start
    for i in range(start, end):
        if AscDesc.lower()=='a':
            if List[i] < List[position] :
                position = i
        elif AscDesc.lower()=='d' :
            if List[i] > List[position] :
                position = i
    return position

def selectionSort2(List,AscDesc):
    # �������� ������ ���� ���������� ��� ���������
    position = None
    n = len(List)
    for i in range(0,n):
        position = findMinMaxPosition(i, n, List,AscDesc)
        List[i], List[position] = List[position], List [i]
    return List

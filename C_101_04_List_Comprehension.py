# worked with Python 2.7.10
# @ by tChatz
# alpha test

'''
�������� 6� ���������� �������
������������� 4 / ������ 101
�� ��������� ��� �� ������, ���� �� ����������� �� �������� �������. �����������
��� ����� ���.        
'''

my_list = [i**2 for i in range(1,11)]
f = open('output.txt', 'w')
for item in my_list:
    f.write(str(item) + '\n') # ������� string ������ � write
f.close()
f = open('output.txt', 'r')
print f.readline()
print f.read()
f.close()
    

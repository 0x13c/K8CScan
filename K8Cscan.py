#coding=utf-8
#pythonnet 
#Test Win7 x86
import clr #py2.7.9 ����������� �����exe�ͱ��� Python.Runtime.Runtime
#python 3.4.4 ִ��PY�ű����ѱ��� Github�Ͽ������߻�δ��� δ��������쳣:  System.InvalidProgramException: ������������ʱ��⵽��Ч�ĳ���
#�� clrModule.PyInit_clr()
import sys

print('python call K8Cscan c# dll')

#���.net���п�·��Ҳû��
#sys.path.append("c:\\Program Files\\Reference Assemblies\\Microsoft\\Framework\\v3.5\\")
#sys.path.append("C:\\Windows\\Microsoft.NET\\Framework\\v2.0.50727\\")
#sys.path.append("C:\\Windows\\Microsoft.NET\\Framework\\v4.0.30319\\")

#DLL����·��(��ǰ·������Ҫ)
#sys.path.append("C:\\Users\\K8team\\Desktop\\pynet")
clr.FindAssembly('netscan.dll')
#����(���϶�˵�������ռ�),��д����: System.IO.FileNotFoundException
clr.AddReference('netscan')
#�����ռ�
from CscanDLL import * 
print(scan.run('192.168.1.1'))

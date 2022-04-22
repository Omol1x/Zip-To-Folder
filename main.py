import zipfile
import os
import tkinter.filedialog as fd

a = fd.askdirectory()
b = input('Delete archives? (y/n): ')
for i in os.listdir(a):
	nf = a+'\\'+i.replace('.zip','')
	os.mkdir(nf)
	z = zipfile.ZipFile(a+'\\'+i)
	z.extractall(nf)
	z.close()
	if b == 'y':
		os.remove(a+'\\'+i)

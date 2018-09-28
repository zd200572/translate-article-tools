 # -*- coding: utf-8 -*-
##Used for translate article, to avoid the meaning changing because of enter
#翻译论文时去除换行和行末连字符
def drop_enter(fin):
	with open(fin,) as f: #'r', encoding='UTF-8'
		paragraph = ''
		for line in f:
			if line != '':
				line= line.strip()
				if line[-1] == '-':
					line = line[:-1]
				else:
					line += ' '
				paragraph += line
	return paragraph


#paragraph = drop_enter("fin.txt")
#print paragraph 
#print(paragraph)
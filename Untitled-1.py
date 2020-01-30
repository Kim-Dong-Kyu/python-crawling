fr =open("test.txt",'r',encoding="UTF-8")
fw =open("test_copy.txt",'w',encoding='UTF-8')
fw.write(fr.read())

fw.close()
fr.close()

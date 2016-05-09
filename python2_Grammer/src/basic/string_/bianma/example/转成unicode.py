#coding=utf-8
'''
把任何 字符串转成unicode
'''
def getunicode(sentence): 
    '''如果无法转string 则返回'''
    if not isinstance(sentence, str):
        try:
            sentence = str(sentence)
        except :
            return""
    '''传进来一句话转为unicode编码'''
    if not isinstance(sentence, unicode):
        try:
            sentence = sentence.decode('utf-8')
        except :
            sentence = sentence.decode('gbk','ignore') 
    return sentence

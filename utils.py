def ireplace(old,new,text):
	idx=0
	while idx<len(text):
		index_l = text.lower().find(old.lower(),idx)
		if index_l == -1:
			return text
		text = text[:index_l]+new+text[index_l + len(old):]
		idx = index_l +len(new)
	return text

def highlight_words(text,term,start_teg,end_teg):
	text = ireplace(term, start_teg+term+end_teg,text)
	return text
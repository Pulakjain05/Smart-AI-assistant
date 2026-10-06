import easyocr
reader = easyocr.Reader(['en'])
result = reader.readtext('test.jpg')
texts=[]
for detection in result:
    text = detection[1]
    confidence = detection[2]
    if confidence>0.5:
        texts.append(text)
final_text=" ".join(texts)        
print("final text:",final_text)
    
from wikipedia import *
import spacy


nlp = spacy.load("en_core_web_sm")
doc = nlp("The conglomerate was adamant that they did not infringe the copyright of Microsoft, the had merely imitated the idea for the surface tablet to create the ipad")

lemmatizer = nlp.get_pipe("lemmatizer")

lemma_list = [(word.text,  word.pos_) for word in doc]
print(lemma_list)
print("-" * 10)
propn_list = []
noun_list = []

for i in lemma_list:

    if i[1] == "PROPN":
        propn_list.append(i[0])
    elif i[1] == "NOUN":
        noun_list.append(i[0])
        
print("traducteur:")        
for i in noun_list:
    from deep_translator import GoogleTranslator
    translated = GoogleTranslator(source='auto', target='fr').translate(i)    
    print(i, " = ", translated)    

print("-" * 10) 
print("wikipedia:")        
for i in propn_list:
    print(i, " = ", wikipedia.summary(str(i), sentences=1))
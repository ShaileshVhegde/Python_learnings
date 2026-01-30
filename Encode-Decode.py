import random
X=input("Enter text to encode: ")
if (len(X)>=3):
    Encoded_text=X[1:]+X[0]
   
    sufix="".join(random.choice('abcdefghijklmnopqrstuvwxyz')for i in range(3))
    prefix="".join(random.choice('abcdefghijklmnopqrstuvwxyz')for i in range(3))
    encoded=prefix+Encoded_text+sufix
    print("Encoded text is: ",encoded)
else:
    Encoded_text=X[-1]+X[0:-1]
    print("Encoded text is: ",Encoded_text)
print("enetering decoding phase")
Y=input("Enter text to decode: ")
if(len(Y)>=3):
    decode_text=Y[3:-3]
    decode=decode_text[-1]+decode_text[0:-1]
    print("Decoded text is: ",decode)
else:
    decode=Y[-1]+Y[0:-1]
    print("Decoded text is: ",decode)
    
    
    
    
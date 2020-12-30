import threading 
from threading import*
import time
dic={}
exc.create("sai",26)
exc.create("source",76,3320) 
exc.read("sai")
exc.read("source")
exc.create("sai",60)
exc.modify("sai",75) 
exc.delete("sai")
t1=Thread(target=(create or read or delete),args=(key_name,value,timeout))
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout))
t2.start()
t2.sleep()
def create(key,value,timeout=0):
    if key in d:
        print("error: this key already exists") 
    else:
	size=1024*1024*1024
	sizeval=16*1024*1024
        if(key.isalpha()):
            if len(dic)<(size) and value<=(sizeval):
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: #constraints for input key_name capped at 32chars
                    dic[key]=l
            else:
                print("error: Memory limit exceeded!! ")
        else:
            print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")
def read(key):
    if key not in dic:
        print("error: given key does not exist in database. Please enter a valid key")
    else:
        b=dic[key]
        if b[1]!=0:
            if time.time()<b[1]:
                stri=str(key)+":"+str(b[0])
                return stri
            else:
                print("error: time-to-live of",key,"has expired")
        else:
            stri=str(key)+":"+str(b[0])
            return stri
def delete(key):
    if key not in dic:
        print("error: given key does not exist in database") 
    else:
        b=dic[key]
        if b[1]!=0:
            if time.time()<b[1]:
                del dic[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired")
        else:
            del dic[key]
            print("key is successfully deleted")

def modify(key,value):
    b=dic[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in dic:
                print("error: given key does not exist in database")
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                dic[key]=l
        else:
            print("error: time-to-live of",key,"has expired") 
    else:
        if key not in dic:
            print("error: given key does not exist in database") 
        else:
            l=[]
            l.append(value)
            l.append(b[1])
            dic[key]=l
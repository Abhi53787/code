def hai(*name):
    print(name)
    for i in name:
        print(i)



def hello(**values):
    print(values)
    for k,v in values.items():
        print(k,  "==",  v)
            
            
        

hai("dfg","dfh","stys")
hello(llo="fdgdf",ol="ddf")

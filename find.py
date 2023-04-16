import re
import sys
import argparse
def find():
    with open('data.json','r') as f:
        text=f.read()
        # print(text)
        pattern1=r"/.*jpg"
        pattern2=r"\d{4}.*\d{2}:\d{2}:\d{2}"
        pattern3=r"\"name\":.*\""
        path=re.findall(pattern1,text)
        time=re.findall(pattern2,text)
      
        name=re.findall(pattern3,text)
        leng=len(path)
        for i in range(leng):
            print(re.sub('/boa/www','..',path[i]))
            print(time[i])
            print(re.sub('\"name\":','User',name[i]))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--par1', nargs='+', type=str, default='weights/best.pt', help='model.pt path(s)')
    opt = parser.parse_args()
    # print(opt)
    find()
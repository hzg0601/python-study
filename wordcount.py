# -*- coding: utf-8 -*-

#Created on Sat Feb  3 19:37:14 2018

#@author: hzg0601

import turtle
count=10
data=[]
words=[]
yscale=6
xscale=30

def drawline(t,x1,y1,x2,y2):
    t.penup()
    t.goto(x1,y1)
    t.pendown()
    t.goto(x2,y2)
    
def drawtext(t,x,y,text):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.write(text)

def drawgraph(t):
    drawline(t,0,0,360,0)
    drawline(t,0,300,0,0)
    
    for x in range(count):
        x=x+1
        drawtext(t,x*xscale-4,-20,(words[x-1]))
        drawtext(t,x*xscale-4,data[x-1]*yscale+10,data[x-1])
    drawbar(t)
    
def drawrectangle(t,x,y):
    x=x*xscale
    y=y*yscale
    drawline(t,x-5,0,x-5,y)
    drawline(t,x-5,y,x+5,y)
    drawline(t,x+5,y,x+5,0)
    drawline(t,x+5,0,x-5,0)
    
def drawbar(t):
    for i in range(count):
        drawrectangle(t,i+1,data[i])
        
def processline(line,wordcounts):
    line=repalcepunctions(line)
    words=line.split()
    for word in words:
        if word in wordcounts:
            wordcounts[word]+=1
        else:
            wordcounts[word]=1

def replacepunctions(line):
    for ch in line:
        if ch in '~@#$%^&*()_-+=?<>/|\{}[]:;''""':
            line=line.replace(ch,' ')
    return line
        
    
    
def main():
    filename=input('enter a filename:').strip()
    infile=open(filename,'r')
    wordcount={}
    for line in infile:
        processline(line.lower(),wordcounts)
    pairs=list(wordcounts.items())
    items.sort()
    
    for i in range(len(item)-1,len(item)-count-1,-1):
        print(item[i][1]+'\t'+str(item[i][0]))
        data.append(item[i][0])
        wrod.append(item[i][1])
    infile.close()
    
    turtle.title('frequency statistics')
    turtle.setup(900,700,0,0)
    t=turtle.Turtle()
    t.hideturtle()
    t.width(3)
    drawgraph(t)
if __name__=='__main__':
    main()
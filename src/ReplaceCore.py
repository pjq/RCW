#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 2010-4-7

@author: Percy.Peng
'''





class StrReplace:
    """
    Used to replace the string with the specified word in the word.list
    """
    wordlistfile = 'word.list'
    wordlist = {}
    
    def __init__(self, file='word.list'):
        print 'init'
        self.wordlistfile = file
        self.createWorldList()
        
    def createWorldList(self):
        """
        Create the world list from file word.list
        """
        print 'create to be Replaced WorldList'
        try:
            file = open(self.wordlistfile, 'rb')  
                      
            for line in file.readlines():
                #print line   
                self.add(line)
                       
            file.close()   
            
            return self.wordlist     
            
        except IOError:
            print 'IOError'
        
        
        
    def replaceFile(self, replacefile='test.txt'):
        """
        Do the core replace job here.
        """
    
        file = open(replacefile, 'rb')
        allcontent = ""
                
        for line in file.readlines():
            line = "%s" % (line)
            allcontent = allcontent + line
               
        #for k, v in self.wordlist.items():
        #    allcontent = allcontent.replace(k, v)  
        
        allcontent = self.replaceStr(text=allcontent)
               
        self.writeFile('out-' + replacefile, allcontent)
        
    def replaceStr(self, text=""):
        """
        Replace the text and return the replaced text
        """
         
        replaced_text = text     
        for k, v in self.wordlist.items():
            #print k, '=', v
            replaced_text = replaced_text.replace(k, v)  
            
        print 'Replaced content:'
        print replaced_text    
        return replaced_text
    
    def recoveryStr(self, text=""):
        """
        Recovery the replaced text.        
        """
        
        recovery_text = text     
        for k, v in self.wordlist.items():
            #print k, '=', v
            recovery_text = recovery_text.replace(v, k)  
            
            
        print 'Recovery content'
        print recovery_text
        return recovery_text   
            
        
    def add(self, line):
        """
        Add a world to the world list
        """
        
        if str(line).strip().__len__() < 2:
            return
        
        l = line.split()
        
        if l.__len__() < 2:
           return 
        
        key = l[0]
        value = l[1:]
        v = ""
        for i in value:
           v = v + i        
        print key, '=', v
        self.wordlist[key] = v
        
    def parseWordList(self, line):
        """
           Parse a line in Word List
        """
        print 'parseWordList'  
        
        l = line.split()
        key = l[0]
        value = l[1:]
        v = ''
        for i in value:
            print i
            v = v + i
        
        #print v    
        return {key:v} 
    
    def writeFile(self, outFile='test_reaplced.txt', tobewrite=''):
        """
        Write the replaced contents to the file
        """
        file = open(outFile, 'w');        
        file.writelines(tobewrite);        
        file.close();
        
    
def test():
        """
        test function
        """
        strReplace = StrReplace('word.list')    
        print strReplace.wordlist['你']
        strReplace.replaceFile('test.txt')

if __name__ == '__main__':    
    print 'main'     
    test();
 
 
 
    
    
    
   
    
 
 
 
 
 
 
 

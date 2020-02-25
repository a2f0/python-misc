#!/usr/bin/env python3

import random

class wildcardPermute(object):
    
    def __init__(self, pattern=None):

        if pattern == None:
            self.pattern = self.generatePattern()
        else:
            self.pattern = pattern
        pass

    def permute(self,s_position,expanded):
        if s_position <  len(self.pattern):
            if self.pattern[s_position] == '?':
                expanded1 = expanded + '1'
                self.permute(s_position+1,expanded1)
                expanded2 = expanded + '0'
                self.permute(s_position+1,expanded2)
            else:
                expanded = expanded + self.pattern[s_position]
                self.permute(s_position+1,expanded)
        else:
            print(expanded)
            return
    
    def generatePattern(self, size=None):
        if size == None:
            size = random.randint(1,10)
        position = 0
        pattern = ''
        while position < size:
            decision = random.randint(1,3)
            if decision == 1:
                pattern = pattern + '0'
            elif decision == 2:
                pattern = pattern + '1'
            else:
                pattern = pattern + '?'
            position+=1
        return pattern

wcp = wildcardPermute()
print('pattern: ' + wcp.pattern)
r = wcp.permute(0,'')
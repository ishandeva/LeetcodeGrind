# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 00:19:14 2022

@author: Ishan
"""

def lengthOfLongestSubstring(str: str) -> int:
       
        # Start/end pointers, dict for seen characters
        length = 1
        start = 0
        end = 0
        seen = {}
        
        # Iterate through string using sliding window
        while end < len(str):
            
            endChar = str[end]
            
            # If our end character has already been seen...
            if endChar in seen:
                # Set our start to the new end plus 1
                #Didn't understand below line
                #or the new start if our last seen "end" char is before our current start)
                start = max(start, seen[endChar] + 1)
                
            # We set the length of our longest known substring w/out repeating characters
            length = max(length, end - start + 1)
                
            # We reset the index we've last seen end char at (or add it, if never seen before)
            seen[endChar] = end
                
            # Expand our window
            end += 1
            
            print(seen)
            print(start, end, length, "\n")
        # Return our longest substring w/ no repeating characters
        return length

print(lengthOfLongestSubstring("pwwkew"))
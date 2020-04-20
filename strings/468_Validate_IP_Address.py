'''
QUESTION
---------
Write a function to check whether an input string is a valid IPv4 address 
or IPv6 address or neither.
IPv4 addresses are canonically represented in dot-decimal notation, 
which consists of four decimal numbers, each ranging from 0 to 255, 
separated by dots ("."), e.g.,172.16.254.1;
Besides, leading zeros in the IPv4 is invalid. For example, the address 
172.16.254.01 is invalid.
IPv6 addresses are represented as eight groups of four hexadecimal digits, 
each group representing 16 bits. The groups are separated by colons (":"). 
For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a 
valid one. Also, we could omit some leading zeros among four hexadecimal 
digits and some low-case characters in the address to upper-case ones, 
so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address(Omit 
leading zeros and using upper cases).
However, we don't replace a consecutive group of zero value with a single 
empty group using two consecutive colons (::) to pursue simplicity. 
For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.
Besides, extra leading zeros in the IPv6 is also invalid. For example, 
the address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.
Note: You may assume there is no extra space or special characters 
in the input string.

Example 1:
Input: "172.16.254.1"

Output: "IPv4"

Explanation: This is a valid IPv4 address, return "IPv4".
Example 2:
Input: "2001:0db8:85a3:0:0:8A2E:0370:7334"

Output: "IPv6"

Explanation: This is a valid IPv6 address, return "IPv6".
Example 3:
Input: "256.256.256.256"

Output: "Neither"

Explanation: This is neither a IPv4 address nor a IPv6 address.

'''

'''
    Solution:
  
  
    # Find whether we're checking ipv4 vs ipv6
    # count periods and colons
    # if both are contained, it's invalid
    # if periods: ipv4
    # if colons: ipv6

    # validation
    
    # IpV4:
        - No.of periods = 3, has four parts four parts
        - the number should be <= 255, >= 0
        - Check for leading zeros;
            - Cast String to Int # do try catch to catch error conversion
            - Cast Int to string
            - If no same, invalid
    
    # IPV6:
        - Has Colons:, has 7 colons
        - Splits into 8 parts
        - try Cast hexa to int(number, base), catch to catch error conversion
        - If length of each part is between 1 to <= 4
        - 65535, max limit 16^4 - 1

    
    Complexity:
      O(N) * 3 for checking if colons are there or not, where N is length of IP string
      O(K) where K is number of parts in the address either 4 or 8 
        O(N) that is incasting of int to string
    
    Total = O(N) where N is number of characters in string.
    
    https://linkedin.com/in/nikshrestha
      

'''


def checkAddress(address):
    if ('.' in address and ':' in address) or '-' in address:
        return 'Neither'
    
    if '.' in address:
        return checkIfValidIPv4(address)
    elif ':' in address:
        return checkIfValidIPv6(address)
        
    return 'Neither'    
    


def checkIfValidIPv4(address):
    parts = address.split('.')
    if len(parts) != 4:
        return 'Neither'
    try:
        for part in parts:
            part_int = int(part)
            if part_int < 256 and part_int >= 0 and str(part_int) == part:
                continue
            else:
                return 'Neither'
    except:
        return 'Neither'
    
    return 'IPv4'
        
            
    
def checkIfValidIPv6(address):
    parts = address.split(':')
    if len(parts) != 8:
        return 'Neither'
    max_limit = 16**4 - 1
    
    try:
        for part in parts:
            part_int = int(part, 16)
            if part_int < max_limit and part_int >= 0 and len(part) <= 4:
                continue
            else:
                return 'Neither'
    except:
        return 'Neither'
        
    return 'IPv6'
                
    






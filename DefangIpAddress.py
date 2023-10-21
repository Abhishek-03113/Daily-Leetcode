"""
@Abhishek 
Day 11 
Topic String 
Problem : Defanging the ip address 
"""

from _typeshed import StrOrLiteralStr


class Solution:
    def defangIPaddr(self, address: str) -> str:
        addr = address.split(".")

        strs = str(addr[0] + "[.]" + addr[1] + "[.]" + addr[2] + "[.]" + addr[3])

        return strs

    def bruteforce(self, address: str) -> str:
        strs = ""
        for i in address:
            if i == ".":
                strs += "[.]"
            else:
                strs += i

            return strs

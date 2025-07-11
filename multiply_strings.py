"""
https://leetcode.com/problems/multiply-strings/
Medium
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
 

Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        product = []
        temp =  []
        original =  []
        c = t = digit = 0

        if (num1 == "0" or num2 == "0"):
            return "0"
        elif (num1 == "1"):
            return num2
        elif (num2 == "1"):
            return num1

        for n in num1:
            original.append(n)

        for j in num2[::-1]:
            digit += 1
            temp = []
            
            c = 0

            if (j == "0"):
                temp = ["0"]
            elif (j == "1"):
                temp = original[:]
            else:
                for i in num1[::-1]:
                    t = c + int(i) * int(j)
                    c = 0
                    while (t >= 10):
                        c += 1
                        t -= 10
                    temp.insert(0, str(t))

                while(c > 0):
                    temp.insert(0, str(c))
                    c -= 10

            if len(product) == 0:
                product = temp[:]
            else:
                for k in range(digit - 1):
                    temp.append("0")
                    
                while(len(product) < len(temp)):
                    product.insert(0, "0")

                c = 0
                k = len(temp) - 1

                while (k >= 0):
                    t = c + int(temp[k]) + int(product[k])
                    c = 0
                    while (t >= 10):
                        c += 1
                        t -= 10
                    product[k] = str(t)
                    k -= 1

                while(c > 0):
                    product.insert(0, str(c))
                    c -= 10

        return "".join(product)
                
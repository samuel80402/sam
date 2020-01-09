# leetcode刷題記錄
以下記錄了我在leetcode挑選的5題的作答簡略過程

## Two Sum
這題的目的是給定一個目標值，從list中找出相加等於目標值的兩個元素，並回傳對應的index值。我用的方法是使用兩個迴圈包起來，讓程式判斷兩兩相加的值等於target，再回傳index值。
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
```
## Reverse Integer
這題的題目是給定一個數值，回傳倒轉過的該數值，我參考了 [如何倒轉數字](https://www.quora.com/How-can-I-reverse-a-number-using-Python)的方式去做，並修改一下來處理負數的問題。
```python
class Solution:
    def reverse(self, x: int) -> int:
        if x>=0:
            if int(str(x)[::-1]) >= 2**31-1:
                return 0
            else:
                return int(str(x)[::-1])
        else:
            if int(str(x)[0]+str(x)[:0:-1])<=-2**31:
                return 0
            else:
                return int(str(x)[0]+str(x)[:0:-1])
```
## Jewels and Stones
這題是給定一組字母為對照組，找出另一組字母中有幾個同樣的字母。由於給的字母組是字串形式，而在尋找的過程中，每個字母都算是單一元素，因此我先把字串換成清單，再由程式去判斷要尋找的那組字母中有多少個字母在對照組，並回傳數量。
```python
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        n=0
        j = list(J)
        s = list(S)
        for i in s:
            if i in j:
                n+=1
        return n
```
## Palindrome Number
這題是看數字轉成字串之後，倒轉過來後是不是跟原本的組成順序一樣，並回傳True or False。這題沿用我在倒轉數字的程式碼所學到的方式作為條件判斷。
```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False
```
## Squares of a Sorted
這題的目的是把原本List的數字平方之後再排序輸出，所以我用了簡單的方式先平方再排序。
```python
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        answer = []
        for i in A:
            answer.append(i**2)
        answer.sort()
        return answer
```

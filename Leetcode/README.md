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
這題的題目是給定一個數值，回傳倒轉過的該數值，我參考了[如何倒轉數字] (https://www.quora.com/How-can-I-reverse-a-number-using-Python)的方式去做，並修改一下來處理負數的問題。
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

## Palindrome Number

## Squares of a Sorted

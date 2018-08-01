Searches a list of numbers and returns the index of the smallest number. The user can choose where to search the list, i.e. from index 0 to 2, or index 1 to 6 etc.
Uses an interval tree to search the list.

this is the tree with the list [25, 24, 5, 20, 7, 4, 30]
![tree](https://user-images.githubusercontent.com/40809349/43552195-a0229ac0-95b7-11e8-8bf0-816307625335.PNG)

To use open q1.py and in the if __name__ == '__main__' section put the list you want to search in the IntervalTree function parameters, then indicate which part of the list you want to seach using indices in the min_in_range parameters.
The program then prints out the index of the smallest number.

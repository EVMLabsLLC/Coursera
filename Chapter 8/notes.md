List is a colection
Square brakets for lists:
`frineds = [ 'Joseph', 'Glenn', 'Sally']` 

List constants
anything in square bracket
you can have lists that include lists i.e.
`my_list = ['red', ['1', '2'], '24']`

`in` means for each item in a list i.e.

```
friends = [ 'Joseph', 'Glenn', 'Sally']
for friend in friends :
    print('Happy New Year:', friend)
print('Done!')
```
In the example above, `friend` is the variable we assign to each item `in` the list

Stings are immutable, we can make copies i.e.

```
>>> fruit = 'Banana'
>>> fruit[0] = 'b'
```
What we are trying to do above, is change the character in the 0 place "B" to a lowercase
becuase this is a string, we cannot change it. We will need to make a copy with the updated casing i.e.

```
>>> x = fruit.lower()
```
this will return `banana`

List are mutable, meaning they can be changed. i.e.

```
>>> list = [2, 14, 26, 41, 63]
>>> print(list)
[2, 14, 26, 41, 63]
>>> list[2] = 28
>>> print(list)
[2, 14, 28, 41, 63]
```

In the example above, we are able to change the value of `14` in the 2 postion

Use `len()` to get the length 
`range` returs the list up to a point i.e. 0 up to but not including
```
>>> print(range(4))
[0, 1, 2, 3]
>>> frineds = ['Joseph', 'Glenn', 'Sally']
>>>print(len(friends))
3
>>>print(list(range(len(friends))))
[0, 1, 2]
```
Fist we print a range of 4
Second, we lint the length of the list, in this case we have 3 names so the len = 3
Third, we print a list showing the range value, 0, 1, 2

Splicing lists
`[1:4]` - remember the second number is up to, but not including. i.e.

```
>>> num = [9, 41, 12, 3, 74, 15]
>>> num[1:3]
[41,12]
>>> num[:4]
[9, 41, 12, 3]
>>> num[3:]
[3, 74, 15]
>>> num[:]
[9, 41, 12, 3, 74, 15]
```
First, we start with position 1, which in the list is 41, then go to position 2, because we are actually saying [1:3] up to but not including position
Second, we start at the beginning of the list (positions 0) because we didnt define a starting point, and go to position 4
Third, we start at postion 3 and read the entire list after because we didnt set an ending point
Finally, we read the whole list because no points are defined

Lists and Strings

`split` takes a string and returns a list i.e.

```
>>> string = 'With three words'
>>> list = string.split()
>>> print(list)
['With', 'three', 'words']
>>> print(len(list))
3
>>> print(list[0])
With
```

First we set a string "With three words"
Second, we use `split` to split the sting into a list
Third, we get the length of the list using `len` which shows 3 i.e. 0, 1, 2
Finally, we print the first postion of the list which is With

You can tell split to split on a different character i.e. `line.split(';')` will look for ; and split there each time

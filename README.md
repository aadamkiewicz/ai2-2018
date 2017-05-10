# ai2-2017
## STRING 1. 
```
donuts
 OK  got: 'Number of donuts: 4' expected: 'Number of donuts: 4'
 OK  got: 'Number of donuts: 9' expected: 'Number of donuts: 9'
  X  got: 'Number of donuts: 10' expected: 'Number of donuts: many'
 OK  got: 'Number of donuts: many' expected: 'Number of donuts: many'
both_ends
 OK  got: 'spng' expected: 'spng'
 OK  got: 'Helo' expected: 'Helo'
 OK  got: '' expected: ''
 OK  got: 'xyyz' expected: 'xyyz'
fix_start
  X  got: 'babble' expected: 'ba**le'
  X  got: 'aardvark' expected: 'a*rdv*rk'
  X  got: 'google' expected: 'goo*le'
 OK  got: 'donut' expected: 'donut'
mix_up
 OK  got: 'pox mid' expected: 'pox mid'
 OK  got: 'dig donner' expected: 'dig donner'
 OK  got: 'spash gnort' expected: 'spash gnort'
 OK  got: 'fizzy perm' expected: 'fizzy perm'
```
## STRING 2.
```
verbing
 OK  got: 'hailing' expected: 'hailing'
 OK  got: 'swimingly' expected: 'swimingly'
 OK  got: 'do' expected: 'do'
not_bad
 OK  got: 'This movie is good' expected: 'This movie is good'
 OK  got: 'This dinner is good!' expected: 'This dinner is good!'
 OK  got: 'This tea is not hot' expected: 'This tea is not hot'
 OK  got: "It's bad yet not" expected: "It's bad yet not"
front_back
 OK  got: 'abxcdy' expected: 'abxcdy'
 OK  got: 'abcxydez' expected: 'abcxydez'
 OK  got: 'KitDontenut' expected: 'KitDontenut'
```

## LIST 1.
```
match_ends
 OK  got: 3 expected: 3
 OK  got: 2 expected: 2
 OK  got: 1 expected: 1
front_x
 OK  got: ['xaa', 'xzz', 'axx', 'bbb', 'ccc'] expected: ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
 OK  got: ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'] expected: ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
 OK  got: ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'] expected: ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
sort_last
  X  got: None expected: [(2, 1), (3, 2), (1, 3)]
  X  got: None expected: [(3, 1), (1, 2), (2, 3)]
  X  got: None expected: [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
LIST2.
remove_adjacent
 OK  got: [1, 2, 3] expected: [1, 2, 3]
 OK  got: [2, 3] expected: [2, 3]
 OK  got: [] expected: []
linear_merge
 OK  got: ['aa', 'bb', 'cc', 'xx', 'zz'] expected: ['aa', 'bb', 'cc', 'xx', 'zz']
 OK  got: ['aa', 'bb', 'cc', 'xx', 'zz'] expected: ['aa', 'bb', 'cc', 'xx', 'zz']
 OK  got: ['aa', 'aa', 'aa', 'bb', 'bb'] expected: ['aa', 'aa', 'aa', 'bb', 'bb']
```
---------------------------------------------------------------------------------------
## WARMUP
```
Hello, world!
  |  |  
--------
  |  |  
--------
  |  |  
--+--+--H--+--+--H--+--+--
  |  |  H  |  |  H  |  |  
--+--+--H--+--+--H--+--+--
  |  |  H  |  |  H  |  |  
--+--+--H--+--+--H--+--+--
========+========+========
--+--+--H--+--+--H--+--+--
  |  |  H  |  |  H  |  |  
--+--+--H--+--+--H--+--+--
  |  |  H  |  |  H  |  |  
--+--+--H--+--+--H--+--+--
========+========+========
--+--+--H--+--+--H--+--+--
  |  |  H  |  |  H  |  |  
--+--+--H--+--+--H--+--+--
  |  |  H  |  |  H  |  |  
--+--+--H--+--+--H--+--+--

0 3 5 6 9 10 12 15 18 20 21 24 25 27 30 33 35 36 39 40 42 45 48 50 51 54 55 57 60 63 65 66 69 70 72 75 78 80 81 84 85 87 90 93 95 96 99 100 102 105 108 110 111 114 115 117 120 123 125 126 129 130 132 135 138 140 141 144 145 147 150 153 155 156 159 160 162 165 168 170 171 174 175 177 180 183 185 186 189 190 192 195 198 200 201 204 205 207 210 213 215 216 219 220 222 225 228 230 231 234 235 237 240 243 245 246 249 250 252 255 258 260 261 264 265 267 270 273 275 276 279 280 282 285 288 290 291 294 295 297 300 303 305 306 309 310 312 315 318 320 321 324 325 327 330 333 335 336 339 340 342 345 348 350 351 354 355 357 360 363 365 366 369 370 372 375 378 380 381 384 385 387 390 393 395 396 399 400 402 405 408 410 411 414 415 417 420 423 425 426 429 430 432 435 438 440 441 444 445 447 450 453 455 456 459 460 462 465 468 470 471 474 475 477 480 483 485 486 489 490 492 495 498 500 501 504 505 507 510 513 515 516 519 520 522 525 528 530 531 534 535 537 540 543 545 546 549 550 552 555 558 560 561 564 565 567 570 573 575 576 579 580 582 585 588 590 591 594 595 597 600 603 605 606 609 610 612 615 618 620 621 624 625 627 630 633 635 636 639 640 642 645 648 650 651 654 655 657 660 663 665 666 669 670 672 675 678 680 681 684 685 687 690 693 695 696 699 700 702 705 708 710 711 714 715 717 720 723 725 726 729 730 732 735 738 740 741 744 745 747 750 753 755 756 759 760 762 765 768 770 771 774 775 777 780 783 785 786 789 790 792 795 798 800 801 804 805 807 810 813 815 816 819 820 822 825 828 830 831 834 835 837 840 843 845 846 849 850 852 855 858 860 861 864 865 867 870 873 875 876 879 880 882 885 888 890 891 894 895 897 900 903 905 906 909 910 912 915 918 920 921 924 925 927 930 933 935 936 939 940 942 945 948 950 951 954 955 957 960 963 965 966 969 970 972 975 978 980 981 984 985 987 990 993 995 996 999 1000 55 -> 166 -> 83.0 -> 250.0 -> 125.0 -> 376.0 -> 188.0 -> 94.0 -> 47.0 -> 142.0 -> 71.0 -> 214.0 -> 107.0 -> 322.0 -> 161.0 -> 484.0 -> 242.0 -> 121.0 -> 364.0 -> 182.0 -> 91.0 -> 274.0 -> 137.0 -> 412.0 -> 206.0 -> 103.0 -> 310.0 -> 155.0 -> 466.0 -> 233.0 -> 700.0 -> 350.0 -> 175.0 -> 526.0 -> 263.0 -> 790.0 -> 395.0 -> 1186.0 -> 593.0 -> 1780.0 -> 890.0 -> 445.0 -> 1336.0 -> 668.0 -> 334.0 -> 167.0 -> 502.0 -> 251.0 -> 754.0 -> 377.0 -> 1132.0 -> 566.0 -> 283.0 -> 850.0 -> 425.0 -> 1276.0 -> 638.0 -> 319.0 -> 958.0 -> 479.0 -> 1438.0 -> 719.0 -> 2158.0 -> 1079.0 -> 3238.0 -> 1619.0 -> 4858.0 -> 2429.0 -> 7288.0 -> 3644.0 -> 1822.0 -> 911.0 -> 2734.0 -> 1367.0 -> 4102.0 -> 2051.0 -> 6154.0 -> 3077.0 -> 9232.0 -> 4616.0 -> 2308.0 -> 1154.0 -> 577.0 -> 1732.0 -> 866.0 -> 433.0 -> 1300.0 -> 650.0 -> 325.0 -> 976.0 -> 488.0 -> 244.0 -> 122.0 -> 61.0 -> 184.0 -> 92.0 -> 46.0 -> 23.0 -> 70.0 -> 35.0 -> 106.0 -> 53.0 -> 160.0 -> 80.0 -> 40.0 -> 20.0 -> 10.0 -> 5.0 -> 16.0 -> 8.0 -> 4.0 -> 2.0 -> 1.0
Temperature F? 212
It is 100.0 degrees Celsius
Temperature F? 
```
## DATA STRUCTURES
```
def object_reference ():
    s = [0] * 3
    s[0] += 1
    print(s)  

    s = [''] * 3
    s[0] += 'a'
    print(s)  

    s = [[]] * 3
    s[0] += [1]
    print(s)

def gcd(a, b):
      while b:
        a, b = b, a % b
        return a
def flip_dict(d):
    out = {}
    for key, value in d.items():
        if value not in out:
            out[value] = []
        out[value].append(key)
    return out

def comprehension_read():
    print([x for x in [1, 2, 3, 4]])
    print([n - 2 for n in range(10)])
    print([k % 10 for k in range(41) if k % 3 == 0])
    print([s.lower() for s in ['PythOn', 'iS', 'cOoL'] if s[0] < s[-1]])

    arr = [[3,2,1], ['a','b','c'], [('do',), ['re'], 'mi']]
    print([el.append(el[0] * 4) for el in arr])  # => [None, None, None]
    print(arr)

    print([letter for letter in "pYthON" if letter.isupper()])
    print({len(w) for w in ["its", "the", "remix", "to", "ignition"]})
def comprehension_write():
    arr = [0, 1, 2, 3]
    print([2 * num + 1 for num in arr])
    arr = [3, 5, 9, 8]
    print([num % 3 == 0 for num in arr])
    arr = ["TA_sam", "TA_guido", "student_poohbear", "student_htiek"]
    print([name[3:] for name in arr if name.startswith('TA_')]) 
    arr = ['apple', 'orange', 'pear']
    print([fruit[0].upper() for fruit in arr])
    print([fruit for fruit in arr if 'p' in fruit])
    print([(fruit, len(fruit)) for fruit in arr])
    print({fruit:len(fruit) for fruit in arr})

```
## FUNCTIONS
```
def print_two(a, b):
    print("Arguments: {0} and {1}".format(a, b))
    
    print_two(4, 1, b=1)    # invalid,  multiple values for 'b'
    print_two(1, a=1)       # invalid,  multiple values for 'a'
    print_two(b=1, a=4)     # valid
    print_two(a=4, b=1)     # valid
    print_two(b=4,1)        # invalid, 
    print_two(4, 1, 1)      # invalid, 3 positional args instead of 2
    print_two(4, a=1)       # invalid,  multiple values for 'a'
    print_two(a=4, 1)       # invalid
    print_two(41)           # invalid
    print_two(4, 1)         # valid 
    print_two()             # invalid

def keyword_args(a, b=1, c='X', d=None):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)

>>> keyword_args(5)
a: 5
b: 1
c: X
d: None
>>> keyword_args(a=5)
a: 5
b: 1
c: X
d: None
>>> keyword_args(5,8)
a: 5
b: 8
c: X
d: None
>>> keyword_args(5,2,c=4)
a: 5
b: 2
c: 4
d: None
>>> keyword_args(5,0,1)
a: 5
b: 0
c: 1
d: None
>>> keyword_args(5,2,d=8,c=4)
a: 5
b: 2
c: 4
d: 8
>>> keyword_args(5,2,0,1," ") --TypeError: keyword_args() takes from 1 to 4 positional arguments but 5 were given
>>> keyword_args(c=7,1) --SyntaxError: positional argument follows keyword argument
>>> keyword_args(c=7,a=1)
a: 1
b: 1
c: 7
d: None
>>> keyword_args(5,2,[],5)
a: 5
b: 2
c: []
d: 5
>>> keyword_args(1,7,e=6) -TypeError: keyword_args() got an unexpected keyword argument 'e'
>>> keyword_args(1,c=7)
a: 1
b: 1
c: 7
d: None
>>> keyword_args(5,2,b=4) - TypeError: keyword_args() got multiple values for argument 'b'


def variadic(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

>>> variadic(2,3,5,7)
Positional: (2, 3, 5, 7)
Keyword: {}
>>> variadic(1,1,n=1)
Positional: (1, 1)
Keyword: {'n': 1}
>>> variadic(n=1,2,3)--SyntaxError: positional argument follows keyword argument
>>> variadic()
Positional: ()
Keyword: {}
>>> variadic(cs="Computer Science", pd="Product Design")
Positional: ()
Keyword: {'cs': 'Computer Science', 'pd': 'Product Design'}
>>> variadic(cs="Coumputer Science", cs="CompSci", cs="CS")-- SyntaxError: keyword argument repeated
>>> variadic(5,8,k=1,swap=2)
Positional: (5, 8)
Keyword: {'k': 1, 'swap': 2}
>>> variadic(8,*[3,4,5],k=1,**{'a':5,'b':'x'})
Positional: (8, 3, 4, 5)
Keyword: {'k': 1, 'a': 5, 'b': 'x'}
>>> variadic(*[8, 3], *[4, 5], k=1, **{'a':5, 'b':'x'})
Positional: (8, 3, 4, 5)
Keyword: {'k': 1, 'a': 5, 'b': 'x'}
>>> variadic(*[3, 4, 5], 8, *(4, 1), k=1, **{'a':5, 'b':'x'})
Positional: (3, 4, 5, 8, 4, 1)
Keyword: {'k': 1, 'a': 5, 'b': 'x'}
>>> variadic({'a':5, 'b':'x'}, *{'a':5, 'b':'x'}, **{'a':5, 'b':'x'})
Positional: ({'a': 5, 'b': 'x'}, 'a', 'b')
Keyword: {'a': 5, 'b': 'x'}

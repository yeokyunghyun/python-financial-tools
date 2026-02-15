import numpy as np
import pandas as pd

a = np.array([1, 2, 3])
print(type(a));

new_list1 = np.array([1, 2, 3]);
new_list2 = np.array([4, 5, 6]);

new_list3 = new_list1 + new_list2;
print(new_list3)

s2 = pd.Series([1, 2, 3, 4])
print(s2, '=================')


s2 = pd.Series([1, 2, 3, 4], index =['a', 'b', 'c', 'd'])
print(s2, '=================')

print("======================")
print(s2.head()) # 최상위 5개만 보여줌 

s3 = pd.Series({'a':1, 'b':2, 'c':3, 'd':4, 'e':5})
print(s3);

s4 = pd.Series([1,1,1, 2, 3, 4, 5, 6, 7, 8, 9, np.nan])
print('test1', s4.unique()) # distinct한 값 추출해서 np.array로 반환 
print(s4.value_counts());

s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
s2 = pd.Series([4, 3, 2, 1], index=['d', 'c', 'b', 'a'])

print('s1 + s2 = ', s1 + s2);

print(s4)
print(len(s4))
print(s4.count())

s1 = np.arange(1, 6, 2)
s2 = np.arange(6, 11, 2)
s3 = pd.DataFrame({'c1':s1, 'c2':s2})

print(s3)

s1 = pd.DataFrame(
    [
        [10, 11],
        [10, 12]
    ]
)

print(s1)

s2 = pd.DataFrame(
    np.array (
        [
            [10, 11, 12, 13],
            [20, 21, 22, 23]
        ]
    )

)

print(s2)

s1 = pd.DataFrame(
    [
        pd.Series(np.arange(10, 15)),
        pd.Series(np.arange(15, 20)),
    ],
    columns=[0, 1, 2, 3, 4],
    index=['r1', 'r2']
)
print(s1)

s2 = pd.DataFrame(
    np.array(
        [
            [10, 11, 12, 13, 14, 15],
            [20, 21, 22, 23 ,24, 25]
        ]
    ),
    columns=['a', 'b', 'c', 'd', 'e', 'f'],
    index=['r1', 'r2']
)

print(s2)


print(np.arange(1, 5))
print(pd.Series(np.arange(1, 9)))

print(np.arange(1,9))
print(pd.Series(np.arange(1,9)))
print(pd.DataFrame(pd.Series(np.arange(1,9))))

my_dict['a'] = 1
df['c4'] = pd.Series([1, 2, 3, 4], index=[0, 1, 2, 10])
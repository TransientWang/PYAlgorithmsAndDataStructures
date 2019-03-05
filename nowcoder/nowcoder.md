小易老师是非常严厉的,它会要求所有学生在进入教室前都排成一列,并且他要求学生按照身高不递减的顺序排列。有一次,n个学生在列队的时候,小易老师正好去卫生间了。学生们终于有机会反击了,于是学生们决定来一次疯狂的队列,他们定义一个队列的疯狂值为每对相邻排列学生身高差的绝对值总和。由于按照身高顺序排列的队列的疯狂值是最小的,他们当然决定按照疯狂值最大的顺序来进行列队。现在给出n个学生的身高,请计算出这些学生列队的最大可能的疯狂值。小易老师回来一定会气得半死。

##### **输入描述:**

```
输入包括两行,第一行一个整数n(1 ≤ n ≤ 50),表示学生的人数
第二行为n个整数h[i](1 ≤ h[i] ≤ 1000),表示每个学生的身高
```

##### **输出描述:**

```
输出一个整数,表示n个学生列队可以获得的最大的疯狂值。

如样例所示: 
当队列排列顺序是: 25-10-40-5-25, 身高差绝对值的总和为15+30+35+20=100。
这是最大的疯狂值了。
```

##### **输入例子1:**

```
5
5 10 25 40 25
```

##### **输出例子1:**

```
100
```

### 解

排序过后，每次挑出最大的和最小的，下次的最大的插入当前最小左边，最小的插入当前最大的右边。如果剩下一个，则和两边都比较，看那边差值大。最后计算结果。

```python
n = int(input())
mlist = list(map(lambda x: int(x), input().split(" ")))
mlist.sort()
l, r = 0, n - 1
res = []
idx = 4
while l < r:
    if idx & 1 ==1:
        res.insert(0, mlist[l])
        res.append(mlist[r])
    else:
        res.insert(0, mlist[r])
        res.append(mlist[l])
    idx += 1
    l += 1
    r -= 1
if n % 2 != 0:
    if abs(mlist[(n - 1) // 2] - res[0]) > abs(mlist[(n - 1) // 2] - res[-1]):
        res.insert(0, mlist[(n - 1) // 2])
    else:
        res.append(mlist[(n - 1) // 2])
last = res[0]
t = 0
for i in res:
    t += abs(i - last)
    last = i
print(t)
```

java：

```java
import java.util.*;

/**
 * @author wangfy
 * @Description TODO
 * @date 2019/3/5
 **/
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (scanner.hasNextInt()) {
            int n = scanner.nextInt();
            int[] list = new int[n];
            for (int k = 0; k < n; k++) {
                list[k] = scanner.nextInt();
            }
            list = Arrays.stream(list).sorted().toArray();
            int l = 0;
            int r = list.length - 1;
            List<Integer> lists = new ArrayList<>();
            int idx = 1;
            while (l < r) {
                if (((idx++) & 1) == 1) {
                    lists.add(0, list[l]);
                    lists.add(list[r]);
                } else {
                    lists.add(0, list[r]);
                    lists.add(list[l]);
                }
                l += 1;
                r -= 1;


            }
            if ((n & 1) == 1) {
                int tmp = list[(n - 1) / 2];
                if (Math.abs(tmp - lists.get(0)) > Math.abs(tmp - lists.get(lists.size() - 1))) {
                    lists.add(0, tmp);
                } else {
                    lists.add(tmp);
                }
            }

            int last = lists.get(0);
            int sum = 0;
            for (int i = 0; i < n; i++) {
                sum += Math.abs(lists.get(i) - last);
                last = lists.get(i);
            }
            System.out.println(sum);
        }
    }
}
```


Notice:

1. Larger dataset only have one chance, and it will expire in 4 minutes. So make sure your code is correct and efficient before submit larger dataset.

2. Some times Google requires you to mod 1000000007 to avoid long result.

2016 A Round

| # | Title | Solution | Basic idea (One line) |
|---| ----- | -------- | --------------------- |
| B | [gcube](https://code.google.com/codejam/contest/4284486/dashboard#s=p1) | [Python]() | |


2017 Pactice

| # | Title | Solution | Basic idea (One line) |
|---| ----- | -------- | --------------------- |
| A | [Lazy Spelling Bee]() | [Python]() | \prod_{i=0}^{n - 1} len(set(i - 1, i, i + 1))|



2017 A Round

| # | Title | Solution | Basic idea (One line) |
|---| ----- | -------- | --------------------- |
| A | [Country Leader](https://code.google.com/codejam/contest/11274486/dashboard#s=p0) | [Python]() | |
| B | [Jane's Flower Shop](https://code.google.com/codejam/contest/11274486/dashboard#s=p1) | [Python]() | Binary search on double |



2017 B Round

| # | Title | Solution | Basic idea (One line) |
|---| ----- | -------- | --------------------- |
| A | [Sherlock and Parentheses](https://code.google.com/codejam/contest/5254487/dashboard#s=p0) | [Python]() | (n + 1) * n / 2 | 
| B | [Sherlock and Watson Gym Secrets](https://code.google.com/codejam/contest/5254487/dashboard#s=p1) | [Python]() | Three optimizations:<br>1. Fast power(x, y) % n<br>2. 0~k-1 buckets<br>3. (i + k)^A % k == i^A % k, so if i satisfies, then i + k, i + 2k.... satisfy condition. |
| C | [Watson and Intervals](https://code.google.com/codejam/contest/5254487/dashboard#s=p2) | [Python]() | l and r interval problem, sort and computer count (add on l, subtract on r). When count == 1, it is a unique interval for current interval. |
| D | [Sherlock and Permutation Sorting](https://code.google.com/codejam/contest/5254487/dashboard#s=p3) | [Python]() | f(n) = n! - \sum f(i)*(n- i)!, then optimize dp from O(n^3) to O(n^2) | 
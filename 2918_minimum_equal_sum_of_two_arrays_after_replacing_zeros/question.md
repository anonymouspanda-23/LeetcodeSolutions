You are given two arrays ```nums1``` and ```nums2``` consisting of positive integers.

You have to replace <b>all</b> the ```0```'s in both arrays with <b>strictly</b> positive integers such that the sum of elements of both arrays becomes <b>equal</b>.

Return <i>the <b>minimum</b> equal sum you can obtain, or ```-1``` if it is impossible</i>.

<b>Example 1:</b><br>
> <b>Input</b>: nums1 = [3,2,0,1,0], nums2 = [6,5,0]<br>
> <b>Output</b>: 12<br>
> <b>Explanation</b>: We can replace 0's in the following way:<br>
> \- Replace the two 0's in nums1 with the values 2 and 4. The resulting array is nums1 = [3,2,2,1,4].<br>
> \- Replace the 0 in nums2 with the value 1. The resulting array is nums2 = [6,5,1].<br>
> Both arrays have an equal sum of 12. It can be shown that it is the minimum sum we can obtain.

<b>Example 2:</b><br>
> <b>Input</b>: nums1 = [2,0,2,0], nums2 = [1,4]<br>
> <b>Output</b>: -1
> <b>Explanation</b>: It is impossible to make the sum of both arrays equal.

<b>Constraints<b>:
<ul>
<li>
<code>
1 <= nums1.length, nums2.length <= 10<sup>5</sup>
</code>
</li>
<li>
<code>
0 <= nums1[i], nums2[i] <= 10<sup>6</sup>
</code>
</li>
</ul>
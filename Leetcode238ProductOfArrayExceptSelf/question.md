Given an integer array ```nums```, return <i>an array ```answer``` such that ```answer[i]``` is equal to the product of all the elements of ```nums``` except ```nums[i]```.</i>

The product of any prefix or suffix of ```nums``` is <b>guaranteed</b> to fit in a <b>32-bit</b> integer.

You must write an algorithm that runs in ```O(n)``` time and without using the division operation.


<b>Example 1:</b>

<pre>
<b>Input:</b> nums = [1,2,3,4]
<b>Output:</b> [24,12,8,6]
</pre>

<b>Example 2:</b>

<pre>
<b>Input:</b> nums = [-1,1,0,-3,3]
<b>Output:</b> [0,0,9,0,0]
</pre>


<b>Constraints:</b>

<ul>
    <li><code>2 <= nums.length <= 10<sup>5</sup></code></li>
    <li><code>-30 <= nums[i] <= 30</code></li>
    <li>The product of any prefix or suffix of <code>nums</code> is <b>guaranteed</b> to fit into a <b>32-bit</b> integer.</li>
</ul>


<b>Follow up:</b> Can you solve the problem in ```O(1)``` extra space complexity? (The output array <b>does not</b> count as extra space for space complexity analysis.)
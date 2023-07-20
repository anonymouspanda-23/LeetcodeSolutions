Given an integer array <code>nums</code> and an integer <code>k</code>, return <i>the</i> <code>k</code> <i>most frequent elements</i>. You may return your answer in <b> any order</b>.

<b>Example 1:</b>

<pre>
    <b>Input:</b> nums = [1, 1, 1, 2, 2, 3], k = 2
    <b>Output:</b> [1, 2]
</pre>

<b>Example 2:</b>

<pre>
    <b>Input:</b> nums = [1], k = 1
    <b>Output:</b> [1]
</pre>


<b>Constraints:</b>

<ul>
    <li><code>1 <= nums.length <= 10<sup>5</sup></code></li>
    <li><code>-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup></code></li>
    <li><code>k</code> is in the range <code>[1, the number of unique elements in the array]</code>.</li>
    <li>It is <b>guaranteed</b> that the answer is <b>unique</b>.</li>
</ul>
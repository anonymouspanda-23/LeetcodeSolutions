Given an array of integers ```nums``` and an integer ```target```, return <i>indices of the two numbers such that they add up to</i> ```target```.

You may assume that each input would have <b><i>exactly</i> one solution</b>, and you may not use the same element twice.

You can return the answer in any order.

 

<b>Example 1:</b>

<pre>
    <b>Input:</b> nums = [2,7,11,15], target = 9
    <b>Output:</b> [0,1]
    <b>Explanation:</b> Because nums[0] + nums[1] == 9, we return [0, 1].
</pre>

<b>Example 2:</b>

<pre>
    <b>Input:</b> nums = [3,2,4], target = 6
    <b>Output:</b> [1,2]
</pre>

<b>Example 3:</b>

<pre>
    <b>Input:</b> nums = [3,3], target = 6
    <b>Output:</b> [0,1]
</pre>

<b>Constraints:</b>

<ul>
    <li><code>2 <= nums.length <= 10<sup>4</sup></code></li>
    <li><code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code></li>
    <li><code>-10<sup>9</sup> <= target <= 10<sup>9</sup></code></li>
    <li>Only one valid answer exists.</li>
</ul>


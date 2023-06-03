Given an array of strings ```strs```, group <b>the anagrams</b> together. You can return the answer in <b>any order</b>.

An <b>anagram</b> is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

<b>Example 1:</b>

<pre>
<b>Input:</b> strs = ["eat","tea","tan","ate","nat","bat"]
<b>Output:</b> [["bat"],["nat","tan"],["ate","eat","tea"]]
</pre>

<b>Example 2:</b>

<pre>
<b>Input:</b> strs = [""]
<b>Output:</b> [[""]]
</pre>

<b>Example 3:</b>

<pre>
<b>Input:</b> strs = ["a"]
<b>Output:</b> [["a"]]
</pre>


<b>Constraints:</b>

<ul>
    <li><code>1 <= strs.length <= 10<sup>4</sup></code></li>
    <li><code>0 <= strs[i].length <= 100</code></li>
    <li><code>strs[i]</code> consists of lowercase English letters.</li>
</ul>


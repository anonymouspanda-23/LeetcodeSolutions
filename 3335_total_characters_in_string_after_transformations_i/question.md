You are given a string ```s``` and an integer ```t```, representing the number of <b>transformations</b> to perform. In one <b>transformation</b>, every character in ```s``` is replaced according to the following rules:

<ul>
<li>
If the character is <code>'z'</code>, replace it with the string <code>"ab"</code>.
</li>
<li>
Otherwise, replace it with the <b>next</b> character in the alphabet. For example. <code>'a'</code> is replaced with <code>'b'</code>, <code>'b'</code> is replaced with <code>'c'</code>, and so on.
</li>
</ul>

Return the <b>length</b> of the resulting string after <b>exactly</b> ```t``` transformations.

Since the answer may be very large, return it <b>modulo</b> <code>10<sup>9</sup> + 7</code>.

<b>Example 1</b>:
> <b>Input</b>: s = "abcyy", t = 2
> 
> <b>Output</b>: 7
> 
> <b>Explanation</b>:
> <ul>
> <li>
> <b>First Transformation (t = 1):</b>
> </li>
> <ul>
> <li>
> <code>'a'</code> becomes <code>'b'</code>
> </li>
> <li>
> <code>'b'</code> becomes <code>'c'</code>
> </li>
> <li>
> <code>'c'</code> becomes <code>'d'</code>
> </li>
> <li>
> <code>'y'</code> becomes <code>'z'</code>
> </li>
> <li>
> <code>'y'</code> becomes <code>'z'</code>
> </li>
> <li>
> String after the first transformation: <code>"bcdzz"</code>
> </li>
> </ul>
> <li>
> <b>Second Transformation (t = 2):</b>
> </li>
> <ul>
> <li>
> <code>'b'</code> becomes <code>'c'</code>
> </li>
> <li>
> <code>'c'</code> becomes <code>'d'</code>
> </li>
> <li>
> <code>'d'</code> becomes <code>'e'</code>
> </li>
> <li>
> <code>'z'</code> becomes <code>"ab"</code>
> </li>
> <li>
> <code>'z'</code> becomes <code>"ab"</code>
> </li>
> <li>
> String after the second transformation: <code>"cdeabab"</code>
> </li>
> </ul>
> <li>
> <b>Final Length of the String:</b> The string is <code>"cdeabab"</code>, which has 7 characters.
> </li>
> </ul>

<b>Example 2</b>:
> <b>Input</b>: s = "azbk", t = 1
> 
> <b>Output</b>: 5
> 
> <b>Explanation</b>:
> <ul>
> <li>
> <b>First Transformation (t = 1):</b>
> </li>
> <ul>
> <li>
> <code>'a'</code> becomes <code>'b'</code>
> </li>
> <li>
> <code>'z'</code> becomes <code>"ab"</code>
> </li>
> <li>
> <code>'b'</code> becomes <code>'c'</code>
> </li>
> <li>
> <code>'k'</code> becomes <code>'l'</code>
> </li>
> <li>
> String after the first transformation: <code>"babcl"</code>
> </li>
> </ul>
> <li>
> <b>Final Length of the string:</b> The string is <code>"babcl"</code>, which has 5 characters.
> </li>
> </ul>

<b>Constraints</b>:
<ul>
<li>
<code>
1 <= s.length <= 10<sup>5</sup>
</code>
</li>
<li>
<code>s</code> consists only of lowercase English letters.
</li>
<li>
<code>
1 <= t <= 10<sup>5</sup>
</code>
</li>
</ul>
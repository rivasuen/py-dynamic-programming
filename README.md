<h1>Dynamic Programming Practice(Python)</h1>
Learning Source: https://www.youtube.com/watch?v=oBt53YbR9Kk

<h3>Examples</h3>
<ol>
<li>fib</li>
<li>gridTraveler</li>
<li>canSum, howSum, bestSum</li>
<li>canConstruct, countConstrust, allConstruct</li>
</ol>

<h3>Memoization Recipe</h2>
<ol>
  <li>
    Make it work
    <ul>
      <li>visualize the problem as a tree</li>
      <li>implement the tree using recursion</li>
      <li>test it</li>
    </ul>
  </li>
  <li>
    Make it efficient
    <ul>
      <li>add a memo object</li>
      <li>add a base case to return memo values</li>
      <li>store return values into the memo</li>
    </ul>
  </li>
</ol>

<h3>Tabulation Recipe</h2>
    <ul>
      <li>visualize the problem as a table</li>
      <li>size the table based on the inputs</li>
      <li>initialize the table with default values</li>
      <li>seed the trivial answer into the table</li>
      <li>iterate through the table</li>
      <li>fill further positions based on the current position</li>
    </ul>

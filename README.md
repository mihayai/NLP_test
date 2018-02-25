# NLP_test
test for NLP course for Projector
I checked 
https://github.com/mbr/asciitree
the word 'trees' is in the parensis

for 
(asciitree (sometimes you) (just (want to draw)) (**_trees_**) (in (your terminal)))

result is
<code>
- asciitree
- +--&nbsp;sometimes
- |&nbsp;&nbsp;&nbsp;+--&nbsp;you
- +--&nbsp;just
- |&nbsp;&nbsp;&nbsp;+-- want
- |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+-- to
- |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+-- draw
- +--&nbsp;trees
- +--&nbsp;in
- |&nbsp;&nbsp;&nbsp;+--&nbsp;your
- |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+--&nbsp;terminal
</code>
and when the word "trees" is not in the parensis. (The word "trees" and "asciitree" are on the same level) 
(asciitree (sometimes you) (just (want to draw)) **trees** (in (your terminal)))

- asciitree
- +--&nbsp;sometimes
- |&nbsp;&nbsp;&nbsp;+--&nbsp;you
- +--&nbsp;just
- |&nbsp;&nbsp;&nbsp;+--&nbsp;want
- |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+--&nbsp;to
- |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+--&nbsp;draw
- trees
- +--&nbsp;in
- |&nbsp;&nbsp;&nbsp;+--&nbsp;your
- |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+--&nbsp;terminal

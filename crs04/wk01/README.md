# University of Illinois Data Mining Specialization
## Course 4: Pattern Discovery in Data Mining
*2018-04-22 to 29 - Week 01*

### Programming Assignment

> In this programming assignment, you are required to implement the Apriori algorithm and apply it to mine frequent itemsets from a real-life data set.

#### Input

* Text file "categories.txt"
    * Categories for 77,185 places in the United States
    * One row per location with a seim-colon delimited list of applicable categories
    * Example: `Breakfast & Brunch;American (Traditional);Restaurants`
* Saved first 100 rows to "categories-head-100.txt" to speed development

#### Output

Implement the **Apriori** mining algorithm in any programming language (Python). Once working, mine with a *minimum support of 0.01*. Output in two parts:

1) All length-1 frequent categories with their *absolute* support
    1) One row per (absolute support count, frequent category) pair
    2) Use colon delimiter, e.g.: `3000:Fast Food`
    3) Save as text file "patterns.txt"
2) All frequent category sets with their *absolute* support
    1) One row per (absolute support count, frequent category set) pair
    2) Delimit categories by semi-colon, e.g.: `2851:Fast Food;Restaurants`
    3) Programmatic grader will *not* consider order of cateories in sets
    4) Save as text file "patterns.text"

#### Grade

100% after two attempts, the first to with just part 1 (passed) and second with parts 1 and 2.

#### Comments

I could write a better implementation of the Apriori algorithm. My method to determine next possible word sets to check for support includes more sets than will pass. However, I think a perfect 'next word sets to check' risks taking more processing time than checking more a few more sets than will pass. Not adept enough at analyzing algorithms to say with certainty.

Also, the Apriori algorithm sucks! Both processing time and memory have O(2<sup>n</sup>). Will try the FP Growth algorithm if I find time.
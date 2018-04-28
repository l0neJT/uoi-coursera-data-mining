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
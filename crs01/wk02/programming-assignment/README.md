# University of Illinois Data Mining Specialization
## Course 01: Data Visualization
*2018-04-30 to 2018-05-06 - Week 02*

### Programming Assignment

> This assignment will give you a chance to explore the topics covered in Week 2 of the course by visualizing some data as a chart. The [data set we provided](gis-temperatures) deals with world temperatures and comes from NASA. Alternatively you can use any data that you would like to explore. You are not required to use D3.js, but if you would like to, we have provided some helpful resources that will make it easier for you to create a visualization. You are welcome to use the [additional resources](https://www.coursera.org/learn/datavisualization/supplement/ijZAO/resources), especially if you do not want to program to complete this project.

#### Instructions

1. Take the data from the [GISTEMP site](gis-temperatures), specifically the data from “Table Data: Global and Hemispheric Monthly Means and Zonal Annual Means.”
2. Parse the data to a suitable format for the tools that you are using
    1. Course provided two files (in JS, TXT, and CSV formats)
    2. Subset of the data on the GISTEMP site
3. Visualize the data to meet the requirements of the [Programming Assignment 1 Rubric](#grading-rubric)
Click below to download the .zip file for this programming assignment.

#### Grading Rubric

| Criteria | Poor (1–2 points) | Fair (3 points) | Good (4 points) | Great (5 points) |
| --- | --- | --- | --- | --- | --- |
| *Appropriate Chart Selection and Variables* | Chart is indecipherable or significantly misleading because of poor chart type or assignment of variables to elements | Major problem(s) with chart selection or assignment of elements to variables | Minor problem(s) with chart selection or assignment of elements to variables | Chart selection is appropriate for data and its elements properly assigned to appropriate data variables |
| *Design of the Chart*<sup>1</sup> | No apparent attention paid to design | Evidence that several of the design rules should have been followed but were not | Evidence that one of the design rules should have been followed but was not | Attention paid to all design rules |
| *Contest*<sup>2</sup> | Misleading | Boring | Not boring | Interesting |

<sup>1</sup>Does the chart effectively display the data, based on the design rules in lecture 2.3.1?<br>
<sup>2</sup>How interesting is the result? Does this represent an interesting choice of data and/or an interesting way to display the data? For example, was a streamgraph used instead of an ordinary bar chart?

#### Input

> The following are plain-text files in tabular format of temperature anomalies, i.e. deviations from the corresponding 1951-1980 means.

* Global-mean monthly, seasonal, and annual mean
    * Files beginning "ExcelFormattedGISTEMPData" (no trailing "2")
    * Rows by year
    * Columns for months and multi-month periods
* GlobalZonal annual means
    * Files beginning "ExcelFormattedGISTEMPData**2**" (with trailing "2")
    * Rows by year
    * Columns for latitudinal regions

#### Output - Planning

Based on lecture 2.1.3, I mapped the data measures to the following graphical elements:

**Global Temperature Variation by Month**

| Measure                 | Calissificaton      | Graphic           |
| ----------------------- | ------------------- | ----------------- |
| Year                    | Ordinal             | Position (x-axis) |
| Month                   | Nominal<sup>1</sup> | Hue               |
| Temperature<sup>2</sup> | Quantitative        | Position (y-axis) |

<sup>1</sup>Might consider as different classificaiton (i.e., ordingal) but not in this context
<sup>2</sup>Difference to mean, by month, from 1951-1980

**Global Temperature Variation by Latitude**

| Measure                 | Calissificaton | Graphic           |
| ----------------------- | -------------- | ----------------- |
| Year                    | Ordinal        | Position (x-axis) |
| Latitudinal Band        | Nominal        | Hue               |
| Temperature<sup>1</sup> | Quantitative   | Position (y-axis) |

<sup>1</sup>Difference to mean, by latitudinal band, from 1951-1980

**Note:** Both datasets have additional measures (e.g., annual, norther vs. southern hemisphere) that I ignored. This both simplified the graphs and kept categories comparable.

#### Grade

*

#### Comments

*


<!--Link Aliases-->
[gis-temperatures]: http://data.giss.nasa.gov/gistemp/
# Quantium starter repo
This repo contains everything you need to get started on the program! Good luck!

## Task 1: Set Up Your Local Development Environment
---

**Here is your task**

1. To begin, get your hands on the starter repo - fork and clone it to your machine: https://github.com/vagabond-systems/quantium-starter-repo. If this step is confusing, read the first two chapters of the Git book linked below.
 
2. Open the project in your IDE of choice — feel free to use any Python IDE you’re comfortable with. If you don’t have a favourite Python IDE yet, look at Pycharm Community Edition. It’s a well-designed IDE by Jetbrains packed with features and plugins, powerful enough to work on the most complex projects, and entirely free.
 
3. One of the best ways to manage dependencies in Python is with virtual environments. Each virtual environment contains a Python interpreter and a collection of project dependencies. They are entirely encapsulated in a single folder, and easy to work with once you get the hang of them. For this project, you will set up a Python 3.9 virtual environment. Review the resources linked below for more information.
 
4. Next, add the dash and pandas packages as dependencies to your virtual environment. Instructions for this step can be found in the Resources section below.
 
5. With your virtual environment active, run `pip install "dash[testing]"` (without backticks) to install all the necessary dash testing dependencies.

Congratulations! You’ve completed the bulk of the work for this task and now have access to a fully-featured workbench. All that’s left is to submit your work. Commit your changes and push them to GitHub!

You’re done! Submit a link to your repo on the next step.
Estimated time for task completion: 30-60 minutes depending on your learning style.
<br>

### Task 1 - Resources

* [Download PyCharm](https://www.jetbrains.com/pycharm/download/#section=linux)
* [Python Virtual Environments: A Primer](https://realpython.com/python-virtual-environments-a-primer/)
* [Dash Installation](https://dash.plotly.com/installation)

**Task 1: Status ✅**

---

## Task 2: Data Processing
---
1. Soul Foods has provided you with three CSV files, all of which are in the data folder of the starter repo you cloned in the last task. These CSV files contain transaction data for Soul Foods’s entire morsel line. Each row indicates the quantity of a given type of morsel sold in a given region at a given price on a given day. Take a moment to acquaint yourself with the data contained in each one of these files.
 
2. Next, we’ll go field by field and think about how we can use each one:
    1. The first field, “product”, contains many different types of morsels. Soul Foods is only interested in Pink Morsels, so we can remove any row which contains another type of product.
    2. Next come “quantity” and “price”. Since we’re interested in the total sales for a given day, these can be combined into a single field, “sales,” by multiplying them together.
    3. The date field is useful as is and can remain untouched.
    4. It would be nice to filter by region in the final visualisation, so we’ll also leave the region field untouched.
 
3. Your task is to use the above instructions to convert the three CSV files into a single formatted output file. Your output file should contain three fields:
    1. Sales
    2. Date
    3. Region
 
4. When you are finished, commit and push your changes, then submit a link to your repo on the next step!.


### Task 2 - Resources

* [CSV File Reading and Writing](https://docs.python.org/3/library/csv.html)
* [Reading and Writing CSV Files in Python](https://realpython.com/python-csv/)

**Task 2 : Status ✅**

---
## Task 3: Create a Dash Application
---
1. Your task is to create a Dash app to visualise the data you generated in the last task. Lean on the resources linked below to learn more about the basics of working with Dash. Your application must incorporate the following elements:
    1. A header which appropriately titles the visualiser
    2. A line chart which visualises the sales data generated in the last task, sorted by date. Be sure to include appropriate axis labels for the chart.
 
2. Recall the original purpose of the Dash app you are building — the goal is to answer Soul Foods’s question: “Were sales higher before or after the Pink Morsel price increase on the 15th of January, 2021?” With the visualiser complete, the answer should be obvious. Congratulations, you just answered a pertinent business question using the awesome power of quantitative data. Soul Foods will be pleased to hear all about it!
 
3. When you are finished, commit and push your changes, then submit a link to your repo on the next step.


### Task 3 - Resources

* [Dash Layout](https://dash.plotly.com/layout)
* [Dash Enterprise App Gallery](https://dash.gallery/Portal/)

**Task 3 : Status ✅**

---
## Task 4: Improve Your Dash Application
---

1. Soul Foods would like a way to dig into region-specific sales data for Pink Morsels. To this end, they’d like a radio button in your visualiser which allows them to filter sales data by region. Leaning on the resources linked below, add a radio button with five options to narrow which data appear in the line chart: “north,” “east,” “south,” “west,” and “all.”
 
2. Now it’s time to dress up your Dash app! Apply some CSS to each element to make your application more visually appealing. There are no requirements for this step other than that you put effort into making your visualiser interesting. The model answer contains an example styling, but the possibilities are infinite — make your visualiser your own!
 
3. When you are finished, commit and push your changes, then submit a link to your repo on the next step.

### Task 4 - Resources

* [Adobe Color Create](https://color.adobe.com/create/color-wheel)
* [Basic Dash Callbacks](https://dash.plotly.com/basic-callbacks)
* [Dash Layout](https://dash.plotly.com/layout)

**Task 4 : Status ✅**

---
## Task 5: Test Your Dash Application
---

1. Your task is to create a test suite to verify your Dash app is working as expected. Using the standard Dash testing framework (documentation linked in the resources below) write three tests which ensure the following:
    1. The header is present.
    2. The visualisation is present.
    3. The region picker is present.
2. Execute your test suite using Pytest and ensure each test passes.
3. Commit and push your changes, then submit a link to your repo below.


### Task 5 - Resources

* [Dash Testing](https://dash.plotly.com/testing)
* [UnitTest](https://martinfowler.com/bliki/UnitTest.html)
* [The Clean Code Blog](https://blog.cleancoder.com/uncle-bob/2017/05/05/TestDefinitions.html)


**Task 5 : Status ✅**

---
## Task 6: Automate Your Test Suite (Bonus Task)
---
Bonus task!
This is an optional bonus task! If you do not wish to complete it, please type N/A into the text field below to finish the program. 

Background information

Continuous integration is the practice of frequently merging the feature branch you are working on with the main branch shared by everyone else working on the same codebase. The goal of continuous integration is to replace large, conflicting merges with smaller, gradual changes. Consider a scenario wherein four developers are working on different parts of the same codebase. This codebase has a main branch, as well as a one-feature branch per developer.

Three of the developers are using a continuous integration workflow. They make small incremental changes, commit them, and merge their feature branches into main several times a day. The fourth developer decides against the practice, creates a feature branch when they start work on their ticket, and does not attempt to merge until a week later when it is complete. Unfortunately, the main branch has changed significantly by the time dev four attempts to merge their feature branch. 

They now must spend a significant amount of time combing through merge conflicts just to merge their feature branch. Needless to say, they don’t have a good time. The three developers using a CI workflow kept their feature branches relatively up to date with main, and as such, spent far less time resolving merge conflicts and more time on the company ping-pong tables.

Furthermore, most CI engines have powerful automated testing and deployment capabilities. In addition to avoiding merge conflicts, the CI engine ensures all tests pass with each commit and can even deploy them to staging environments. As such, developers are instantly made aware that their code behaves as expected when combined with everyone else's. In this task, you will focus on the test automation side of CI — your goal is to make the test you created in the last task executable by a CI engine.

Task instructions

In this task, you will implement a bash script, which automatically runs the test suite you created in the last task. You could integrate this script into a CI engine to allow the test suite to run automatically. The bash script should do the following:

    1. Activate the project virtual environment.
    2. Execute the test suite.
    3. Return exit code 0 if all tests passed, or 1 if something went wrong.
When you’ve finished implementing your bash script, commit and push your changes, then submit a link to your repo below! 


### Task 6 - Resources

* [Continous Integration](https://www.martinfowler.com/articles/continuousIntegration.html)
* [Continous integration Wikipedia](https://en.wikipedia.org/wiki/Continuous_integration)
* [Usage and Invocations](https://docs.pytest.org/en/6.2.x/usage.html)
* [Bash Scripting Tutorial for Beginners](https://linuxconfig.org/bash-scripting-tutorial-for-beginners)
* [Bash Scripting cheatsheet](https://devhints.io/bash)
* [Advanced Bash Scripting](https://tldp.org/LDP/abs/html/)

**Task 6 : Status ✅**
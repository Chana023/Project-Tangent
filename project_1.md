# Project 1 Overview

This project involves parsing a csv file into a different format.

The source data contains several user stories along with associated tasks and
a flag indicating if the task has been completed.

The data is akin to something you might expect when exporting a summary from Azure Devops or similiar sprint planning related apps.

The parsed output data will summarise the source data and save it to a new csv.

# Source Data

The source data contains the following columns:

### User Story
- There are 15 unique user stories

### Task ID 
- Each user story has several tasks
- It is possible that some user stories contain duplicate task ID's. Data from clients is not always perfect.

### Complete
- This is either **yes** or **no** indicating if the task is complete

# Parsed Output Data

The source data should be parsed and output to a new csv with the following columns:

#### User Story
- Each row will be a summary for a specific user story. In other words, since there are 15 user stories in the source data, there will be 15 rows output.

#### All Complete
- This should be **yes** or **no** indicating if all tasks for the user story have been completed.

#### Num Unique Completed Tasks
- How many **unique** tasks have been completed for this story

#### Num Unique Incomplete Tasks
- How many **unique** tasks have not been completed for this task

#### Max Completed Task ID
- What is the maximum task ID for this story which has been completed


## NB:
It is possible that for a certain story/task combination, there exists a **yes**
and a **no**. In these cases, the task should be considered incomplete (ie: **no**)

# Example Source Data

```
User Story      Task ID     Complete
item_1          1           yes
item_2          3           no
item_1          2           yes
item_2          4           yes
item_2          3           yes
item_1          2           yes
```

Given the above source data, the output would be:

```
User Story      All Complete     Num Unique Completed Tasks     Num Unique Incomplete Tasks     Max Completed Task ID
item_1          yes              2                              0                               2
item_2          no               1                              1                               4                 
```

# Tips

- Use GitHub so that I have a place to review your code
- Write clean code that will be logical and readable by other developers
- Use self contained commits as you progress through the project.
- Use feature branches in git and PR's back into main/master

# Bonus

These items are not required. We'll introduce these more in the 2nd project.
Give them a go in this project if you're up to it.

- Add unit tests
- Generate a code coverage report from your tests
- Run your code in a Docker container
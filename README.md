# CMPS 2200  Recitation 01

**Name (Team Member 1):**Blake Anderson
**Name (Team Member 2):**_________________________

In this recitation, we will investigate asymptotic complexity. Additionally, we will get familiar with the various technologies we'll use for recitations and assignments for this semester.

To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.


## Setup
- Login to Github.
- Click on the assignment link posted on canvas and accept the assignment.
- Click on your personal github repository for the assignment (e.g., https://github.com/CMPS2200-Fall2021/recitation-01-your_username).
- [Clone](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) the repository to your local device
- Complete the lab task
- [Add, commit, and push](https://docs.github.com/en/github/managing-files-in-a-repository/managing-files-using-the-command-line/adding-a-file-to-a-repository-using-the-command-line) your completed lab back up to GitHub.
  - You will need to issue `git add` for all files that you have modified, e.g., `main.py`, `README.md`, and any others that you modify as well.
  - For example, on the command line, in the same directory as your cloned lab:
```
$ git add main.py
$ git commit -m "Implement Required Functions"
$ git push origin main
```
## Running and testing your code
- You can run the tests using `pytest`. To install `pytest`, on your terminal:
  + `pip3 install pytest`
  + You may also have to install other python modules such as `tabulate` or other imported modules as you work through these recitations.
- It's usually best to run only one test at a time. To run tests, from the command-line, you can run
  + `pytest -s main.py` will run all tests
  + `pytest -s main.py::test_one` will just run `test_one`
- If you want to run your whole program, make sure to use `python3`. `python` still defaults to python version 2.

## Turning in your work
- You may work with a partner to complete this recitation.
- Only one team member needs to push your completed lab to github.
- In the README.md file, include the names of the team members.

## Comparing search algorithms

We'll compare the running times of `linear_search` and `binary_search` empirically.

- [ ] 1. In `main.py`, the implementation of `linear_search` is already complete. Your task is to implement `binary_search`. Implement a recursive solution using the helper function `_binary_search`.

- [ ] 2. Test that your function is correct by calling from the command-line `pytest main.py::test_binary_search`

- [ ] 3. Write at least two additional test cases in `test_binary_search` and confirm they pass.

- [ ] 4. Describe the worst case input value of `key` for `linear_search`? for `binary_search`?

**
Linear Search: last index of the given list
Binary Search: last, first, or not present in the given list
**

- [ ] 5. Describe the best case input value of `key` for `linear_search`? for `binary_search`?

**
Linear Search: first index of the given list
Binary Search: first MIDDLE element of the given list
**

- [ ] 6. Complete the `time_search` function to compute the running time of a search function. Note that this is an example of a "higher order" function, since one of its parameters is another function.

- [ ] 7. Complete the `compare_search` function to compare the running times of linear search and binary search. Confirm the implementation by running `pytest main.py::test_compare_search`, which contains some simple checks.

- [ ] 8. Call `print_results(compare_search())` and paste the results here:
|        n |   linear |   binary |
|----------|----------|----------|
|       10 |    0.005 |    0.005 |
|      100 |    0.013 |    0.005 |
|     1000 |    0.139 |    0.018 |
|    10000 |    1.344 |    0.016 |
|   100000 |   13.022 |    0.019 |
|  1000000 |  212.485 |    0.044 |
| 10000000 | 2691.093 |    0.041 |


- [ ] 9. The theoretical worst-case running time of linear search is $O(n)$ and binary search is $O(log_2(n))$. Do these theoretical running times match your empirical results? Why or why not?

**No, my results are quicker.  If they did, my times would be far higher.**

- [ ] 10. Binary search assumes the input list is already sorted. Assume it takes $\Theta(n^2)$ time to sort a list of length $n$. Suppose you know ahead of time that you will search the same list $k$ times.
  + What is worst-case complexity of searching a list of $n$ elements $k$ times using linear search? ** O(kn) **
  + For binary search? ** O(k*log_2(n))**
  + For what values of $k$ is it more efficient to first sort and then use binary search versus just using linear search without sorting?
  ** Binary = theta(n^2) + k*log_2(n)
     Linear = kn
     theta(n^2) + k*log_2(n)<kn
     ANSWER:  k > theta(n^2)/(n - log_2(n))
  **

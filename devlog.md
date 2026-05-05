# Python Calculator Programming Journal

## Feb 4th, 2026

1. Decided to make a calculator program, as that can integrate many algorithms.

2. Went to the [recommended](https://docs.python.org/3/library/tkinter.html)
   Tkinter [tutorial](https://tkdocs.com/tutorial/intro.html) to learn how to
   make GUIs.

## Feb 5th, 2026

3. Decided to use GIMP to create sketches (plans) of GUI before implementation.

4. Using [Zed editor](https://zed.dev/) instead of Thonny, as I'm more
   familiar/comfortable using that. (I'm using
   [ty](https://github.com/astral-sh/ty) and
   [Ruff](https://github.com/astral-sh/ruff) LSPs)

5. Decided to pause the tutorial; the first example contains everything I need
   for this project.

6. Found that one grid doesn't do the job; I need a second frame to contain the
   buttons.

7. Searched online to find the Python equivalent of C/C++
   `function.bind(argument)`; it is `partial(function, argument)`,
   `from functools import partial`. (see [GeeksforGeeks article](https://www.geeksforgeeks.org/python/how-to-bind-arguments-to-given-values-in-python-functions/))

8. Skimmed TkDocs, and found that journal entry 6 was wrong; a widget can span
   multiple grid cells using `columnspan` and `rowspan`. Regardless, the design
   I came up with has other advantages; I'm now using a `ttk.Notebook` to allow
   different calculator button sets. (Basic one would be arithmetic.)

9. Tweaked my development environment; `rumdl` for Markdown formatting (this
   journal), and `harper-ls` for spell/grammar checking in Markdown and
   comments.

## Feb 9th or 10th?, 2026

10. Tweaked ruff formatter/linter to be compliant to PEP 8
    (line length 88 -> 79)

11. Decided to use Python's `eval()` to calculate expressions.

## Feb 11th, 2026

12. Reminded myself of core competencies plan; decided that iterating upon this
    calculator project for _all_ the core-competencies would be a good idea.

13. Created/iterated on documentation (Markdown) files, including:
    - `curricular-competencies.md`
    - `README.md`

## Feb 12th, 2026

14. Added factorial function.

## Feb 17th, 2026

15. Added exception handling based on [this](https://www.geeksforgeeks.org/python/define-custom-exceptions-in-python/)

16. Begun GitHub upload process; syncing credentials with GitHub (see
    [this](https://stackoverflow.com/questions/64766508/git-change-users-credentials-in-past-commits-without-changing-the-history-date))

    This is needed because offline username included my real name.

17. Uploaded to GitHub.

## Feb 18th, 2026

18. Researched and found [tutorial by _Real Python_ about unit tests.](https://realpython.com/python-testing/))

19. Teacher assigned to implement a program for solving linear systems.
    [Textbook can be found here](https://github.com/APEXCalculus/Fundamentals-of-Matrix-Algebra-4th-Edition/blob/master/Fundamentals%20of%20Matrix%20Algebra%203rd%20Edition.pdf) (CC-BY-NC license)

20. Thoroughly looked through (and copied) curricular competencies. (not
    present in this repo for licensing reasons)

21. Organized code into separate files

22. Enforced better security on eval call. (see [Real Python's article](https://realpython.com/python-eval-function/))

23. Begun work implementing JSON-based scope definition system. (will be
    committed when usable)

## Feb 19th, 2026

24. Found out how to dynamically import modules from [this article](https://www.pythonmorsels.com/dynamically-importing-modules/)

25. REFLECTION (for Feb 17th-18th)

## Feb 20th, 2026

26. Noted memory state diagram goal.

## Feb 23rd, 2026

27. Begun writing `module_loader.py`.

28. Looked into [reading files](https://www.geeksforgeeks.org/python/how-to-read-from-a-file-in-python/) in Python. (Needed for module loading)

29. Researched [tree traversal](https://www.geeksforgeeks.org/python/tree-traversal-techniques-in-python/) for Python; needed for module loading.
    Decided pre-order traversal to be easiest in this case.

30. Teacher assigned up to textbook section 1.2 to finish before the end of the
    day.

31. Finished; working on 1.3.

32. Decided to find an example in video form for learning Gaussian elimination;
    the textbook isn't doing it for me. Decided to watch [this one](https://www.youtube.com/watch?v=2j5Ic2V7wq4)
    next time; class is ending now.

33. REFLECTION

34. (at home) worked on getting NixOS development environment working.

35. Worked on module loader and begun tree traversal function.

## Feb 24th, 2026

36. Worked on textbook; finished reading through and note-taking Gaussian
    elimination.

37. Added TO-DO file; used for planning improvements to structure and marking
    things to do that are not strictly assigned by teacher.

38. Updated `goals.md`

39. REFLECTION

## Feb 25th, 2026

40. Finished textbook section 1.3, and moving on to 1.4.

41. Confused a little about Reduced Row Echelon Form; looking at [GeeksforGeeks
    article](https://www.geeksforgeeks.org/maths/reduced-row-echelon-form/) for guidance. Figured it out.

42. Started [`gaussian_elimination` sub-project.](subprojects/gaussian_elimination) Creating `Matrix` class.

43. Decided on a documentation standard.

44.5. REFLECTION (forgot to log)

## Feb 26th, 2026

44. Found that [LaTeX expressions are supported in reStructuredText;](https://docs.generic-mapping-tools.org/6.2/rst-cheatsheet.html) I can
    put them in comments.

45. Going through textbook section 1.4; learning about independent vs. dependent
    variables. (Math concept, not programming concept)

## Feb 27th, 2026

46. Learned from textbook about how to tell how many 'solutions' an augmented
    reduced row echelon form matrix has.

47. REFLECTION

## Mar 2nd, 2026

48. Deprioritized code documentation; I'll do it when I have time.

49. Working on Gaussian Elimination function of `Matrix` class.

50. Switched away from a monorepo structure; sub-projects will be linked in
    README.

51. Writing CLI manual testing interface for Matrix class. (Learning
    [user input](https://www.w3schools.com/python/python_user_input.asp))

## Mar 3rd, 2026

52. Worked on matrix class and manual testing interface of matrix class

## Mar 4th, 2026

53. Worked on matrix class manual testing interface.

## Mar 6th, 2026

54. Finished matrix class manual testing interface

55. Working on completing Gaussian Elimination member function

56. REFLECTION

## Mar 23rd, 2026

27. Completed Gaussian Elimination member function

28. Working on solution counter.

## Mar 24th

29. Begun refactoring Matrix class.

30. Begun writing Pytest module.

## Mar 25th

31. Finishing refactoring Matrix class...

32. Learned about [Python property() attribute constructor.](https://docs.python.org/3/library/functions.html#property) ([forum](https://stackoverflow.com/questions/2627002))

33. Learned about @cached_property in Python.

34. Found [suggested way to check whether @cached_property is currently cached.](https://discuss.python.org/t/76667/7)

35. Enabled _most_ linting rules in Ruff and all in ty, for stricter linting.
    - This includes some that necessarily require significant changes to the code:
        - FBT: Disallows booleans as function arguments, to prevent the [boolean
          trap](https://adamj.eu/tech/2021/07/10/python-type-hints-how-to-avoid-the-boolean-trap/)
        - COM812: Requires trailing commas when something is split across
          multiple lines. (reduces git diff size)
        - LOG015: Requires instantiated logger to be used from logger module.
    - The newly enabled rules also provide lots of docstring linting.

## Mar 26th

36. Git Stashed Matrix class refactoring for later; I'd better focus on the tests.

37. Begun porting teacher's tests to work with my `Matrix` class.

38. Finished reading the book about pytest.

## Mar 27th

39. Finished integrating teacher's matrix test with old version of Matrix class.

## Mar 28th

40. Begun writing my own tests by teacher's request.

41. Linted `main.py`.

## Mar 31st

42. Created first test of `test_matrix.py` module; tests
    `matrix.Matrix.__init__()`.

43. Reconfigured Nix environment to inherit `venv`.

44. Configured `ty` environment.

## Apr 1st

45. Refactored existing fixtures and test.

46. Began working on more complex fixtures.

## Apr 2nd

47. Learned about `itertools.chain.from_iterable` from [this SO answer.](https://stackoverflow.com/a/953097)

48. Learned about dynamic type annotations for functions indirectly from the
    function signature of `zip`. Applied it to a function in `test_matrix.py`.
    - This means my use of `typing.Any` is no longer necessary. Adjusted LSP
      rules accordingly.

## Apr 7th

49. Reconfigured development environment for simplicity; replaced `nix develop`
    flake with devenv.

## Apr 8th

50. Found use of RNG in tests better than testing all possible combos.

## Apr 9th

51. Worked on unit reflection.

## Apr 13th

52. Submitted term reflection.

## Apr 15-16th

53. Worked on curriculum plan

## Apr 17th

54. Worked on tests. Got 2/8 created.

## May 4th

55. Remembered about the devlog.

_Backlog:_

56. Finish Matrix class tests
57. Slightly refactored [Gaussian Elimination `main.py` file.](https://github.com/athyfr/py-learning-gaussian-elimination/blob/d7addadf04baa8e337fa1244dd9d4e5eae9395ed/main.py)

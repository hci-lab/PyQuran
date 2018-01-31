Contributing to PyQuran
=======================
We use GitHub issues for reporting bugs and for feature requests.

If you want to give us a hand, you may pick one of the opened issues and solve a bug, implement a feature request
or to suggest a new missing feature.


## Reporting issues

When reporting a bug, use GitHub issue with the **Bug label**, please include  as 
much details as possible about:
- your operating system.
- your python version.
- a self-contained code to reproduce and demonstrate the Bug.

**Issue will be closed if the Bug cannot be reproduced.**


## Feature Request
Whenever you think *PyQuran* is missing a feature, create a GitHub issue with **Feature Request label**,
define what you want precisely and include sufficient examples to cover all the new feature aspects.

If you would like to implement it by yourself, please read the [Contributing Code](#contributing-code) section.



## Contributing Code

_not_completed


### code conventions
Your code have to meet [these standartds](CodeConventions/README.md),
and follow [this style](CodeConventions/example_google.py).


### contributing flow

At first, fork the project [on GitHub](https://github.com/TahaMagdy/PyQuran/),
then, create a *feature branch* and start writing your changes. 
We **DO NOT** accept changes to the *master branch*.

Once you are done, push the changes to *your feature branch*, after that create a *pull request*
with an expressive title and description.

### commit messages

**It is so important to commit properly**, we expect you to commit every one logical change.
A commit message should describe what have been changed, why, and reference issues fixed (if
any). 

**Commit Message Properties**:
1. The Fist line is the commit title, should be less then or equal 50 characters, it must be expressive.
2. Keep the second line blank.
3. Wrap all other lines in the message body at 80 columns.
4. Include `Fixes #N`, where _N_ is the issue number the commit
    fixes, if any.

Commits should look like the following:
```text
explain commit in one line

Body of commit message is a few lines of text, explaining things
in more detail, possibly giving some background about the issue
being fixed, etc.

The body of the commit message **can be several paragraphs**, and
please do proper word-wrap and keep columns shorter than about
80 characters.

Fixes #101
```


## Tests

_not_completed


##  Code Conventions
<br>

> This helps everyone to read and maintain the code **even when they are maintains someone else code**<br>
> *Please restrict to the rules.*

## Rules:
* A line **must not** exceed *80 character* length.
* Use **Spaces** not **Tabs**.
* Always return to `example_google.py` file.



## Naming:
* **Class Name**: [PascalCase](https://en.wikipedia.org/wiki/PascalCase): initial letter is **upper case**
  * *Examples*: `Class, NewClass, ...`
* **Function**: [snake_case](https://en.wikipedia.org/wiki/Snake_case): Lowercase underscore-separated names.
  * *Examples*: `foo, foo_name, ...`
* **Variables**: [lowerCamelCase](https://en.wikipedia.org/wiki/Camel_case): initial letter is **lower case** and rest are PascalCasee.
  * *Examples*: `variable, varibaleName, ...`

## Function prototypes
* Functions should have a description followed by sections as in the following example.
* You don't need to include all section, but include what makes the function as clear as possible.
* **Function prototypes also used for proposed functions**.

```python
def function_with_types_in_docstring(param1, param2):
    """Here you write a  rigorous description of the function
    
    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.
    Returns:
        bool: The return value. True for success, False otherwise.
    Note:
        Do not include the `self` parameter in the ``Args`` section.

    """
```
<br><br>



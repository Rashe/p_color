# Color your print()

Install `p_color` :

```
pip install p_color
```

Usage:

```python
from prcolor import cprint

# by type
cprint.success('Hello world')
cprint.error('Hello world')
cprint.warn('Hello world')

# by color
cprint.green('Hello world')
cprint.yellow('Hello world')
cprint.blue('Hello world')

# bold
cprint.green('Hello <b>World</b>')

# underline
cprint.yellow('Hello, <u>World</u>')
```

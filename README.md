# unichen

**Unit conversion library for Japanese Yen**

# Usage
## unichen
This is a function to convert units. Please use it for analysis of financial statements, etc.
### Inputs (required) 
* `value_unit (str)` - Value before conversion
### Returns
* `res (int)` - Value after conversion

### Example
```python
from unichen import unichen

value_1='130百万円'
value_2 = '130百万'

res_1 = unichen(value_1)
res_2 = unichen(value_2)

# returns
# res_1      : 130000000
# res_1      : 130000000
```

# Requirements
* re
* math

# Installing kawazanyo
```
$ pip install git+https://github.com/yu10kami/unichen
```

# Support
Bugs may be reported at https://github.com/yu10kami/unichen/issues
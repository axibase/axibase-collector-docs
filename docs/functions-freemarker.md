# FreeMarker Functions

## Overview

## Reference

* [column](#column)

### `column`

Retrieves column value for the item from list. [Item Lists](collections.md#item-lists) are defined on the **Collections > Item Lists** page.

```javascript
  ${ITEM?column(column_index)}
```

Retrieves column value by index. The first column index is 0.

```javascript
  ${ITEM?column('column_name')}
```

Retrieves column value by name. To use this function the `Item List` must contains a header row, for example:

```txt
#column_name_1,column_name_2,column_name_3
value1,value2,value3
```

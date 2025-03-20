### **Solution Approach**
We need to implement a **basic SQL-like database** with operations for inserting, deleting, and selecting data from tables.

#### **Key Requirements**
- Each table has a unique name and a fixed number of columns.
- Each inserted row gets an **auto-incremented ID** starting from `1`, which **persists even if rows are deleted**.
- Deleted rows do not affect the ID of the next inserted row.
- **Selecting a value** from a row should be efficient.

---

### **Efficient Data Structures**
1. **Dictionary (`dict`) for table storage**
   - `{table_name: {row_id: row_data}}`
   - Allows quick **insert, delete, and select** operations.

2. **Tracking Auto-Incrementing Row IDs**
   - `{table_name: next_row_id}`
   - Ensures **unique row IDs** for each table.

---

### **Implementation**
```python
class SQL:
    def __init__(self, names: list[str], columns: list[int]):
        # Dictionary to store tables {table_name: {row_id: row_data}}
        self.tables = {name: {} for name in names}
        # Track the next row ID for each table
        self.next_id = {name: 1 for name in names}

    def insertRow(self, name: str, row: list[str]) -> None:
        # Insert the row with auto-incremented ID
        self.tables[name][self.next_id[name]] = row
        self.next_id[name] += 1  # Increment row ID counter

    def deleteRow(self, name: str, rowId: int) -> None:
        # Delete row if exists (does not affect future IDs)
        if rowId in self.tables[name]:
            del self.tables[name][rowId]

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        # Fetch the specific cell value (1-based column index)
        return self.tables[name][rowId][columnId - 1]
```

---

### **Complexity Analysis**
- **Initialization (`__init__`)** → \(O(n)\)
  - Creates tables and initializes the next row ID.
- **Insert (`insertRow`)** → \(O(1)\)
  - Inserts a row using a dictionary lookup.
- **Delete (`deleteRow`)** → \(O(1)\)
  - Removes a row from the dictionary.
- **Select (`selectCell`)** → \(O(1)\)
  - Direct dictionary and list access.

---

### **Example Walkthrough**
```python
sql = SQL(["one", "two", "three"], [2, 3, 1])
sql.insertRow("two", ["first", "second", "third"])  # ID = 1
sql.selectCell("two", 1, 3)  # Returns "third"
sql.insertRow("two", ["fourth", "fifth", "sixth"])  # ID = 2
sql.deleteRow("two", 1)  # Deletes row ID 1
sql.selectCell("two", 2, 2)  # Returns "fifth"
```

---

### **Why This Works Well**
- **Fast operations** using dictionaries.
- **Auto-increment logic** ensures unique row IDs.
- **Deletions do not affect future insertions**.

### **Understanding `deleteRow` and `selectCell` in the `SQL` Class**

This `SQL` class is a **simplified in-memory database** that supports inserting, deleting, and selecting data from tables. Each table stores **rows** using an **auto-incrementing ID**.

---

## **🔹 `deleteRow(self, name: str, rowId: int) -> None`**
### **Purpose:**
Deletes a row from the specified table by its row ID.

### **How It Works:**
```python
def deleteRow(self, name: str, rowId: int) -> None:
    if rowId in self.tables[name]:  # Check if row exists
        del self.tables[name][rowId]  # Remove the row
```
🔹 **Steps:**
1. It **checks if `rowId` exists** in the given table (`self.tables[name]`).
2. If it exists, it **deletes the row** from the dictionary using `del`.
3. **Note:** The deletion **does not affect future row IDs** (i.e., `next_id` is not reset).

### **Example**
#### **Before Deletion:**
```python
tables = {
    "users": {
        1: ["Alice", "25"],
        2: ["Bob", "30"],
        3: ["Charlie", "22"]
    }
}
```
🔹 **Deleting row 2 (`Bob`)**:
```python
deleteRow("users", 2)
```
#### **After Deletion:**
```python
tables = {
    "users": {
        1: ["Alice", "25"],
        3: ["Charlie", "22"]  # Row 2 is removed, but IDs remain unchanged
    }
}
```
✅ **Row 2 is gone, but row IDs are not shifted!**
If a new row is inserted, it will get **ID 4** instead of reusing **ID 2**.

---

## **🔹 `selectCell(self, name: str, rowId: int, columnId: int) -> str`**
### **Purpose:**
Returns the value of a specific cell from a table based on the row ID and column index.

### **How It Works:**
```python
def selectCell(self, name: str, rowId: int, columnId: int) -> str:
    return self.tables[name][rowId][columnId - 1]
```
🔹 **Steps:**
1. Retrieves the **row** from `self.tables[name]` using `rowId`.
2. Retrieves the **specific cell value** using `columnId - 1` (since columns are **1-based**, but Python uses **0-based indexing**).

---

### **Example**
#### **Table (`products`)**
```python
tables = {
    "products": {
        1: ["Laptop", "1000"],
        2: ["Phone", "500"],
        3: ["Tablet", "700"]
    }
}
```
#### **Selecting a Cell**
```python
selectCell("products", 2, 2)  # Fetch the 2nd column of row ID 2
```
🔹 **Steps:**
- `tables["products"][2] → ["Phone", "500"]`
- `columnId - 1 = 2 - 1 = 1` → Selects `"500"`

✅ **Output:** `"500"`

---

## **🔹 Key Takeaways**
| Method | Purpose | Behavior |
|---------|---------|------------|
| **`deleteRow(name, rowId)`** | Deletes a row by ID | IDs are **not shifted** after deletion |
| **`selectCell(name, rowId, columnId)`** | Fetches a cell's value | Uses **1-based column indexing** |

### **Time and Space Complexity Analysis of `SQL` Class Methods**

The `SQL` class acts as an **in-memory table storage system** using **Python dictionaries**. Each table is stored as a dictionary where:

- The **keys** represent row IDs.
- The **values** represent lists of column values.

---

## **1️⃣ `insertRow(self, name: str, row: list[str])`**
### **Time Complexity:**
- **Adding to a dictionary** → \(O(1)\) (since dictionary insertions are average-case \(O(1)\)).
- **Incrementing `next_id`** → \(O(1)\).

✅ **Overall: \(O(1)\) (constant time)**

### **Space Complexity:**
- **Each row takes \(O(c)\) space**, where \(c\) is the number of columns.
- Since we're storing `n` rows, the total space is **\(O(n \cdot c)\)**.

✅ **Overall: \(O(n \cdot c)\) (where \(n\) is the number of rows and \(c\) is columns per row).**

---

## **2️⃣ `deleteRow(self, name: str, rowId: int)`**
### **Time Complexity:**
- **Checking if row exists** → \(O(1)\) (dictionary lookup is \(O(1)\) average case).
- **Deleting a row** → \(O(1)\) (dictionary deletions are average-case \(O(1)\)).

✅ **Overall: \(O(1)\)**.

### **Space Complexity:**
- **No additional space is used**, since it only modifies an existing dictionary.

✅ **Overall: \(O(1)\)**.

---

## **3️⃣ `selectCell(self, name: str, rowId: int, columnId: int) -> str`**
### **Time Complexity:**
- **Dictionary lookup for row** → \(O(1)\) (average case for dictionary access).
- **List index access** → \(O(1)\) (since lists allow direct index-based access).

✅ **Overall: \(O(1)\)**.

### **Space Complexity:**
- **No extra space is used**, just retrieving an existing value.

✅ **Overall: \(O(1)\)**.

---

## **Final Complexity Summary**
| **Method**       | **Time Complexity** | **Space Complexity** |
|------------------|-------------------|-------------------|
| `insertRow()`   | **\(O(1)\)**       | **\(O(n \cdot c)\)** |
| `deleteRow()`   | **\(O(1)\)**       | **\(O(1)\)** |
| `selectCell()`  | **\(O(1)\)**       | **\(O(1)\)** |

### **Conclusion**
- All operations run in **constant time** \(O(1)\), making this implementation **efficient**.
- **Insertions consume memory**, but the space usage is reasonable (\(O(n \cdot c)\)).
- **Deletions do not reclaim space**, but do not increase memory usage.

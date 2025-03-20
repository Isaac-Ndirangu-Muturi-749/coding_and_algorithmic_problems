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

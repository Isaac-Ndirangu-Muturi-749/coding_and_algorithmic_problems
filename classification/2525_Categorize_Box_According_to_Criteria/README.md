To solve this problem, we need to classify the box based on its dimensions and mass according to the given rules. The solution involves simple conditional checks to determine the category of the box.

---

### Algorithm
1. Compute whether the box is **"Bulky"**:
   - Check if any of the dimensions (\( \text{length}, \text{width}, \text{height} \)) is greater than or equal to \( 10^4 \).
   - Compute the volume \( \text{volume} = \text{length} \times \text{width} \times \text{height} \) and check if it is greater than or equal to \( 10^9 \).
2. Check whether the box is **"Heavy"**:
   - If the mass is greater than or equal to \( 100 \), the box is "Heavy".
3. Determine the category:
   - If both "Bulky" and "Heavy", return `"Both"`.
   - If neither "Bulky" nor "Heavy", return `"Neither"`.
   - If only "Bulky", return `"Bulky"`.
   - If only "Heavy", return `"Heavy"`.

---

### Python Code
```python
def categorizeBox(length: int, width: int, height: int, mass: int) -> str:
    # Check "Bulky"
    bulky = length >= 10**4 or width >= 10**4 or height >= 10**4 or (length * width * height) >= 10**9

    # Check "Heavy"
    heavy = mass >= 100

    # Determine the category
    if bulky and heavy:
        return "Both"
    elif bulky:
        return "Bulky"
    elif heavy:
        return "Heavy"
    else:
        return "Neither"
```

---

### Complexity
- **Time Complexity**: \( O(1) \)
  - The calculations for volume and conditional checks are constant time operations.
- **Space Complexity**: \( O(1) \)
  - No additional space is used apart from variables.

---

### Example Runs

#### Example 1
```python
length = 1000
width = 35
height = 700
mass = 300
print(categorizeBox(length, width, height, mass))  # Output: "Heavy"
```
- **Bulky Check**:
  - Dimensions: \( \text{max(length, width, height)} = 1000 < 10^4 \)
  - Volume: \( 1000 \times 35 \times 700 = 24,500,000 < 10^9 \)
  - Not bulky.
- **Heavy Check**: \( 300 \geq 100 \), so "Heavy".
- **Category**: "Heavy".

---

#### Example 2
```python
length = 200
width = 50
height = 800
mass = 50
print(categorizeBox(length, width, height, mass))  # Output: "Neither"
```
- **Bulky Check**:
  - Dimensions: \( \text{max(length, width, height)} = 800 < 10^4 \)
  - Volume: \( 200 \times 50 \times 800 = 8,000,000 < 10^9 \)
  - Not bulky.
- **Heavy Check**: \( 50 < 100 \), so not heavy.
- **Category**: "Neither".

---

#### Example 3
```python
length = 10**5
width = 10
height = 10
mass = 10
print(categorizeBox(length, width, height, mass))  # Output: "Bulky"
```
- **Bulky Check**:
  - Dimensions: \( \text{max(length, width, height)} = 10^5 \geq 10^4 \)
  - Bulky.
- **Heavy Check**: \( 10 < 100 \), so not heavy.
- **Category**: "Bulky".

---

This approach ensures we correctly classify the box in all scenarios with constant time complexity.

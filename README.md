# 🧮 Mean Parser — XFEL Home Test Task

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/)
[![Math Module](https://img.shields.io/badge/Math-Math_Module-green)](https://docs.python.org/3/library/math.html)
[![Sys Module](https://img.shields.io/badge/sys-args-red)](https://docs.python.org/3/library/sys.html)
[![Safe Parsing](https://img.shields.io/badge/Safe_Parsing-ast.literal_eval-orange)](https://docs.python.org/3/library/ast.html)

A Python script that reads lines from a text file and computes their mean values according to specific parsing rules.  
It safely interprets lists or tuples, supports nested structures, filters invalid inputs, and recognizes special values like `NaN`, `inf`, and `-inf`.

---

## ✨ Features

- ✅ Safe parsing using **`ast.literal_eval`** — prevents code execution
- 🔁 Handles **nested lists and tuples** recursively
- 🧹 Cleans string values and replaces commas (`,` → `.`)
- ♾️ Recognizes `"inf"`, `"-inf"`, and `"NaN"` (case-insensitive)
- 🚫 Ignores `None`, `NaN`, empty strings, and invalid values
- 🧮 Returns:
  - Mean of valid numbers
  - `inf` / `-inf` if only infinities present
  - `NaN` if both `inf` and `-inf` appear
  - `None` if no valid values remain

---

## 📂 Repository Structure
  - Script.py # Main Python script
  - test_input.txt # Example input file
  - README.md # Project documentation

---

## **Example Input (`test_input.txt`) and Output**

- [" 1.0 ", "2,5", "NaN", "-INF", 0, 127] → -inf  
- ["", "abc", "3.14"] → 3.14  
- [3, [6, 3], (4, "5.0")] → 4.0  
- ["inf", "-inf", "10"] → nan

---
## Run the Script
- Python script.py test_input.txt


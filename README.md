# functional-treat
# 📊 Data Analyzer and Transformer

## 📖 Project Description

The **Data Analyzer and Transformer** is a menu-driven Python application developed to demonstrate various Python programming concepts. It allows users to input numerical data into a one-dimensional (1D) array and perform different data analysis and transformation operations.

This project showcases the use of built-in functions, user-defined functions, recursion, lambda expressions, sorting, filtering, and returning multiple values from functions.

---

## 🎯 Objectives

- Accept numerical data from the user.
- Analyze the dataset using Python built-in functions.
- Calculate the factorial of a number using recursion.
- Filter data based on a user-defined threshold using a lambda function.
- Sort data in ascending or descending order.
- Display dataset statistics.
- Demonstrate functional programming concepts in Python.

---

## ✨ Features

- 📥 Input numerical data into a 1D array.
- 📊 Display data summary.
- 🔁 Calculate factorial using recursion.
- 🔍 Filter values greater than a threshold.
- 📈 Sort data in ascending or descending order.
- 📋 Display dataset statistics.
- 🚪 Exit the application.

---

## 🧠 Python Concepts Used

### 1. Menu-Driven Programming
The program uses a `while True` loop to repeatedly display the menu until the user chooses to exit.

### 2. User Defined Functions
Functions used in the project include:

- `display_summary()`
- `factorial()`
- `total_sum()`
- `dataset_statistics()`

### 3. Built-in Functions

The following Python built-in functions are used:

- `len()`
- `min()`
- `max()`
- `sum()`
- `sorted()`
- `filter()`
- `float()`
- `input()`
- `print()`

### 4. Recursive Function

The factorial is calculated recursively.

Example:

```
5! = 5 × 4 × 3 × 2 × 1 = 120
```

### 5. Lambda Function

The project uses a lambda function with `filter()` to filter values greater than a threshold.

Example:

```python
filtered_data = list(filter(lambda x: x > threshold, data_list))
```

### 6. Variable Length Arguments (*args)

The project includes an example of `*args`:

```python
def total_sum(*numbers):
    return sum(numbers)
```

### 7. Returning Multiple Values

Functions return multiple values using tuples.

Example:

```python
return total_elements, min_value, max_value, sum_values, average_value
```

---

## 📋 Menu Options

| Option | Description |
|---------|-------------|
| 1 | Input Data |
| 2 | Display Data Summary |
| 3 | Calculate Factorial |
| 4 | Filter Data by Threshold |
| 5 | Sort Data |
| 6 | Display Dataset Statistics |
| 7 | Exit Program |

---

## ▶️ How the Program Works

1. The user enters numerical data separated by spaces.
2. The data is stored as a list of floating-point numbers.
3. The user selects different menu options to perform operations.
4. Results are displayed immediately.
5. The program continues running until Exit is selected.

---

## 💻 Example Run

### Input

```
10 25 35 50 60
```

### Data Summary

```
Total Elements : 5
Minimum Value  : 10
Maximum Value  : 60
Sum            : 180
Average        : 36.0
```

### Filter Example

Threshold:

```
30
```

Output:

```
35.0
50.0
60.0
```

### Sorting

Ascending

```
10.0
25.0
35.0
50.0
60.0
```

Descending

```
60.0
50.0
35.0
25.0
10.0
```

---

## 🛠 Requirements

- Python 3.x
- No external libraries required

---

## 📁 Project Structure

```
Data Analyzer and Transformer/
│
├── functional treat.py
├── README.md
```

---

## 🚀 Future Enhancements

- Add support for 2D arrays.
- Implement exception handling.
- Save data to a file.
- Add graphical charts using Matplotlib.
- Implement **kwargs and global keyword.
- Add proper docstrings for all functions.

---

## 👨‍💻 Author

**Khushboo Variya**

Python Functional Programming Project

---

## 📄 License

This project is developed for educational and learning purposes.

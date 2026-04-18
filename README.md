# Hexadecimal Calculator - TDD Masterclass

Welcome to the official repository for the Hexadecimal Calculator TDD Course! 

In this course, we are building an online calculator application from scratch following the Test-Driven Development (TDD) model. This repository contains the shared solutions for every section of the course.

## Project Goal

To build a web-based calculator that performs basic arithmetic functions (addition, subtraction, multiplication, and division) on a set of hexadecimal numbers. 

### Calculator Constraints

To effectively practice TDD, our calculator must adhere to the following strict functional requirements:

- **Input Limitation:** The calculator will only accept inputs up to 2 digits.
- **Output Limitation:** The calculator will return answers up to a maximum of 4 digits.
- **No Negatives:** The calculator will not return any negative answers.
- **Whole Numbers Only:** The calculator will not return answers with decimal places.

### Calculator Requirements 
| **Category**                        | **Functional Requirements** | **Description / TDD Testing Focus**                                                                                  |
| ----------------------------------- | --------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Inputting and outputting values** | Limitation on input         | The calculator must only accept inputs up to 2 digits.                                                               |
|                                     | Number input confirmation   | Inputs must be valid hexadecimal characters (0-9, A-F).                                                              |
|                                     | Limitation on output        | The calculator must return answers up to a maximum of 4 digits.                                                      |
| **Core Arithmetic Operations**      | Addition                    | The application must successfully add two valid hex numbers.                                                         |
|                                     | Subtraction                 | The application must successfully subtract two valid hex numbers.                                                    |
|                                     | Multiplication              | The application must successfully multiply two valid hex numbers.                                                    |
|                                     | Division                    | The application must successfully divide two valid hex numbers.                                                      |
| **Constraint Handling**             | No negative answers         | The calculator must not return any negative answers (e.g., attempting `05 - 0A` should be handled/prevented).        |
|                                     | No decimal places           | The calculator must not return answers with decimal places (e.g., attempting `05 / 02` should be handled/prevented). |
|                                     | Division by zero            | The calculator must safely handle or reject any attempts to divide by zero.                                          |

## Course Structure & Branches

This course is divided into 4 main sections. We will create specific branches for each section to keep track of our progression and help you navigate the tutorial:

- **[Section 1] Identifying functional requirements and setting up the repository** 
  - *Branch:* `section-1-setup`
- **[Section 2] Writing tests, drafting code** 
  - *Branch:* `section-2-tdd`
- **[Section 3] Testing the GUI (in progress...)** 
  - *Branch:* `section-3-gui` 
- **[Section 4] Porting to containers and cloud services (in progress..)**
  - *Branch:* `section-4-deployment`

## Getting Started (Local Setup)

#### 1. **Clone the repository:**
  ```bash
   git clone [https://github.com/kyle-liebenberg/hex-calculator.git](https://github.com/kyle-liebenberg/hex-calculator.git)
  ```
#### 2. **Create the virtual environment:**
```Bash
python3 -m venv .venv
```
#### 3. **Activate the environment:**
- On macOS/Linux:
```Bash
source .venv/bin/activate
```
- On Windows:
```Bash
.venv\Scripts\activate
```
#### 4. **Install dependencies:**
```Bash
pip install pytest
```

#### 5. **Enter `backend/` directory:**
```bash
pip install pytest
```

#### 6. Run test suite:
```bash
python -m pytest test/
```

---

*Built with ❤️ by Kyle & Diya for IMY 772*

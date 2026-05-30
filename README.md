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
| **Category** | **Functional Requirements** | **Description / TDD Testing Focus** |
| ----------------------------------- | --------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Inputting and outputting values** | Limitation on input         | The calculator must only accept inputs up to 2 digits.                                                               |
|                                     | Number input confirmation   | Inputs must be valid hexadecimal characters (0-9, A-F).                                                              |
|                                     | Limitation on output        | The calculator must return answers up to a maximum of 4 digits.                                                      |
| **Core Arithmetic Operations** | Addition                    | The application must successfully add two valid hex numbers.                                                         |
|                                     | Subtraction                 | The application must successfully subtract two valid hex numbers.                                                    |
|                                     | Multiplication              | The application must successfully multiply two valid hex numbers.                                                    |
|                                     | Division                    | The application must successfully divide two valid hex numbers.                                                      |
| **Constraint Handling** | No negative answers         | The calculator must not return any negative answers (e.g., attempting `05 - 0A` should be handled/prevented).        |
|                                     | No decimal places           | The calculator must not return answers with decimal places (e.g., attempting `05 / 02` should be handled/prevented). |
|                                     | Division by zero            | The calculator must safely handle or reject any attempts to divide by zero.                                          |

## Course Structure & Branches

This course is divided into 4 main sections. We will create specific branches for each section to keep track of our progression and help you navigate the tutorial:

- **[Section 1] Identifying functional requirements and setting up the repository** 
   - *Branch:* `section-1-setup`
- **[Section 2] Writing tests, drafting code** 
   - *Branch:* `section-2-tdd`
- **[Section 3] Testing the GUI** 
   - *Branch:* `section-3-gui` 
- **[Section 4] Porting to containers and cloud services** 
   - *Branch:* `section-4-deployment`

## Deployment & CI/CD Pipeline

This application is fully containerized using **Docker** and deployed to the **AWS Cloud**. 
- **Container Registry:** Images are securely stored in a private Amazon ECR repository.
- **Compute:** The container is hosted on an Amazon EC2 instance (Amazon Linux 2023) mapped to port 80.
- **Automation:** We use GitHub Actions for Continuous Integration and Continuous Deployment (CI/CD). Every push to the repository automatically triggers Pytest and Playwright GUI tests. If they pass, the pipeline builds the Docker image, pushes it to AWS, and updates the live EC2 server via SSH.

---

## Getting Started (Local Setup)

#### 1. **Clone the repository:**
```bash
git clone [https://github.com/kyle-liebenberg/hex-calculator.git](https://github.com/kyle-liebenberg/hex-calculator.git)
cd hex-calculator
```

### Option A: Run via Docker (Recommended)

Because this application is containerized for production, the easiest way to run it locally is using Docker.

```bash
# Build the image
docker build -t hex-calc .

# Run the container
docker run -p 8000:8000 hex-calc
```

*Open `http://localhost:8000` in your browser to view the calculator!*

### Option B: Run via Python Virtual Environment (For Development)

#### 2. **Create and activate the virtual environment:**

* On macOS/Linux: `python3 -m venv .venv && source .venv/bin/activate`
* On Windows: `python -m venv .venv && .venv\Scripts\activate`

#### 3. **Install dependencies:**

```Bash
pip install -r requirements.txt
pip install pytest pytest-playwright
playwright install
```

#### 4. **Run the backend Python server:**

Because our API serves our frontend static files, you must run the server from the `backend` directory.

```bash
cd backend
uvicorn src.main:app --reload
```

*Open `http://127.0.0.1:8000` in your browser to view the calculator!*

## Running Tests

To run the automated Test-Driven Development (TDD) tests and the Playwright GUI tests locally, ensure your virtual environment is active and your Python server is running in the background.

```bash
# Run both Backend Logic and Frontend GUI tests in one go!
export PYTHONPATH=backend
python -m pytest backend/test/ frontend/
```

---

*Built with ❤️ by Kyle & Diya for IMY 772*
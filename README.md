# Dorm & Dine

## Description
Dorm & Dine is a student-to-student food platform built for dormitory life. Instead of ordering expensive delivery or cooking alone for one, students can buy and sell home-cooked meals within their own building. Cooks cover their ingredient costs by selling extra portions, buyers get fresh food, and both sides skip the waste, the packaging, and the delivery fee.

---

## Tech Stack
- **Python 3.10+**
- **Flask** - web framework
- **Flask-SQLAlchemy** -  ORM 
- **Bootstrap-Flask** - UI components

---
## Installation
### 1. Clone the repository
```
git clone https://github.com/MrGreeeenTea/Dorm-Dine.git
cd Dorm-Dine
```

### 2. Create and activate a virtual environment
**Windows**
```
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS / Linux**
```
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```
pip install -r requirements.txt
```
---
## Running the App

```
flask run
```

---
## Sample Data

To populate the database with sample dorms, users, and meals, visit the following route **once** after starting the app:

```
http://localhost:5000/insert/sample
```

**Warning:** Do not use it in production.

---
## Routes

| Route | Description |
|-------|-------------|
| `/` | Landing page |
| `/feed` | Browse all available meals |
| `/dishes/<id>` | Meal detail |
| `/order_view/<id>` | Order confirmation |
| `/post` | Post a new meal *(login required)* |
| `/dashboard` | User dashboard *(login required)* |
| `/profile/<username>` | User profile |
| `/register` | Create a new account |
| `/login` | Log in |
| `/logout` | Log out |
| `/insert/sample` | Flush DB and load sample data |

---
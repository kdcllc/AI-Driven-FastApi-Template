# Code Refactoring Prompt

Use this prompt when refactoring code.

## Refactoring Principles

### 1. Make It Work, Make It Right, Make It Fast
- First ensure functionality is correct
- Then improve code quality
- Finally optimize performance

### 2. Keep Changes Small
- Refactor in small, testable increments
- Commit frequently
- Ensure tests pass after each change

### 3. Improve Without Changing Behavior
- Refactoring should not change external behavior
- Keep the same API contracts
- Maintain backward compatibility when possible

## Common Refactoring Patterns

### Extract Function
```python
# Before: Long function with multiple responsibilities
def process_user_data(data):
    # Validate
    if not data.get("email"):
        raise ValueError("Email required")
    
    # Process
    normalized = data["email"].lower().strip()
    
    # Save
    db.save(normalized)

# After: Smaller, focused functions
def validate_user_data(data):
    if not data.get("email"):
        raise ValueError("Email required")

def normalize_email(email):
    return email.lower().strip()

def process_user_data(data):
    validate_user_data(data)
    normalized_email = normalize_email(data["email"])
    db.save(normalized_email)
```

### Extract Class
```python
# Before: Related data and functions scattered
user_email = "user@example.com"
user_name = "John Doe"

def send_email(email, name):
    pass

# After: Encapsulated in a class
class User:
    def __init__(self, email: str, name: str):
        self.email = email
        self.name = name
    
    def send_email(self):
        pass
```

### Replace Magic Numbers
```python
# Before
if user.age >= 18:
    pass

# After
LEGAL_ADULT_AGE = 18
if user.age >= LEGAL_ADULT_AGE:
    pass
```

## Refactoring Checklist
- [ ] Identify code smell or improvement opportunity
- [ ] Ensure tests exist and pass
- [ ] Make incremental changes
- [ ] Run tests after each change
- [ ] Update documentation if needed
- [ ] Review for improved readability
- [ ] Check performance hasn't degraded

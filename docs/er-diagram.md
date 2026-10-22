# LedgerForge — Database ER Diagram

## Core HR Data Model

This diagram represents the four core tables used for
employee information, roles, departments, and assignment history.

```mermaid
erDiagram
    DEPARTMENTS ||--o{ ROLES : "contains"
    DEPARTMENTS ||--o{ EMPLOYEES : "has employees"
    DEPARTMENTS ||--o{ EMPLOYEE_ASSIGNMENTS : "assignment department"
    ROLES ||--o{ EMPLOYEES : "current role"
    ROLES ||--o{ EMPLOYEE_ASSIGNMENTS : "assignment role"
    EMPLOYEES ||--o{ EMPLOYEE_ASSIGNMENTS : "has history"
    EMPLOYEES |o--o{ EMPLOYEES : "manages"
    EMPLOYEES |o--o{ EMPLOYEE_ASSIGNMENTS : "assignment manager"

    DEPARTMENTS {
        string department_id PK
        string department_name
        string cost_center
    }

    ROLES {
        string role_id PK
        string department_id FK
        string role_title
        int level
    }

    EMPLOYEES {
        string employee_id PK
        string department_id FK
        string role_id FK
        string manager_id FK
        string full_name
        string work_email UK
        date hire_date
        date exit_date
    }

    EMPLOYEE_ASSIGNMENTS {
        string assignment_id PK
        string employee_id FK
        string department_id FK
        string role_id FK
        string manager_id FK
        date effective_from
        date effective_to
    }
```


## Database Rules

- Each department can contain multiple roles.
- Each employee belongs to one current department and role.
- An employee may have another employee as their manager.
- One employee can have multiple assignment-history records.
- Every work_email must be unique.
- exit_date cannot be earlier than hire_date.
- effective_to cannot be earlier than effective_from.
- A NULL exit_date or effective_to is allowed.
- Employee searches have indexes on department_id,
  manager_id, full_name, and employment_status.

## Migration

Initial database migration:
`faca27f3c8a6_create_core_hr_tables.py`

The migration supports both upgrade and downgrade.

# Django Modular API Using APIView

## Overview
Modular Django REST Framework backend to manage:

- **Master Apps:** Vendor, Product, Course, Certification  
- **Mapping Apps:** Vendor → Product, Product → Course, Course → Certification  
- **APIs built with:** APIView only  
- **Documentation:** Swagger & ReDoc (drf-yasg)

---

## Features
- CRUD for all master and mapping modules  
- Validations: unique codes, no duplicate mappings, only one primary mapping per parent  
- Soft delete with `is_active`  
- Query-param filtering  
- Modular app structure

---

## Setup
1. Clone repo:  
```bash
git clone https://github.com/<your-username>/django-modular-api.git
cd django-modular-api

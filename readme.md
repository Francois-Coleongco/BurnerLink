# 🔥 Burner Link

A self-destructing message link service built with Django.

## Features
- Create temporary links to secret messages
- Set expiration time (default: 24 hours)
- Optional one-time view (auto-deletes after opening)
- No user accounts required

## Coming Soon

- Messages will be encrypted at rest (password protected messages)

## How to use

Will deploy soon, but in the meantime:

### Requirements
- Python 3.10+
- Django 5.2.4

### Installation

```
pip install -r requirements.txt
cd BurnerLink
python manage.py runserver
```
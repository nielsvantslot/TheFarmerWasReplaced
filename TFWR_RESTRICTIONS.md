# TFWR Scripting Restrictions

This file documents language and syntax restrictions for The Farmer Was Replaced scripting environment.

## Known Restrictions

- The `is` and `is not` keywords are not allowed. Use `==` and `!=` for all equality/inequality checks.
- Real Python classes are not supported. Use the "faux class" pattern: a function returning a dictionary of methods and state.
- Typing imports and advanced Python typing features are not supported.
- Only a subset of Python built-ins and syntax is available; check game documentation for details.

Add more restrictions here as you discover them.

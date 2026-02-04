# Assignment 2 – CFG to PDA Conversion Using Python and PLY

## Project Overview

This implementation follows the standard CFG-to-PDA construction described in the course textbook.

---

## Work Distribution 

- **Nicole Zino**: CFG Tokenization (PLY Lexer)  
  [`grammar_parser/lexer.py`](grammar_parser/lexer.py)

- **Tolu Adekore**: PDA Simulation  
  [`cfg_to_pda/simulator.py`](cfg_to_pda/simulator.py)

- **Reet Singh**: *To be assigned*

- **Shahbaaz Gill**: *To be assigned*

### Remaining Components (to be assigned)

- CFG Structure Builder (PLY Parser)  
  [`grammar_parser/parser.py`](grammar_parser/parser.py)

- CFG → PDA Conversion  
  [`cfg_to_pda/converter.py`](cfg_to_pda/converter.py)

---

## Project Structure

The `ply/` directory contains the official source files for **PLY (Python Lex-Yacc)**,
copied directly from the PLY GitHub repository as recommended by the author.
- [`ply/init__`](ply/__init__.py)
- [`ply/lex`](ply/lex.py)
- [`ply/yacc`](ply/yacc.py)

---

## Tools

- Python 3
- PLY (Python Lex-Yacc)

---

## Dependencies

This project uses **PLY (Python Lex-Yacc)** by David Beazley.

PLY is included locally in this repository by copying the official source files
from the PLY GitHub repository, as recommended by the author.

Source: https://github.com/dabeaz/ply



---

## How to Run
1. Clone the repository
2. Run the main driver file:
   ```bash
   python main.py
---

## Conclusion

---

## References

- Sipser, Introduction to the Theory of Computation

- David Beazley, PLY – Python Lex-Yacc
https://www.dabeaz.com/ply/

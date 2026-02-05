import ply.lex as lex

# These are the kinds of tokens we want to recognize in a CFG
tokens = (
    "VAR",
    "ARROW",
    "PIPE",
    "EPS",
    "TERM",
    "NEWLINE",
)

# Simple fixed symbols
t_ARROW = r"->"
t_PIPE = r"\|"

# Ignore spaces and tabs (they don't matter for grammar rules)
t_ignore = " \t\r"

def t_EPS(t):
    # Match epsilon productions
    # We accept 'eps' (and also ε just in case)
    r"eps|ε"
    t.value = "eps"
    return t

def t_VAR(t):
    # Match nonterminal symbols (uppercase names like S, T, A, NP)
    r"[A-Z][A-Z_]*"
    return t

def t_TERM(t):
    # Match terminal symbols
    # These are single characters like digits or lowercase letters
    # This matches what we see in the lecture examples
    r"[a-z0-9\(\)\+\*/]"
    return t

def t_NEWLINE(t):
    # Keep track of line numbers and allow the parser to know when one rule ends and another begins
    r"\n+"
    t.lexer.lineno += len(t.value)
    return t

def t_comment(t):
    # Allow comments starting with # and anything after # on a line is ignored
    r"\#.*"
    pass

def t_error(t):
    # If we hit an unexpected character, stop and report it
    raise SyntaxError(f"Illegal character {t.value[0]!r} at line {t.lexer.lineno}")

def make_lexer():
    # Build and return the lexer object
    return lex.lex()

# Small test to make sure the lexer works on its own and to see the tokens printed
if __name__ == "__main__":
    sample = """S -> 0T1 | eps
T -> 0T1 | eps
"""
    lexer = make_lexer()
    lexer.input(sample)
    for tok in lexer:
        print(tok.type, tok.value)
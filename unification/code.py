def occurs_check(var, expr):
    """Check if variable occurs in expression (to avoid infinite substitution)."""
    if var == expr:
        return True
    elif isinstance(expr, list):
        return any(occurs_check(var, subexpr) for subexpr in expr)
    return False


def substitute(expr, var, val):
    """Apply substitution {var/val} to expression."""
    if expr == var:
        return val
    elif isinstance(expr, list):
        return [substitute(subexpr, var, val) for subexpr in expr]
    else:
        return expr


def unify(x, y, subst=None):
    """Unification algorithm based on the image steps."""
    if subst is None:
        subst = {}

    # Step 1: If x or y is variable/constant
    if isinstance(x, str) and x.islower():  # x is variable
        if x in subst:
            return unify(subst[x], y, subst)
        elif occurs_check(x, y):
            return None  # FAILURE
        else:
            subst[x] = y
            return subst

    elif isinstance(y, str) and y.islower():  # y is variable
        if y in subst:
            return unify(x, subst[y], subst)
        elif occurs_check(y, x):
            return None  # FAILURE
        else:
            subst[y] = x
            return subst

    elif x == y:

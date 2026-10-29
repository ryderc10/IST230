"""Chapter 1 logic operations and truth table."""


def negation(p: bool) -> bool:
    """Returns the logical negation of p (¬p)."""
    return not p


def conjunction(p: bool, q: bool) -> bool:
    """Returns the logical conjunction of p and q (p ∧ q)."""
    return p and q


def disjunction(p: bool, q: bool) -> bool:
    """Returns the logical disjunction of p and q (p ∨ q)."""
    return p or q


def exclusive_or(p: bool, q: bool) -> bool:
    """Returns p ⊕ q: True if exactly one input is True."""
    return p != q


def conditional(p: bool, q: bool) -> bool:
    """Returns p → q: False ONLY when p is True and q is False."""
    return (not p) or q


def biconditional(p: bool, q: bool) -> bool:
    """Returns p ↔ q: True when p and q have the same truth value."""
    return p == q


def run_truth_table_generator():
    """Displays evaluations for all four binary truth assignments."""
    print(f"{'p':<6} | {'q':<6} | {'¬p':<6} | {'p ∧ q':<6} | {'p → q':<12} | {'q → p (Conv)':<13}")
    print("-" * 60)
    combinations = [(True, True), (True, False), (False, True), (False, False)]
    for p, q in combinations:
        print(
            f"{str(p):<6} | {str(q):<6} | {str(negation(p)):<6} | "
            f"{str(conjunction(p, q)):<6} | {str(conditional(p, q)):<12} | "
            f"{str(conditional(q, p)):<13}"
        )


if __name__ == "__main__":
    print("IST 230 Lab - Chapter 1 Evaluation Matrix")
    run_truth_table_generator()

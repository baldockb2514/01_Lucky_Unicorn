# Add decoration to a statement
def statement_decorator(statement, decoration):
    # Make string with three characters
    sides = decoration * 3

    # add decoration to start and ent of statement
    statement = "{} {} {}".format(sides, statement, sides)
    # Make the decoration above and below the statement the same length as the statement
    top_bottom = decoration * len(statement)

    # add decoration to the to and bottom of the statement
    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


statement_decorator("Unicorn", "*")

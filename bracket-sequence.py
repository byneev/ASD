def is_correct_bracket_seq():
    closed = [")", "]", "}"]
    opened = ["(", "[", "{"]
    brackets = [char for char in input()]
    if not len(brackets):
        return True
    if brackets[0] in closed:
        return False
    if bool(len(brackets) % 2):
        return False
    opened_count = 0
    closed_count = 0
    for item in opened:
        if item in brackets:
            opened_count += 1
    for item in closed:
        if item in brackets:
            closed_count += 1
    if closed_count != opened_count:
        return False
    if closed_count == 1 and opened_count == 1:
        return True
    if closed_count == 2 and opened_count == 2:
        if (
            brackets[len(brackets) - 2] == "{"
            and brackets[len(brackets) - 1] == "}"
        ):
            return True

    while bool(len(brackets)):
        actual_length = len(brackets)
        try:
            current_open_index = opened.index(brackets[0])
        except ValueError:
            return False
        i = 0
        inner_loop_work = True
        closed_count = 0
        while inner_loop_work and i < len(brackets):
            if brackets[i] in closed:
                closed_count += 1
                if (
                    current_open_index == closed.index(brackets[i])
                    and bool(i % 2)
                    and closed_count == (i + 1) / 2
                ):
                    del brackets[i]
                    del brackets[0]
                    inner_loop_work = False
            i += 1
        if actual_length == len(brackets):
            return False
    return True


print(is_correct_bracket_seq())

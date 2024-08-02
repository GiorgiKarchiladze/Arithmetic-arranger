def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = ""
    second_line = ""
    dashes = ""
    answers = ""

    for problem in problems:
        first_number = problem.split()[0]
        operator = problem.split()[1]
        second_number = problem.split()[2]

        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        if not first_number.isdigit() or not second_number.isdigit():
            return "Error: Numbers must only contain digits."
        if len(first_number) > 4 or len(second_number) > 4:
            return "Error: Numbers cannot be more than four digits."

        length = max(len(first_number), len(second_number)) + 2
        top = first_number.rjust(length)
        bottom = operator + second_number.rjust(length - 1)
        line = "-" * length

        if show_answers:
            if operator == "+":
                answer = str(int(first_number) + int(second_number)).rjust(length)
            else:
                answer = str(int(first_number) - int(second_number)).rjust(length)

        if first_line:
            first_line += "    "
            second_line += "    "
            dashes += "    "
            if show_answers:
                answers += "    "

        first_line += top
        second_line += bottom
        dashes += line

        if show_answers:
            answers += answer

    if show_answers:
        arranged_answers = first_line + "\n" + second_line + "\n" + dashes + "\n" + answers
    else: arranged_answers = first_line + "\n" + second_line + "\n" + dashes

    return arranged_answers



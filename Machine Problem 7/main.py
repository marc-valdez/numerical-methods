import math
import os

try:
    import msvcrt
except ImportError:
    msvcrt = None


def arrow_menu(prompt, options):
    """Interactive arrow-key menu (Up/Down + Enter)."""
    if msvcrt is None:
        # Fallback for non-Windows terminals.
        print(prompt)
        for idx, option in enumerate(options, start=1):
            print(f"{idx}. {option}")
        while True:
            try:
                choice = int(input("Enter choice number: ").strip())
                if 1 <= choice <= len(options):
                    return options[choice - 1]
            except ValueError:
                pass
            print("Invalid choice. Try again.")

    selected = 0
    while True:
        os.system("cls")
        print(
            "Numerical Derivatives using Hardcoded Divided-Difference Formulas (up to 2nd Derivative)"
        )
        print()
        print(prompt)
        for i, option in enumerate(options):
            prefix = ">" if i == selected else " "
            print(f"{prefix} {option}")

        key = msvcrt.getch()

        if key in (b"\r", b"\n"):
            return options[selected]

        if key in (b"\x00", b"\xe0"):
            key2 = msvcrt.getch()
            if key2 == b"H":
                selected = (selected - 1) % len(options)
            elif key2 == b"P":
                selected = (selected + 1) % len(options)


def choose_function(choice):
    if choice == 1:
        return "exp(x)", lambda x: math.exp(x)
    if choice == 2:
        return "ln(x+1)", lambda x: math.log(x + 1)
    if choice == 3:
        return "sqrt(x+4)", lambda x: math.sqrt(x + 4)
    return None, None


def required_nodes(method, x, h):
    if method == "forward":
        return [x, x + h, x + 2 * h]
    if method == "backward":
        return [x, x - h, x - 2 * h]
    return [x - h, x, x + h]


def validate_domain(function_name, nodes):
    if function_name == "ln(x+1)":
        return all(
            node > -1 for node in nodes
        ), "ln(x+1) requires all sample points > -1."
    if function_name == "sqrt(x+4)":
        return all(
            node >= -4 for node in nodes
        ), "sqrt(x+4) requires all sample points >= -4."
    return True, ""


def compute_derivatives(func, x, h, method):
    if method == "forward":
        first = (-3 * func(x) + 4 * func(x + h) - func(x + 2 * h)) / (2 * h)
        second = (func(x) - 2 * func(x + h) + func(x + 2 * h)) / (h * h)
        return first, second

    if method == "backward":
        first = (3 * func(x) - 4 * func(x - h) + func(x - 2 * h)) / (2 * h)
        second = (func(x) - 2 * func(x - h) + func(x - 2 * h)) / (h * h)
        return first, second

    first = (func(x + h) - func(x - h)) / (2 * h)
    second = (func(x + h) - 2 * func(x) + func(x - h)) / (h * h)
    return first, second


def main():
    try:
        function_options = ["exp(x)", "ln(x+1)", "sqrt(x+4)"]
        selected_function = arrow_menu(
            "Choose function (Arrow keys + Enter):", function_options
        )
        fn_choice = function_options.index(selected_function) + 1
        function_name, func = choose_function(fn_choice)
        if func is None:
            print("Invalid function choice.")
            return

        x = float(input("Enter x: ").strip())
        h_input = input("Enter step size h (e.g. 0.001): ").strip()
        h = 0.001 if h_input == "" else float(h_input)
        if h <= 0:
            print("h must be positive.")
            return

        method_options = ["forward", "backward", "center"]
        method = arrow_menu("Choose method (Arrow keys + Enter):", method_options)

        nodes = required_nodes(method, x, h)
        is_valid, error_message = validate_domain(function_name, nodes)
        if not is_valid:
            print(error_message + " Adjust x or h.")
            return

        first_derivative, second_derivative = compute_derivatives(func, x, h, method)

        print("\nResults")
        print(f"f(x) = {function_name}")
        print(f"Method = {method}")
        print(f"x = {x:.4f}")
        print(f"f'(x) = {first_derivative:.4f}")
        print(f"f''(x) = {second_derivative:.4f}")

    except ValueError:
        print("Invalid numeric input.")


if __name__ == "__main__":
    main()

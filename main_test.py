from main import *

run_cases = [
    (
        [
            ["Scooby Doo", "Lassie"],
            ["Blue", "Wishbone"],
        ],
        ["Cartoon TV Dogs", "Real TV Dogs"],
        "<table><tr><th>Cartoon TV Dogs</th><th>Real TV Dogs</th></tr><tr><td>Scooby Doo</td><td>Lassie</td></tr><tr><td>Blue</td><td>Wishbone</td></tr></table>",
    ),
]

submit_cases = run_cases + [
    (
        [
            ["Garfield", "Salem"],
            ["Tom", "Mr. Bigglesworth"],
        ],
        ["Cartoon TV Cats", "Real TV Cats"],
        "<table><tr><th>Cartoon TV Cats</th><th>Real TV Cats</th></tr><tr><td>Garfield</td><td>Salem</td></tr><tr><td>Tom</td><td>Mr. Bigglesworth</td></tr></table>",
    ),
]


def test(data_rows, headers, expected_output):
    print("---------------------------------")
    print(f"Data Rows: {data_rows}")
    print(f"Headers: {headers}")
    print(f"Expecting:\n{expected_output}")
    result = create_html_table(data_rows)(headers)
    print(f"Actual:\n{result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()

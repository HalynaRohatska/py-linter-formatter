def format_linter_error(error: dict) -> dict:
    formated_error = {
        "source": "flake8"
    }
    for key, value in error.items():
        if key == "line_number":
            formated_error["line"] = value
        elif key == "column_number":
            formated_error["column"] = value
        elif key == "text":
            formated_error["message"] = value
        elif key == "code":
            formated_error["name"] = value
    return formated_error


def format_single_linter_file(file_path: str, errors: list) -> dict:
    # write your code here
    pass


def format_linter_report(linter_report: dict) -> list:
    # write your code here
    pass

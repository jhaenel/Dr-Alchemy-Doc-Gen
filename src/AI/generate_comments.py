from src.AI.openai_util import call_openai_api

GENERATE_COMENTS_PROMPT = """
Add any useful, insightful inline comments to the code below.
Give me back the full unaltered code with your comments added.
Here is the code:

"""


def generate_comments(code_to_comment: str) -> dict:
    comment_prompt = GENERATE_COMENTS_PROMPT + code_to_comment
    return call_openai_api(comment_prompt)


if __name__ == "__main__":
    code_to_comment = """
    a = 5
    b = 2
    hypotensuse = (a**2 + b**2)**0.5
    """
    result = generate_comments(code_to_comment)
    print(result)

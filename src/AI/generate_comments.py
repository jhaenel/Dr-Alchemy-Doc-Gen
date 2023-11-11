from src.AI.openai_util import generate

GENERATE_COMENTS_PROMPT = """
Add any useful, insightful inline comments to the code below.
Give me back the full unaltered code with your comments added.
DO NOT ADD ANYTHING OTHER THAN COMMENTS.
Your response should be a fucntioning file, dont add anything before or after that would break the code.
Here is the code:

"""


def generate_comments(code_to_comment: str) -> dict:
    comment_prompt = GENERATE_COMENTS_PROMPT + code_to_comment
    return generate(comment_prompt)

if __name__ == "__main__":
    code_to_comment = """
    a = 5
    b = 2
    hypotensuse = (a**2 + b**2)**0.5
    """
    result = generate_comments(code_to_comment)
    print(result)

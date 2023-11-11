from src.AI.openai_util import generate

GENERATE_COMENTS_PROMPT = """
Add any useful, insightful inline comments to the code below.
Give me back the full unaltered code with your comments added.
DO NOT ADD ANYTHING OTHER THAN COMMENTS.
ONLY RESPOND WITH THE CODE AND COMMENTS INA PYTHON CODE.
Do not put your response inside a code block. And there should be nothing before and nothing after.
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

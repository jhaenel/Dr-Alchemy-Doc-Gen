import click
from src.orchestration import orchestration

@click.command()
@click.option('-s', '--source', default='.', help='Source directory to copy from. Default is the current directory.')
def main(source, destination, model):
    """
    CLI tool to automate generating comments for software, using specified OpenAI model.
    """
    click.echo(f"Running with source: {source}")
    orchestration(source,)

if __name__ == '__main__':
    main()

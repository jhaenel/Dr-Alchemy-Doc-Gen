import click
from src.orchestration import orchestration

@click.command()
@click.option('-s', '--source', default='.', help='Source directory to copy from. Default is the current directory.')
@click.option('-d', '--destination', default='doc_gen', help='Destination directory to copy to. Default is "doc_gen".')
def main(source, destination, model):
    """
    CLI tool to automate generating comments for software, using specified OpenAI model.
    """
    click.echo(f"Running with source: {source}, destination: {destination}")
    orchestration(source, destination)

if __name__ == '__main__':
    main()

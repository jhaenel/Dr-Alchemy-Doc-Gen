import click
from src.orchestration import orchestrate


@click.command()
@click.option(
    "-s",
    "--source",
    default=".",
    help="Source directory to copy from. Default is the current directory.",
)
@click.option(
    "-d",
    "--destination",
    default="doc_gen",
    help='Destination directory to copy to. Default is "doc_gen".',
)
def main(source: str, destination: str) -> None:
    """
    CLI tool to automate generating comments for software in cloned directory
    """
    click.echo(f"Running with source: {source}, destination: {destination}")
    orchestrate(source, destination)


if __name__ == "__main__":
    main()

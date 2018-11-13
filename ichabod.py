from typing import List

import click
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


@click.command()
@click.option('--debug', default=False, type=bool, is_flag=True,
              help="Debug the script. Turns off headless mode and requires actual browser window.")
@click.option('--limit', default=20, type=int, help="Limit the number of results to display.")
@click.option('-v', '--verbose', type=bool, default=False, is_flag=True,
              help="Print details of operations to the console.")
@click.argument('words', nargs=-1, required=True)
def search(words: List[str], limit: int, verbose: bool, debug: bool) -> None:
    """Search Google for a phrase made up of WORDS (Default)"""

    def _echo(value: str, is_verbose: bool=True):
        if not is_verbose or (verbose and is_verbose):
            click.echo(value)

    phrase = " ".join(words)
    options = Options()
    if not debug:
        options.add_argument("--headless")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)

    try:
        _echo(click.style("Loading Google.com", dim=True))
        driver.get("https://www.google.com")

        _echo(click.style("Searching for \"{}\"".format(phrase), dim=True))
        search_box = driver.find_element_by_name("q")
        search_box.clear()
        search_box.send_keys(phrase)
        search_box.send_keys(Keys.RETURN)
        item = 0

        while item < limit:
            _echo(click.style("Parsing response".format(phrase), dim=True))
            entries = driver.find_elements_by_xpath('//div[@class="rc"]')
            _echo(click.style("Found {} entries".format(len(entries), limit), dim=True))

            for entry in entries:
                item += 1
                a = entry.find_element_by_xpath('.//div[@class="r"]/a')
                href = a.get_attribute("href")
                title = entry.find_element_by_xpath('.//div[@class="r"]//h3').text
                text = entry.find_element_by_xpath('.//div[@class="s"]/div/span').text
                _echo('', False)
                _echo(click.style(title, bold=True, fg="bright_magenta"), False)
                _echo(click.style(href, underline=True, fg="bright_blue"), False)
                _echo(click.style(text), False)
                _echo('', False)
                if item >= limit:
                    break
            if item >= limit:
                break
            _echo(click.style("Loading next page of results", dim=True))
            driver.find_element_by_link_text("Next").click()

    except Exception as cause:
        click.echo("An error occurred: {}".format(cause), err=True)
    finally:
        driver.close()


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        pass


cli.add_command(search)


if __name__ == '__main__':
    cli()


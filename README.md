# Ichabod the Headless Scraper

## Local Python

### Install

1. Install [Google Chrome](https://www.google.com/chrome/).

2. Install [Chrome Driver](http://chromedriver.chromium.org/).

3. Clone the repository

    ```bash
    git clone https://github.com/aenglander/ichabod.git
    ```

4. Switch to the cloned code directory

    ```bash
    cd ichabod
    ```

5. Install project requirements via [pipenv](https://pipenv.readthedocs.io/).

    ```bash
    pipenv install --three
    ```

### Search Google

Run the script with a search term like my name:

```bash
pipenv run python ichabod.py search Adam Englander
```

## Docker

### Build the Image

1. Clone the repository

    ```bash
    git clone https://github.com/aenglander/ichabod.git
    ```

2. Switch to the cloned code directory

    ```bash
    cd ichabod
    ```

3. Build the container

    ```bash
    docker build -t ichabod .
    ```

### Run the Image

Run the image in an non-persistent interactive terminal mode using the `search` command with a 
search term like my name:

```bash
docker run --rm -it ichabod search Adam Englander
```

## Getting Help

Adding `--help` to execution in either environment will show the help information.

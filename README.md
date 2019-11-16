# linear-economic-graph
Create a command line program that asks for a product and it's maximum quantity. 
It will then ask for the marginal utility at each point.

Simple program which outputs a line graph that plots the product's utility in function of the quantity.

## Installation

Python 3 and Pipenv are required in order to run this program.

### OSX

```bash
brew install python3
```
```bash
brew install pipenv
```

## Usage

If you want to test the script manually, you can achieve this by doing :

```bash
cd module
pipenv install
pipenv run python3 index.py
```

## Example

<p align="center">
    <img src="assets/cli-example.png" width="400">
    <img src="assets/graph-example.png" width="650">
</p>

## Executable

If you want to build a cross-platform executable, you need to execute the following bash commands :

```bash
cd module
pipenv install
pipenv run pyinstaller index.py --onefile
```

The executable file will be located on the generated dist folder.

## License

[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)

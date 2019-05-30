
## CodeClub Async/Await presentation examples and exercises

### Download and install Python 3.6+

MacOS X comes with Python 2.x preinstalled, which is too old and does
not support async/await. Several options for downloading/installing 
Python on MacOS:

* Official Python web site:
  <https://www.python.org/downloads/>
  
* Install Python with `brew`:
  ```
  brew install python
  ```


### Install dependencies
We only need `aiohttp` for these examples:
```
pip3 install --user aiohttp
```

### Run the examples/exercises

Start with `playground.py`. Examine the code, run the file and examine
the output. Can you answer the questions in the comments in the code?

Then examine `crawler-01.py`. This is more or less the crawler code
mentioned during the presentation. Is it clear how it works? Run the
script and examine the results.

If have time, and would like to dive a bit deeper, try implementing
image links checker: instead of returning just the sizes of all pages,
verify whether all images on the page are valid (return 2xx HTTP status).

`crawler-02` is a trivial example implementation of such image validator.
Can you spot problems there? How would you improve it?
 

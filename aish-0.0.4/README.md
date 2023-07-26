AISHell
=====

An language-model-powered shell wrapper that tries to Do What You Mean.

⚠️ DO NOT USE THIS SHELL IF YOU DO NOT WANT DATA LOSS OR OTHER NEGATIVE
CONSEQUENCES INCLUDING BUT NOT LIMITED TO ACTUALLY EMAILING JEFF BEZOS

More info, including a pre-recorded demo of what the result looks like, can be found at:

https://riveducha.onfabrica.com/openai-powered-linux-shell


Installation
--------

You will need to install the Python dependencies listed in either Pipfile (for
Pipenv users) or requirements.txt (for pip users).

Since large GPT models are impractical to run for most people, this program uses
external services.

There are currently two providers available: OpenAI (based on GPT-3), and Grand
(GPT-J-6B). Since OpenAI currently has a waitlist for its API, you may consider
Grand instead.

Whichever service you choose, you will need an account and sufficient budget for
your usage.

For OpenAI, set the `OPENAI_API_KEY` environment variable to your own OpenAI API
key.

For Grand, set `GRAND_AUTH_KEY` and `GRAND_AUTH_SECRET` to your own key.

Then, you can run `./aish`.

Additionally included is a `howdoi` command that simply prints out the result
from the AI. This is useful for occassional help on the command-line.

Usage
-----

`aish` is similar to a typical CLI shell, but instead of typing in the name
of a process to run, you type in what you want to accomplish. It will then
query the GPT API for a bash command to run.

You have a chance to approve the generated command by pressing Enter, or
canceling and not running the command with ^C.

Commands may not do the right thing, or may do something harmful or otherwise
unwanted.

`howdoi` provides one-off answers, and can be used as follows:

```
$ howdoi add myself to the docker group
sudo usermod -aG docker $USER
```

Built-ins
---------

There are several built-in commands that are executed directly, rather than
passed to the AI:

* cd - changes the current working directory
* pwd - shows the current working directory
* clear - clears the terminal. If readline is working properly, then ^L should
  also clear the terminal.

Options
-------

`--live-dangerously`: if run with this flag, `aish` will not ask for approval before running the AI-generated command. DO NOT USE THIS FLAG.

`--reverse`: Generate natural-language descriptions of the shell command that you type in.

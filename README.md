# Raspberry Pi Pico

A very basic data logger... purely used as a quick demonstration.


## What does it do?

Simply put:

- blinks a light
- saves subset of Pin & ADC values to a CSV file.

that's it 😎.

**Is it tested?**

Nope!

Note: it doesn't handle oversized file (ie: disk out of space),
I think the light will keep blinking.. so if you adopt this project
to your own, that's probably the first thing to fix 👍.


## Setup & Run

### Pre-requisites

Hardware: a [Raspberry Pi Pico](https://micropython.org/download/RPI_PICO)
(or [Pico W](https://micropython.org/download/RPI_PICO_W)) (preferably with latest firmware)

Software: Install [`mpremote`](https://pypi.org/project/mpremote/)

```shell
python -m pip install -r requirements.txt
```

Or use Thonny... apparently... but I haven't figured that out yet.

### Exec Remotely

To run and debug, `mpremote` is awesome:

```shell
$ mpremote mount ./src run ./src/main.py repl
>>> run()
```

Will run the mainline.

You can also halt it by pressing `[Ctrl+C]`.
It's using async, so re-starting `run()` after halting probably won't be pretty...
best `[Ctrl+D]` to reset before each `run()`

### Flash and Run

ie: independent of a computer.

Copy files over with `./copy.sh`.

Note: this is a bit flawed, it will replace changed files, but won't
purge deleted files (not a sync; just a copy).

Again: I haven't quite figured a good way to do this yet 🤔.

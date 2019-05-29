#!/usr/bin/env python3

import asyncio
import time

# Async/await learning playground:
# Several functions that do trivial things. Run this example and examine the console output.
# Try to answer questions in the comments.
#


def hog_cpu(duration):
    """ Hog CPU for the amount of time specified. This is NOT a coroutine, and it does not yield """
    # Non-async sleep, simulates long-running function
    time.sleep(duration)


async def buggy_foo():
    """ Question: we call this function in main. Why we don't see Buggy-foo on the console? """
    print("Buggy-foo!")


async def buggy_bar():
    """ Question: This function raises an exception. Who printed the exception message? Why? """
    print("Buggy-bar!")
    raise Exception("Buggy-bar exception")


async def looping_bar():
    """ Example of long-running execution, with periodic yield to the loop """
    for x in range(20):
        print('Loop #', x)
        hog_cpu(1)
        await asyncio.sleep(0)


async def meaning_of_life():
    return 42


def timer():
    print('Timer!')
    asyncio.get_event_loop().call_later(3, timer)


async def main():
    print('Main!')
    timer()
    buggy_foo()
    meaning = meaning_of_life()
    print("Meaning of life is (wrong!): ", meaning)
    print("Meaning of life is (right!): ", await meaning)
    asyncio.get_event_loop().create_task(buggy_bar())
    await looping_bar()


asyncio.get_event_loop().run_until_complete(main())

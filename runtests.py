"""
Simple script that actually executes py.test runner when passed "--pytest" as
first argument; in this case, all other arguments are forwarded to pytest's
main().
"""

if __name__ == '__main__':
    import sys
    # check manually if we plan to use pytest, so we leave argument handling
    # to pytest's main.
    if len(sys.argv) > 1 and sys.argv[1] == '--pytest':
        import pytest
        sys.exit(pytest.main(sys.argv[2:]))
    else:
        # now argv can be parsed by your arguments parsing library of choice
        # using argv as usual
        print('Hello')
        sys.exit(0)

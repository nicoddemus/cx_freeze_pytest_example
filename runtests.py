
if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == '--pytest':
        import pytest
        sys.exit(pytest.main(sys.argv[2:]))
    else:
        print('Hello')
        sys.exit(0)

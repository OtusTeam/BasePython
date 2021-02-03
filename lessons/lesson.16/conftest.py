from pytest import fixture

print("before all tests")

# sys.path.insert(0, "")


@fixture
def my_fixture():
    return "spam and eggs"

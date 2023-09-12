import StudentCode;
from IOWrapper import IOWrapper
testIO= IOWrapper()
expectedIO= IOWrapper()
def test_hello():
    expectedIO.print("Hello World")
    assert (StudentCode.runner(testIO)).check(expectedIO)
    print("Passed")
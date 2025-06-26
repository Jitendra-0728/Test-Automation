import pytest


@pytest.fixture(scope="class")                               # Fixture --- used to execute common functionality before the mentioned testcases
def setup():
    print("i'll execute before the testcase")
    yield                                       # yield --- use to execute statement after the mentioned test cases
    print("i'll execute after all the testcases")


# ____________________________________________________________________
# Data driven Fixture ---- Data driven & Parameterization can be done by using return statement in tuple format

@pytest.fixture()
def dataLoad():
    print("User Profile")
    return ["Hello","Shadow","Viper"]

# ____________________________________________________________________
# Parameterization

# @pytest.fixture(params=["chrom", "firefox","IE"])         # tuple values - all are binding with request to execute 1 by 1
@pytest.fixture(params=[("chrome", "shadow", "viper"), ("firefox", "Insta", "facebook", "twitter"), ("IE", "X")])       #   multiple set of value and access like request.chrome and its index we want, EX crossbrowser[1] ---then o/p will be shadow, Insta, x --- return 1 index of each group
def crossBrowser(request):
    return request.param


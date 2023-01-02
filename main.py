from natas0 import get_natas1_password
from natas1 import get_natas2_password
from natas2 import get_natas3_password
from natas3 import get_natas4_password
from natas4 import get_natas5_password
from natas5 import get_natas6_password
from natas6 import get_natas7_password
from natas7 import get_natas8_password
from natas8 import get_natas9_password
from natas9 import get_natas10_password
from natas10 import get_natas11_password
from natas11 import get_natas12_password
from natas12 import get_natas13_password
from natas13 import get_natas14_password
from natas14 import get_natas15_password
from natas15 import get_natas16_password
from natas16 import get_natas17_password


def main():
    natas1_password = get_natas1_password()
    natas2_password = get_natas2_password(natas1_password)
    natas3_password = get_natas3_password(natas2_password)
    natas4_password = get_natas4_password(natas3_password)
    natas5_password = get_natas5_password(natas4_password)
    natas6_password = get_natas6_password(natas5_password)
    natas7_password = get_natas7_password(natas6_password)
    natas8_password = get_natas8_password(natas7_password)
    natas9_password = get_natas9_password(natas8_password)
    natas10_password = get_natas10_password(natas9_password)
    natas11_password = get_natas11_password(natas10_password)
    natas12_password = get_natas12_password(natas11_password)
    natas13_password = get_natas13_password(natas12_password)
    natas14_password = get_natas14_password(natas13_password)
    natas15_password = get_natas15_password(natas14_password)
    natas16_password = get_natas16_password(natas15_password)
    natas17_password = get_natas17_password(natas16_password)


if __name__ == '__main__':
    main()

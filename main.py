from natas0 import get_natas1_password
from natas1 import get_natas2_password
from natas2 import get_natas3_password

def main():
    natas1_password = get_natas1_password()
    natas2_password = get_natas2_password(natas1_password)
    natas3_password = get_natas3_password(natas2_password)

if __name__ == '__main__':
    main()
from natas0 import get_natas1_password
from natas1 import get_natas2_password

def main():
    natas1_password = get_natas1_password()
    natas2_password = get_natas2_password(natas1_password)

if __name__ == '__main__':
    main()
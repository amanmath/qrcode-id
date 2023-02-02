from driverInfo import DriverInfo
from flask import Flask

app = Flask(__name__)


@app.route('/information/getDriverInfo')
def retrieveDriverInfo():
    p1 = DriverInfo("Aman", "Matharu", "llS933923ljfd", "82 Universe Drive", "1997-01-15")
    return p1.infoBehindQR


def main():
    p1 = DriverInfo("Aman", "Matharu", "llS933923ljfd", "82 Universe Drive", "1997-01-15")
    print(p1.infoBehindQR)

if __name__ == "__main__":
    main()
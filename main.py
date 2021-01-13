import AutoPilot


def main():
    config = open('config.txt', 'r')
    lines = config.readlines()
    auto_pilot = AutoPilot(key=lines[0].strip(), secret=lines[1].strip())
    result = auto_pilot.get_symbol_info(symbol='BTCUSDT')
    if(result != None):
        print(result)
    print(type(result))


if __name__ == '__main__':
    main()

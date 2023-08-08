import fire

from mylib.calc import add, sub, mul, div, sqrt


def add_cli(a, b):
    print(add(a, b))


def sub_cli(a, b):
    print(sub(a, b))


def mul_cli(a, b):
    print(mul(a, b))


def div_cli(a, b):
    print(div(a, b))


def sqrt_cli(a):
    print(sqrt(a))


def main():
    cli = {
        "add": add_cli,
        "sub": sub_cli,
        "mul": mul_cli,
        "div": div_cli,
        "sqrt": sqrt_cli,
    }

    fire.Fire(cli)


if __name__ == "__main__":
    main()

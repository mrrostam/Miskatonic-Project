import random

class Token:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class ChaosBag:
    def __init__(self, t=[("+1", 1), ("0", 2), ("-1", 3), ("-2", 2), ("-3", 1), ("-4", 1), ("-5", 0), ("-6", 0), ("-7", 0), ("-8", 0), ("Skull", 2), ("Cultist", 1), ("Elder Thing", 0), ("Tablet", 1), ("Tentacles", 1), ("Elder Sign", 1)]):
        self.tokens = []
        for i in t:
            for j in range(i[1]):
                self.tokens.append(Token(i[0]))

    def get_token(self, num=1):
        return random.sample(self.tokens, num)

    def add_token(self, t="0"):
        self.tokens.append(Token(t))
        return self

    def remove_token(self, t="0"):
        for token in self.tokens:
            if token.name == t:
                self.tokens.remove(token)
                break
        return self

    def __repr__(self):
        s = ""
        s += "-"*14
        for token in self.tokens:
            s += "\n|{:>12}|".format(str(token))
        s = s + "\n" + "-"*14
        return s


if __name__ == '__main__':
    chaos_bag = ChaosBag()
    print(chaos_bag)
    token = chaos_bag.get_token()
    print(token)

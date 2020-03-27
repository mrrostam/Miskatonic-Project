import random
import constant


class Token:
    def __init__(self, name, parentBag=None):
        self.name = name
        self.parentBag = parentBag

    def __repr__(self):
        return self.name


class ChaosBag:
    def __init__(self, t=constant.default_tokens, parentScenario=None):
        self.parentScenario = parentScenario
        self.tokens = []
        for i in t:
            for _ in range(i[1]):
                self.tokens.append(Token(i[0], self))

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
    import sys
    chaos_bag = ChaosBag()
    print(chaos_bag)
    token = chaos_bag.get_token()
    print(token)
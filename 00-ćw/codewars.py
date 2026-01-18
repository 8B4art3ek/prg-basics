VERSES = {
    "first": "{N} bottle{s} of beer on the wall, {n} bottle{s} of beer.",
    "second": "Take one down and pass it around, {n} bottle{s} of beer on the wall.",
    "final": "Go to the store and buy some more, {n} bottle{s} of beer on the wall.",
}

def sing(bottles: int = 99) -> list[str]:
    def verse(kind, num):
        amount = str(num or "no more")
        suffix = "s" if num != 1 else ""
        return VERSES[kind].format(n=amount, N=amount.capitalize(), s=suffix)

    def stanzas(initial_num):
        count = max(initial_num, 0)
        while count:
            yield verse("first", count)
            count -= 1
            yield verse("second", count)
        else:
            yield verse("first", 0)
            yield verse("final", initial_num)

    return list(stanzas(bottles))

lines = iter(sing())
stanzas = zip(lines, lines)
for verses in stanzas:
    print(*verses, sep="\n", end="\n\n")
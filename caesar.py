from asciimatics import screen

alphas = [
    "abcdefghijklmnopqrstuvwxyz",
    "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzżź",
    "aąbcćdeęfghijklłmnńoóprsśtuwyzżź",
]

cypher = input()

def main(scr: screen.Screen):
    offset = 0

    def get_rotated(ctext: str, alpha: str, ofs: int):
        ptext = ""
        for c in ctext:
            try:
                ptext += alpha[(alpha.index(c) + ofs) % len(alpha)]
            except ValueError:
                ptext += c
        return ptext

    while True:
        scr.wait_for_input(1)
        ev: screen.KeyboardEvent = scr.get_event()
        if not isinstance(ev, screen.KeyboardEvent):
            continue

        scr.print_at(f"{offset:3}", 0, 0)
        scr.print_at(cypher, 0, 1)

        for aidx, alpha in enumerate(alphas):
            scr.print_at(get_rotated(cypher, alpha, offset), 0, aidx + 3)

        scr.refresh()

        if ev.key_code == scr.KEY_ESCAPE:
            break
        if ev.key_code in [scr.KEY_LEFT, scr.KEY_UP]:
            offset -= 1
        if ev.key_code in [scr.KEY_RIGHT, scr.KEY_DOWN]:
            offset += 1

try:
    screen.Screen.wrapper(main, height=20)
except KeyboardInterrupt:
    ...

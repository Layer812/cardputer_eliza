import eliza
import time

eliza = eliza.Eliza()
eliza.load('doctor.txt')

while True:
    print("\n\n\n\n\n\n\n", eliza.initial())
    while True:
        said = input('> ')
        response = eliza.respond(said)
        if response is None:
            break
        print(response)
    print(eliza.final())
    time.sleep(3)

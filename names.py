import cPickle
import gzip
def load(file_name):
    # load the model
    stream = gzip.open(file_name, "rb")
    model = cPickle.load(stream)
    stream.close()
    return model


def save(file_name, model):
    # save the model
    stream = gzip.open(file_name, "wb")
    cPickle.dump(model, stream)
    stream.close()

cont = "y"

while cont == "y":
    name = raw_input("Who goes there?\n")
    names = load("./nameslist")
    quotes = load("./quoteslist")
    if name in names:
        print quotes[names.index(name)]
    else:
        names.append(name)
        quotes.append(raw_input("Name not in library\nWhat should I say to " + name + "?"))

    save("./nameslist", names)
    save("./quoteslist", quotes)
    cont = raw_input("Keep going?(y/n)")

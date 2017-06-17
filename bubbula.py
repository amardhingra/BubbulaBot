from chatterbot import ChatBot


class Bubbula(ChatBot):
    def __init__(self, corpus):
        ChatBot.__init__(self, 'Bubbula',
                         trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
                         silence_performance_warning=True)
        self.train(corpus)


def main():
    bot = Bubbula("chatterbot.corpus.english")
    print bot.get_response("What do you think of the world?")
    print bot.get_response("Really?")


if __name__ == '__main__':
    main()

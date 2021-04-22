import config
from publisher.bot_runner import BotRunner


def main():
    runner = BotRunner(config.BOT_TOKEN)
    runner.run()


if __name__ == '__main__':
    exit(main())

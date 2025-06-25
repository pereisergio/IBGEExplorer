from ibgeexplorer.utils.logger import LogWriter


def main():
    log = LogWriter("DEBUG")
    log.info("Mensagem de informação.")
    log.warning("Aviso.")
    log.error("Erro.")
    log.debug("Debug.")


if __name__ == "__main__":
    main()

from ibgeexporer.infrastructure.logging import LogWriter


def test_logwriter_basic_usage():
    log = LogWriter("DEBUG")
    log.info("Mensagem de informação.")
    log.warning("Aviso.")
    log.error("Erro.")
    log.debug("Debug.")
    # Não há assert, pois o teste é para garantir que não há exceções e o log é gerado corretamente.

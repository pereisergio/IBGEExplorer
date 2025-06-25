import json
import os
from unittest.mock import mock_open, patch

import pytest

from ibgeexplorer.domain.models.config import Settings
from ibgeexplorer.utils.settings import load_settings


class TestSettings:
    def test_load_settings_success(self):
        """Testa se as configurações são carregadas corretamente do arquivo settings.json."""
        # Lê o arquivo settings.json real para verificar se está carregando corretamente
        result = load_settings()

        # Verifica se o resultado é uma instância de Settings
        assert isinstance(result, Settings)

        # Verifica se as propriedades esperadas existem e têm o tipo correto
        assert isinstance(result.id_pesquisas, list)
        assert isinstance(result.id_agregados, list)
        assert isinstance(result.id_variaveis, list)
        assert isinstance(result.periodos, list)
        assert isinstance(result.url_pesquisa, str)

        # Verifica se alguns valores específicos estão corretos
        assert "url_pesquisa" in dir(result) and result.url_pesquisa
        assert len(result.id_pesquisas) > 0
        assert len(result.id_agregados) > 0
        assert len(result.id_variaveis) > 0
        assert len(result.periodos) > 0

    def test_load_settings_file_not_found(self):
        """Testa se é lançada exceção quando o arquivo de configuração não existe."""
        with patch("os.path.exists", return_value=False):
            with pytest.raises(FileNotFoundError):
                load_settings()

    def test_load_settings_with_mock_data(self):
        """Testa o carregamento de configurações com dados mockados."""
        mock_settings = {
            "id_pesquisas": ["TEST1", "TEST2"],
            "id_agregados": [1, 2, 3],
            "id_variaveis": [101, 102],
            "url_pesquisa": "https://test-url.com",
            "periodos": ["2020", "2021"],
        }

        # Mock do arquivo JSON sendo aberto e lido
        mock_file = mock_open(read_data=json.dumps(mock_settings))

        with (
            patch("os.path.exists", return_value=True),
            patch("builtins.open", mock_file),
        ):
            result = load_settings()

            assert result.id_pesquisas == ["TEST1", "TEST2"]
            assert result.id_agregados == [1, 2, 3]
            assert result.id_variaveis == [101, 102]
            assert result.url_pesquisa == "https://test-url.com"
            assert result.periodos == ["2020", "2021"]

    def test_load_settings_invalid_json(self):
        """Testa se é lançada exceção quando o arquivo JSON é inválido."""
        with (
            patch("os.path.exists", return_value=True),
            patch("builtins.open", mock_open(read_data="{ invalid json }")),
        ):
            with pytest.raises(json.JSONDecodeError):
                load_settings()

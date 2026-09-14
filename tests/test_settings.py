import pytest

from steam_trade_monitor.config.settings import Settings


def test_carrega_configuracoes(monkeypatch):
    monkeypatch.setattr(
        "steam_trade_monitor.config.settings.load_dotenv",
        lambda: None,
    )
    monkeypatch.setenv("STEAM_API_KEY", "chave-ficticia")
    monkeypatch.setenv("STEAM_ID", "76561198000000000")

    settings = Settings()

    assert settings.steam_api_key == "chave-ficticia"
    assert settings.steam_id == "76561198000000000"


def test_steam_id_pode_ser_opcional(monkeypatch):
    monkeypatch.setattr(
        "steam_trade_monitor.config.settings.load_dotenv",
        lambda: None,
    )
    monkeypatch.setenv("STEAM_API_KEY", "chave-ficticia")
    monkeypatch.delenv("STEAM_ID", raising=False)

    settings = Settings()

    assert settings.steam_api_key == "chave-ficticia"
    assert settings.steam_id is None


def test_api_key_e_obrigatoria(monkeypatch):
    monkeypatch.setattr(
        "steam_trade_monitor.config.settings.load_dotenv",
        lambda: None,
    )
    monkeypatch.delenv("STEAM_API_KEY", raising=False)

    with pytest.raises(ValueError):
        Settings()
import pytest

from steam_trade_monitor.models.item import Item, TradeSide


def test_cria_item_valido():
    item = Item(
        appid=730,
        classid="123456",
        name="AK-47 | Redline",
        side=TradeSide.RECEIVED,
    )

    assert item.appid == 730
    assert item.classid == "123456"
    assert item.name == "AK-47 | Redline"
    assert item.side == TradeSide.RECEIVED
    assert item.quantity == 1


def test_cria_item_com_quantidade_informada():
    item = Item(
        appid=730,
        classid="123456",
        name="Chave",
        side=TradeSide.SENT,
        quantity=3,
    )

    assert item.quantity == 3


def test_nao_permite_nome_vazio():
    with pytest.raises(ValueError):
        Item(
            appid=730,
            classid="123456",
            name="   ",
            side=TradeSide.RECEIVED,
        )


def test_nao_permite_quantidade_invalida():
    with pytest.raises(ValueError):
        Item(
            appid=730,
            classid="123456",
            name="Chave",
            side=TradeSide.RECEIVED,
            quantity=0,
        )


def test_nao_permite_lado_invalido():
    with pytest.raises(ValueError):
        Item(
            appid=730,
            classid="123456",
            name="Chave",
            side="qualquer coisa",
        )
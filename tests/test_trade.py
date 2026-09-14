from steam_trade_monitor.models.item import Item, TradeSide
from steam_trade_monitor.models.trade import Trade, TradeStatus


def test_cria_trade_sem_itens():
    trade = Trade(
        offer_id="123456789",
        sender_id="76561198000000000",
    )

    assert trade.offer_id == "123456789"
    assert trade.sender_id == "76561198000000000"
    assert trade.message == ""
    assert trade.status == TradeStatus.UNKNOWN
    assert trade.received_items == []
    assert trade.sent_items == []
    assert trade.offer_url is None


def test_cria_trade_com_itens_dos_dois_lados():
    received_item = Item(
        appid=730,
        classid="received-class",
        name="AK-47 | Redline",
        side=TradeSide.RECEIVED,
    )

    sent_item = Item(
        appid=730,
        classid="sent-class",
        name="AWP | Asiimov",
        side=TradeSide.SENT,
    )

    trade = Trade(
        offer_id="123456789",
        sender_id="76561198000000000",
        message="Boa troca!",
        status=TradeStatus.PENDING,
        received_items=[received_item],
        sent_items=[sent_item],
        offer_url="https://steamcommunity.com/tradeoffer/123456789",
    )

    assert trade.message == "Boa troca!"
    assert trade.status == TradeStatus.PENDING
    assert trade.received_items == [received_item]
    assert trade.sent_items == [sent_item]
    assert trade.offer_url == (
        "https://steamcommunity.com/tradeoffer/123456789"
    )


def test_trade_pode_ter_apenas_itens_recebidos():
    received_item = Item(
        appid=730,
        classid="received-class",
        name="Chave",
        side=TradeSide.RECEIVED,
    )

    trade = Trade(
        offer_id="123456789",
        sender_id="76561198000000000",
        received_items=[received_item],
    )

    assert trade.received_items == [received_item]
    assert trade.sent_items == []


def test_trade_pode_ter_apenas_itens_enviados():
    sent_item = Item(
        appid=730,
        classid="sent-class",
        name="Chave",
        side=TradeSide.SENT,
    )

    trade = Trade(
        offer_id="123456789",
        sender_id="76561198000000000",
        sent_items=[sent_item],
    )

    assert trade.received_items == []
    assert trade.sent_items == [sent_item]


def test_trades_nao_compartilham_a_mesma_lista():
    trade_a = Trade(
        offer_id="111",
        sender_id="sender-a",
    )

    trade_b = Trade(
        offer_id="222",
        sender_id="sender-b",
    )

    item = Item(
        appid=730,
        classid="class-id",
        name="Chave",
        side=TradeSide.RECEIVED,
    )

    trade_a.received_items.append(item)

    assert trade_a.received_items == [item]
    assert trade_b.received_items == []
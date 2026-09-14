from datetime import datetime
from enum import Enum
from .item import Item


class TradeStatus(str, Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    DECLINED = "declined"
    CANCELED = "canceled"
    UNKNOWN = "unknown"


class Trade:
    def __init__(self, offer_id: str,
                sender_id: str,
                message: str = "",
                status: TradeStatus = TradeStatus.UNKNOWN,
                received_at: datetime | None = None,
                detected_at: datetime | None = None,
                received_items: list[Item] | None = None,
                sent_items: list[Item] | None = None,
                offer_url: str | None = None,
                ) -> None:
        self.offer_id = offer_id
        self.sender_id = sender_id
        self.message = message
        self.status = status
        self.received_at = received_at
        self.detected_at = detected_at
        self.received_items = (
            list(received_items) if received_items is not None else []
        )
        self.sent_items = (
            list(sent_items) if sent_items is not None else []
        )
        self.offer_url = offer_url
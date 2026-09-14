from enum import Enum  

class TradeSide(str, Enum):
    RECEIVED = "received"
    SENT = "sent"


class Item:
    def __init__(self, appid: int,
                  classid: str, 
                  name: str, 
                  side: TradeSide, 
                  quantity: int = 1, 
                  asset_id: str | None = None, 
                  image_url: str | None = None,
    ) -> None:
        if not name.strip():
            raise ValueError("O item precisa ter um nome.")
        if quantity <= 0:
            raise ValueError("A quantidade do item precisa ser maior que zero.")
        if not isinstance(side, TradeSide):
            raise ValueError("O lado deve ser Received ou Sent.")
        self.appid = appid
        self.classid = classid
        self.name = name
        self.side = side
        self.quantity = quantity
        self.asset_id = asset_id
        self.image_url = image_url

from typing import Any, TypeVar, Type, cast

T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class QrModel:
    id: int
    tipo: str
    valor: str

    def __init__(self, id: int, tipo: str, valor: str) -> None:
        self.id = id
        self.tipo = tipo
        self.valor = valor

    @staticmethod
    def from_dict(obj: Any) -> 'QrModel':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        tipo = from_str(obj.get("tipo"))
        valor = from_str(obj.get("valor"))
        return QrModel(id, tipo, valor)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["tipo"] = from_str(self.tipo)
        result["valor"] = from_str(self.valor)
        return result


def search_response_from_dict(s: Any) -> QrModel:
    return QrModel.from_dict(s)


def search_response_to_dict(x: QrModel) -> Any:
    return to_class(QrModel, x)

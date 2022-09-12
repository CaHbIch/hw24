from dataclasses import dataclass
from typing import Union

from marshmallow import ValidationError # type: ignore

from config import COMMANDS


@dataclass
class Commands:
    cmd1: str
    value1: Union[str, int]
    cmd2: str
    value2: Union[str, int]

    def __validate(self) -> None:
        """Проверка полей и объединение команд"""
        if self.cmd1 not in COMMANDS:
            raise ValidationError(f'Команда прошла как cmd1 ({self.cmd1}) недопустимая команда. '
                                  f'Только {", ".join(COMMANDS)} допустимый')
        if self.cmd2 not in COMMANDS:
            raise ValidationError(f'Команда прошла как as cmd2 ({self.cmd2}) недопустимая команда. '
                                  f'Только {", ".join(COMMANDS)} допустимый')


CommandsSchema = marshmallow_dataclass.class_schema(Commands) # type: ignore

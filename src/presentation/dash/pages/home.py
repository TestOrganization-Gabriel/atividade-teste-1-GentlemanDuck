from dash.development.base_component import Component
from src.init import get_message_repository
from src.presentation.dash.component.history import HistoryComponent
from src.usecase.history import HistoryUsecase


def layout() -> Component:
    message_repository = get_message_repository()
    messages = HistoryUsecase(message_repository).execute()
    return HistoryComponent(messages)

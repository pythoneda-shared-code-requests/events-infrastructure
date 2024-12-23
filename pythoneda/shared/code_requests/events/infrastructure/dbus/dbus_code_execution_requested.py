# vim: set fileencoding=utf-8
"""
pythoneda/shared/code_requests/events/infrastructure/dbus/dbus_code_execution_requested.py

This file defines the DbusCodeExecutionRequested class.

Copyright (C) 2023-today rydnr's pythoneda-shared-code-requests/events-infrastructure

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from dbus_next import Message
from dbus_next.service import signal
import json
from pythoneda.shared import Event
from pythoneda.shared.infrastructure.dbus import DbusEvent
from pythoneda.shared.code_requests.events import CodeExecutionRequested
from pythoneda.shared.code_requests.events.infrastructure.dbus import DBUS_PATH
from typing import List, Type


class DbusCodeExecutionRequested(DbusEvent):
    """
    D-Bus interface for CodeExecutionRequested

    Class name: DbusCodeExecutionRequested

    Responsibilities:
        - Define the d-bus interface for the CodeExecutionRequested event.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DbusCodeExecutionRequested.
        """
        super().__init__("Pythoneda_CodeRequests_CodeExecutionRequested")

    @signal()
    def CodeExecutionRequested(self, codeRequest: "s"):
        """
        Defines the CodeExecutionRequested d-bus signal.
        :param codeRequest: The code request.
        :type codeRequest: str
        """
        pass

    @property
    def path(self) -> str:
        """
        Retrieves the d-bus path.
        :return: Such value.
        :rtype: str
        """
        return DBUS_PATH

    @classmethod
    def transform(cls, event: CodeExecutionRequested) -> List[str]:
        """
        Transforms given event to signal parameters.
        :param event: The event to transform.
        :type event: pythoneda.shared.code_requests.events.CodeExecutionRequested
        :return: The event information.
        :rtype: List[str]
        """
        return [
            event.code_request,
            json.dumps(event.previous_event_ids),
            event.id,
        ]

    @classmethod
    def sign(cls, event: CodeExecutionRequested) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: pythoneda.shared.code_requests.events.CodeExecutionRequested
        :return: The signature.
        :rtype: str
        """
        return "sss"

    @classmethod
    def parse(cls, message: Message) -> CodeExecutionRequested:
        """
        Parses given d-bus message containing a CodeExecutionRequested event.
        :param message: The message.
        :type message: dbus_next.Message
        :return: The CodeExecutionRequested event.
        :rtype: pythoneda.shared.code_requests.events.CodeExecutionRequested
        """
        code_request, prev_event_ids, event_id = message.body
        return CodeExecutionRequested(
            code_request,
            json.loads(prev_event_ids),
            event_id,
        )

    @classmethod
    def event_class(cls) -> Type[Event]:
        """
        Retrieves the specific event class.
        :return: Such class.
        :rtype: type(pythoneda.shared.Event)
        """
        return CodeExecutionRequested


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:

# vim: set fileencoding=utf-8
"""
pythoneda/shared/code_requests/events/infrastructure/dbus/dbus_code_described.py

This file defines the DbusCodeDescribed class.

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
from pythoneda.shared.code_requests.events import CodeDescribed
from pythoneda.shared.code_requests.events.infrastructure.dbus import DBUS_PATH
from typing import List, Type


class DbusCodeDescribed(DbusEvent):
    """
    D-Bus interface for CodeDescribed

    Class name: DbusCodeDescribed

    Responsibilities:
        - Define the d-bus interface for the CodeDescribed event.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DbusCodeDescribed.
        """
        super().__init__("Pythoneda_CodeRequests_CodeDescribed")

    @signal()
    def CodeDescribed(self, codeRequest: "s"):
        """
        Defines the CodeDescribed d-bus signal.
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
    def transform(cls, event: CodeDescribed) -> List[str]:
        """
        Transforms given event to signal parameters.
        :param event: The event to transform.
        :type event: pythoneda.shared.code_requests.events.CodeDescribed
        :return: The event information.
        :rtype: List[str]
        """
        return [
            event.code_request,
            json.dumps(event.previous_event_ids),
            event.id,
        ]

    @classmethod
    def sign(cls, event: CodeDescribed) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: pythoneda.shared.code_requests.events.CodeDescribed
        :return: The signature.
        :rtype: str
        """
        return "sss"

    @classmethod
    def parse(cls, message: Message) -> CodeDescribed:
        """
        Parses given d-bus message containing a CodeDescribed event.
        :param message: The message.
        :type message: dbus_next.Message
        :return: The CodeDescribed event.
        :rtype: pythoneda.shared.code_requests.events.CodeDescribed
        """
        code_request, prev_event_ids, event_id = message.body
        return CodeDescribed(
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
        return CodeDescribed


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:

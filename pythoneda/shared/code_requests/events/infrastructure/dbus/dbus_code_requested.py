# vim: set fileencoding=utf-8
"""
pythoneda/shared/code_requests/events/infrastructure/dbus/dbus_code_requested.py

This file defines the DbusCodeRequested class.

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
from dbus_next.service import ServiceInterface, signal
import json
from pythoneda.shared import BaseObject
from pythoneda.shared.code_requests.events import CodeRequested
from pythoneda.shared.code_requests.events.infrastructure.dbus import DBUS_PATH
from typing import List


class DbusCodeRequested(BaseObject, ServiceInterface):
    """
    D-Bus interface for CodeRequested

    Class name: DbusCodeRequested

    Responsibilities:
        - Define the d-bus interface for the CodeRequested event.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DbusCodeRequested.
        """
        super().__init__("Pythoneda_CodeRequests_CodeRequested")

    @signal()
    def CodeRequested(self, change: "s"):
        """
        Defines the CodeRequested d-bus signal.
        :param change: The code request.
        :type change: str
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
    def transform(cls, event: CodeRequested) -> List[str]:
        """
        Transforms given event to signal parameters.
        :param event: The event to transform.
        :type event: pythoneda.shared.code_requests.events.CodeRequested
        :return: The event information.
        :rtype: List[str]
        """
        return [
            event.change,
            json.dumps(event.previous_event_ids),
            event.id,
        ]

    @classmethod
    def sign(cls, event: CodeRequested) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: pythoneda.shared.code_requests.events.CodeRequested
        :return: The signature.
        :rtype: str
        """
        return "sss"

    @classmethod
    def parse(cls, message: Message) -> CodeRequested:
        """
        Parses given d-bus message containing a CodeRequested event.
        :param message: The message.
        :type message: dbus_next.Message
        :return: The CodeRequested event.
        :rtype: pythoneda.shared.code_requests.events.CodeRequested
        """
        change, event_id, prev_event_ids = message.body
        return CodeRequested(
            change,
            json.loads(prev_event_ids),
            event_id,
        )


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:

# vim: set fileencoding=utf-8
"""
pythoneda/shared/code_requests/events/infrastructure/dbus/dbus_code_execution_packaged.py

This file defines the DbusCodeExecutionPackaged class.

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
from pythoneda.shared.code_requests.events import CodeExecutionPackaged
from pythoneda.shared.code_requests.events.infrastructure.dbus import DBUS_PATH
from typing import List


class DbusCodeExecutionPackaged(BaseObject, ServiceInterface):
    """
    D-Bus interface for CodeExecutionPackaged

    Class name: DbusCodeExecutionPackaged

    Responsibilities:
        - Define the d-bus interface for the CodeExecutionPackaged event.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DbusCodeExecutionPackaged.
        """
        super().__init__("Pythoneda_CodeRequests_CodeExecutionPackaged")

    @signal()
    def CodeExecutionPackaged(self, nixFlake: "s"):
        """
        Defines the CodeExecutionPackaged d-bus signal.
        :param nixFlake: The Nix flake.
        :type nixFlake: str
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
    def transform(cls, event: CodeExecutionPackaged) -> List[str]:
        """
        Transforms given event to signal parameters.
        :param event: The event to transform.
        :type event: pythoneda.shared.code_requests.events.CodeExecutionPackaged
        :return: The event information.
        :rtype: List[str]
        """
        return [
            event.nix_flake,
            json.dumps(event.previous_event_ids),
            event.id,
        ]

    @classmethod
    def sign(cls, event: CodeExecutionPackaged) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: pythoneda.shared.code_requests.events.CodeExecutionPackaged
        :return: The signature.
        :rtype: str
        """
        return "sss"

    @classmethod
    def parse(cls, message: Message) -> CodeExecutionPackaged:
        """
        Parses given d-bus message containing a CodeExecutionPackaged event.
        :param message: The message.
        :type message: dbus_next.Message
        :return: The CodeExecutionPackaged event.
        :rtype: pythoneda.shared.code_requests.events.CodeExecutionPackaged
        """
        nix_flake, prev_event_ids, event_id = message.body
        return CodeExecutionPackaged(
            nix_flake,
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

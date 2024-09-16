class IPerson:
    def __init__(self, role: str) -> None:
        self._role = role

    def print_role(self) -> None:
        raise NotImplementedError

    @property
    def role(self) -> str:
        return self._role

class DomainError(Exception):
    pass
class ConfigError(DomainError):
    pass
class InvalidFilenameError(DomainError):
    pass
class InvalidFilterError(DomainError):
    pass
class EntityNotFoundError(DomainError):
    pass
from typing import Any, List, Optional, Set, Tuple, Dict

from django.db.models.manager import Manager

class ModelBase(type): ...

class Model(metaclass=ModelBase):
    class DoesNotExist(Exception):
        pass
    pk: Any = ...
    objects: Manager[Model]
    def __init__(self, *args, **kwargs) -> None: ...
    def delete(self, using: Any = ..., keep_parents: bool = ...) -> Tuple[int, Dict[str, int]]: ...
    def full_clean(self, exclude: Optional[List[str]] = ..., validate_unique: bool = ...) -> None: ...
    def clean_fields(self, exclude: List[str] = ...) -> None: ...
    def validate_unique(self, exclude: List[str] = ...) -> None: ...
    def save(
        self,
        force_insert: bool = ...,
        force_update: bool = ...,
        using: Optional[str] = ...,
        update_fields: Optional[List[str]] = ...,
    ) -> None: ...
    def refresh_from_db(self, using: None = ..., fields: Optional[List[str]] = ...) -> None: ...
    def get_deferred_fields(self) -> Set[str]: ...

class ModelStateFieldsCacheDescriptor: ...

class ModelState:
    db: None = ...
    adding: bool = ...
    fields_cache: ModelStateFieldsCacheDescriptor = ...

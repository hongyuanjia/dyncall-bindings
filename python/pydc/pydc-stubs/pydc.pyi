import sys
from typing import Optional, Any, TypeVar

# Handle type is different, depending on python version
if sys.version_info < (2, 7) or (sys.version_info >= (3, 0) and sys.version_info < (3, 1)):
    H = TypeVar('H', PyCObject)
else:
    H = TypeVar('H', PyCapsule)

def load(libpath: Optional[str]) -> H: ...
def find(libhandle: H, symbol: str) -> H: ...
def free(libhandle: H) -> None: ...
def get_path(libhandle: Optional[H]) -> str: ...
def call(funcptr: H, signature: str, *arguments: Any) -> Any: ...


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Tuple, Union

    VERSION_TUPLE = Tuple[Union[int, str], ...]
else:
    VERSION_TUPLE = object

version: str
__version__: str
__version_tuple__: VERSION_TUPLE
version_tuple: VERSION_TUPLE

# TODO: this is the only place you update the package version
__version__ = version = '0.0.1'
__version_tuple__ = version_tuple = tuple(map(int, version.split('.')))

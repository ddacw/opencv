import numpy as np

from typing import (
    Any,
    overload,
    Sequence,
    Tuple,
)

Size = Tuple[int, int]
Mat = np.ndarray
InputArray = np.ndarray
OutputArray = np.ndarray


# videoio
class VideoCapture:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(
            self,
            filename: str,
            apiPreference: int = ...
    ) -> None: ...

    @overload
    def __init__(
            self,
            filename: str,
            params: Sequence[int]
    ) -> None: ...

    @overload
    def __init__(
            self,
            index: int,
            apiPreference: int = ...
    ) -> None: ...

    @overload
    def __init__(
            self,
            index: int,
            apiPreference: int,
            params: Sequence[int]
    ) -> None: ...

    def get(self, propId: int) -> float: ...

    def getBackendName(self) -> str: ...

    def getExceptionMode(self) -> bool: ...

    def grab(self) -> bool: ...

    def isOpened(self) -> bool: ...

    @overload
    def open(
            self,
            filename: str,
            apiPreference: int = ...
    ) -> bool: ...

    @overload
    def open(
            self,
            filename: str,
            apiPreference: int,
            params: Sequence[int]
    ) -> bool: ...

    @overload
    def open(
            self,
            index: int,
            apiPreference: int = ...
    ) -> bool: ...

    @overload
    def open(
            self,
            index: int,
            apiPreference: int,
            params: Sequence[int]
    ) -> bool: ...

    def read(self, image: OutputArray = None) -> Tuple[bool, OutputArray]: ...

    def release(self) -> None: ...

    def retrieve(
            self,
            image: OutputArray = None,
            flag: int = 0
    ) -> Tuple[bool, OutputArray]: ...

    def set(self, propId: int, value: float) -> bool: ...

    def setExceptionMode(self, enable: bool) -> None: ...


class VideoWriter:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(
            self,
            filename: str,
            fourcc: int,
            fps: float,
            frameSize: Size,
            isColor: bool = True
    ) -> None: ...

    @overload
    def __init__(
            self,
            filename: str,
            fourcc: int,
            fps: float,
            frameSize: Size,
            isColor: bool = True
    ) -> None: ...

    @overload
    def __init__(
            self,
            filename: str,
            apiPreference: int,
            fourcc: int,
            fps: float,
            frameSize: Size,
            isColor: bool = True
    ) -> None: ...

    @overload
    def __init__(
            self,
            filename: str,
            fourcc: int,
            fps: float,
            frameSize: Size,
            params: Sequence[int]
    ) -> None: ...

    @overload
    def __init__(
            self,
            filename: str,
            apiPreference: int,
            fourcc: int,
            fps: float,
            frameSize: Size,
            params: Sequence[int]
    ) -> None: ...

    @staticmethod
    def fourcc(c1: str, c2: str, c3: str, c4: str) -> int: ...

    def get(self, propId: int) -> float: ...

    def getBackendName(self) -> str: ...

    def isOpened(self) -> bool: ...

    @overload
    def open(
            self,
            filename: str,
            fourcc: int,
            fps: float,
            frameSize: Size,
            isColor: bool = True
    ) -> bool: ...

    @overload
    def open(
            self,
            filename: str,
            apiPreference: int,
            fourcc: int,
            fps: float,
            frameSize: Size,
            isColor: bool = True
    ) -> bool: ...

    @overload
    def open(
            self,
            filename: str,
            fourcc: int,
            fps: float,
            frameSize: Size,
            params: Sequence[int]
    ) -> bool: ...

    @overload
    def open(
            self,
            filename: str,
            apiPreference: int,
            fourcc: int,
            fps: float,
            frameSize: Size,
            params: Sequence[int]
    ) -> bool: ...

    def release(self) -> None: ...

    def set(self, propId: int, value: float) -> bool: ...

    def write(self, image: InputArray) -> None: ...


# imgcodecs
def haveImageReader(filename: str) -> bool: ...


def haveImageWriter(filename: str) -> bool: ...


def imcount(filename: str, flags: int = ...) -> int: ...


def imdecode(buf: InputArray, flags: int) -> Mat: ...


def imencode(
        ext: str,
        img: InputArray,
        params: Sequence[int] = ()
) -> Tuple[bool, np.ndarray]: ...


def imread(filename: str, flags: int = ...) -> Mat: ...


@overload
def imreadmulti(
        filename: str,
        mats: Sequence[Mat] = None,
        flags: int = ...
) -> Tuple[bool, List[Mat]]: ...


@overload
def imreadmulti(
        filename: str,
        start: int,
        count: int,
        mats: Sequence[Mat] = None,
        flags: int = ...
) -> Tuple[bool, List[Mat]]: ...


def imwrite(
        filename: str,
        img: InputArray,
        params: Sequence[int] = ()
) -> bool: ...


def imwritemulti(
        filename: str,
        img: InputArray,
        params: Sequence[int] = ()
) -> bool: ...

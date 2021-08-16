  
import json
from typing import AbstractSet, Any, Iterable, Mapping, Optional, Set, Union

from bson.json_util import dumps, loads

JSONType = Mapping[str, Any]


def success(operation: str, msg: str, data: Optional[JSONType] = None) -> JSONType:
    """
    This function returns a formatted dictionary for the successful cases.
    Args:
        operation (str): Operation successfully completed
        msg (str): Sucessful Message
        data (Optional[JSONType], optional): Data to be sent. Defaults to None.
    Returns:
        JSONType: Formatted Dictionary
    """
    return {
        "operation": operation,
        "success": True,
        "message": msg,
        "data": data,
    }


def failure(operation: str, msg: str) -> Mapping[str, Union[str, bool]]:
    """
    This function returns a formatted dictionary for the failure cases, or exceptions.
    Args:
        operation (str): Operation that failed
        msg (str): Failure Message
    Returns:
        Mapping[str, Union[str, bool]]: Formatted Dictionary
    """
    return {
        "operation": operation,
        "success": False,
        "message": msg,
    }



image_extensions = {"png", "jpg", "jpeg", "gif", "bmp", "svg"}

def is_image(filename: str) -> str:
    """
    Checks if the filename if that of a valid image
    Args:
        filename (str): Filename to be checked
    Returns:
        str: Extension of the filename if valid else gives assertion error
    """
    extension = filename.rsplit(".", 1)[-1].lower()
    assert (
        extension in image_extensions
    ), f"Invalid image: {filename}. Allowed extensions: {image_extensions}"
    return extension


pdf_extensions = {"pdf"}

def is_pdf(filename: str) -> str:
    """
    Checks if the filename if that of a valid image
    Args:
        filename (str): Filename to be checked
    Returns:
        str: Extension of the filename if valid else gives assertion error
    """
    extension = filename.rsplit(".", 1)[-1].lower()
    assert (
        extension in pdf_extensions
    ), f"Invalid pdf: {filename}. Allowed extensions: {pdf_extensions}"
    return extension


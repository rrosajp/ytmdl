"""Store all the exceptions related to ytmdl that might
arise during the runtime of the app
"""


class DownloadError(Exception):
    """Exception for download error.

    This exception is solely for those cases when
    the download fails for some reason.
    """
    def __init__(self, link, error) -> None:
        super().__init__()

        self.__message = self.__build_message(link, error)

    def __build_message(self, link, error) -> str:
        """Build the error message."""
        return "Download failed for `{}` with error: {}".format(
            link, error
        )

    def __str__(self) -> str:
        return self.__message


class ConvertError(Exception):
    """Exception for conversion erros.

    This exception is raised whenever the conversion goes wrong,
    mostly while using ffmpeg or something similar.
    """
    def __init__(self, error) -> None:
        super().__init__()

        self.__message = self.__build_message(error)

    def __build_message(self, error) -> str:
        """Build the error message"""
        return "Conversion failed with error: {}".format(error)

    def __str__(self) -> str:
        return self.__message

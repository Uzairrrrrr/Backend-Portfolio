# encoding=utf-8
""" API path handling """

from typing import List, Tuple

name = "api-utils"


def join(first: str, *others: str) -> str:
    """
	Join one or more path components intelligently.

	Rules:
    - If any component starts with "http", all previous parts will be discarded.
	- The returned path will always start with "/", except if it starts with "http".
	- The returned path will never end with "/", except when ending in a protocol
      notation ("://") or enforced (see below)
	- A trailing slash can be enforced with a final component "/"
	- Empty strings are skipped
	"""

    all_components: List[str] = [first, *others]

    if any([type(x) not in [str, bytes] for x in all_components]):
        raise TypeError("expected str or bytes objects")

    sep = "/"
    final_sep: bool = all_components[-1] == sep

    final_path: str = sep

    for comp in all_components:
        if comp == "":
            continue

        assert final_path.endswith(sep)

        remove_start_sep: bool = comp[0] == sep and final_path.endswith(sep)
        append_end_sep: bool = comp[-1] != sep

        # Absolute path: Reset path
        if comp.startswith("http"):
            final_path = ""
            remove_start_sep = False

        if remove_start_sep:
            comp = comp[1:]

        if append_end_sep:
            comp += sep

        final_path += comp

    # Final sep allowed if enforced or if just a protocol
    if not final_sep and not final_path.endswith("://"):
        final_path = final_path[:-1]

    return final_path

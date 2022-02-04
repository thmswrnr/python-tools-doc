import cv2
import numpy.typing as npt


def grayscale(img: npt.NDArray, inplace: bool = True) -> npt.NDArray:
    n_dim = len(img.shape)

    if not inplace:
        out = img.copy()
    else:
        out = img

    if n_dim == 1:
        raise ValueError("Image does not have enough dimension (must be > 1).")

    if n_dim == 3:
        out = cv2.cvtColor(out, cv2.COLOR_BGR2GRAY)

    if n_dim == 4:
        out = cv2.cvtColor(out, cv2.COLOR_BGR2GRAY)

    return out


def align_to_template(
    img: npt.NDArray, template: npt.NDArray, alignment: str
) -> npt.NDArray:
    raise NotImplementedError

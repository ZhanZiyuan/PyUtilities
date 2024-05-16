#!/usr/bin/env python
# -*- coding:utf-8 -*-

from base64 import b64decode, b64encode
from pathlib import Path
from typing import Union

import numpy as np
from numpy.random import default_rng
from PIL import Image


def encode_base64(image_to_encode: str,
                  encoded_text: Union[str, Path] = Path(__file__).with_suffix(".txt")) -> None:
    """
    Encode the input image as a Base64 string.
    """
    with open(image_to_encode, "rb") as image_file:
        encoded_string = b64encode(image_file.read()).decode("utf-8")
        with open(encoded_text, "w", encoding="utf-8") as text_file:
            text_file.write(encoded_string)


def decode_base64(encoded_text: str,
                  decoded_image: Union[str, Path] = Path(__file__).with_suffix(".png")) -> None:
    """
    Decode the input Base64 string into an image.
    """
    with open(encoded_text, "r", encoding="utf-8") as text_file:
        decoded_output = b64decode(text_file.read())
        with open(decoded_image, "wb") as image_file:
            image_file.write(decoded_output)


def shuffle_pixels(origin_image: str,
                   shuffled_image: str,
                   index_file: Union[str, Path] = Path(__file__).with_suffix(".npy"),
                   dimension: int = 0,
                   seed: Union[int, None] = None) -> None:
    """
    Shuffle the arrangement of pixels in a specified dimension.
    """
    rng = default_rng(seed)

    pixel_array = np.array(
        Image.open(origin_image)
    )
    indices_shuffled = rng.permutation(
        pixel_array.shape[dimension]
    )

    np.save(index_file, indices_shuffled)

    shuffled_output = Image.fromarray(
        np.take(
            pixel_array,
            indices_shuffled,
            axis=dimension
        )
    )
    shuffled_output.save(shuffled_image)


def recover_pixels(shuffled_image: str,
                   recovered_image: str,
                   index_file: Union[str, Path] = Path(__file__).with_suffix(".npy"),
                   dimension: int = 0) -> None:
    """
    Recover the arrangement of pixels in a specified dimension.
    """
    pixel_array = np.array(
        Image.open(shuffled_image)
    )

    indices_recovered = np.argsort(
        np.load(index_file)
    )

    recovered_output = Image.fromarray(
        np.take(
            pixel_array,
            indices_recovered,
            axis=dimension
        )
    )
    recovered_output.save(recovered_image)


if __name__ == "__main__":

    path_of_original_image = "C:/Users/user/Downloads/original.jpg"
    path_of_text = "C:/Users/user/Downloads/key.txt"
    path_of_decoded_image = "C:/Users/user/Downloads/decoded.jpg"
    path_of_arr = "C:/Users/user/Downloads/pixels.npy"
    path_of_shuffled_image = "C:/Users/user/Downloads/shuffled.jpg"
    path_of_recovered_image = "C:/Users/user/Downloads/recovered.jpg"

    encode_base64(
        path_of_original_image,
        path_of_text
    )

    decode_base64(
        path_of_text,
        path_of_decoded_image
    )

    shuffle_pixels(
        path_of_original_image,
        path_of_shuffled_image,
        path_of_arr,
        dimension=1,
        seed=None
    )

    recover_pixels(
        path_of_shuffled_image,
        path_of_recovered_image,
        path_of_arr,
        dimension=1
    )

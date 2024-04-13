#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
TODO:

1. threading & multiprocessing
2. exe
"""

import argparse
from pathlib import Path
from time import sleep, time
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


class WebDownloader(object):
    """
    ``WebDownloader``
    =================

    A class to download elements from a specified website.

    Attributes
    ----------
    website_url: string
        The URL of the website to be crawled.
    folder_path: string
        The directory to store the downloaded elements.
    element_tag: string
        The tag of elements to be filtered.
        Default is "img".
    requests_per_minute: integer
        The number of requests to the specified URL per minute.
        Default is 10.
    last_request_time: float
        The time of the last request made to the website.
    """

    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"
    }

    def __init__(self,
                 website_url: str,
                 folder_path: str,
                 element_tag: str = "img",
                 requests_per_minute: int = 10) -> None:
        """
        Initialize the WebDownloader object.
        """
        self.website_url = website_url
        self.folder_path = folder_path
        self.element_tag = element_tag
        self.requests_per_minute = requests_per_minute
        self.last_request_time = 0.0

    def _check_folder_path(self) -> Path:
        """
        Check if the directory to the input file exists.
        """
        if not Path(self.folder_path).exists():
            Path(self.folder_path).mkdir(
                parents=True,
                exist_ok=True
            )
        return Path(self.folder_path)

    def _rename_duplicate_files(self, file_name: str) -> str:
        """
        Rename files if their names are the same.

        Args
        ----
        file_name: str
            The original file name.
        """
        folder_path = self._check_folder_path()
        base_name = Path(file_name).stem
        extension = Path(file_name).suffix

        i = 1
        while (folder_path / file_name).exists():
            file_name = f"{base_name}_({i}){extension}"
            i += 1
        return file_name

    @staticmethod
    def _make_request(url: str) -> requests.Response:
        """
        Make a request to the specified URL.

        Args
        ----
        url: string
            The URL to make the request to.
        """
        return requests.get(
            url=url,
            headers=WebDownloader.headers,
            timeout=10
        )

    def download_single_element(self, url: str) -> None:
        """
        Download a single element from the specified URL.

        Args
        ----
        url: string
            The URL of the element to be downloaded.
        """
        current_time = time()

        if current_time - self.last_request_time < 60 / self.requests_per_minute:
            sleep(
                60/self.requests_per_minute
                - (current_time - self.last_request_time)
            )

        response = WebDownloader._make_request(url)

        if response.status_code == 200:
            updated_file_name = self._rename_duplicate_files(Path(url).name)
            full_file_path = self._check_folder_path() / updated_file_name
            with open(full_file_path, "wb") as file_object:
                file_object.write(response.content)
                print(f"Downloaded: {updated_file_name}")
            self.last_request_time = time()

    def _modify_tag_of_elements(self) -> str:
        """
        Modify the tag of elements to be filtered.
        """
        if self.element_tag == "img":
            return "images"
        elif self.element_tag == "audio":
            return "audio"
        elif self.element_tag == "video":
            return "videos"
        else:
            raise ValueError(
                f'Incorrect tag of elements: "{self.element_tag}"'
            )

    def download_all_elements(self) -> None:
        """
        Download all elements from the specified website.
        """
        response = WebDownloader._make_request(self.website_url)

        if response.status_code == 200:
            print(
                f"Downloading {self._modify_tag_of_elements()} "
                f"from: {self.website_url}"
            )
            soup = BeautifulSoup(response.text, "html.parser")
            element_tags = soup.find_all(self.element_tag, src=True)
            for elem_tag in element_tags:
                elem_url = elem_tag.get("src")
                full_elem_url = urljoin(self.website_url, elem_url)
                self.download_single_element(full_elem_url)
            print("All downloads completed.")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Download elements from the specified website."
    )

    parser.add_argument(
        "--website_url",
        type=str,
        default="https://takanenonadeshiko.jp/",
        help="The URL to be requested."
    )
    parser.add_argument(
        "--folder_path",
        type=str,
        default="C:/Users/user/Downloads",
        help="The directory to store the downloaded elements."
    )
    parser.add_argument(
        "--element_tag",
        type=str,
        choices=["img", "audio", "video"],
        default="img",
        help="The tag of elements to be downloaded."
    )
    parser.add_argument(
        "--requests_per_minute",
        type=int,
        default=10,
        help="The number of requests to the specified URL per minute."
    )

    command_args = parser.parse_args()

    downloader = WebDownloader(
        website_url=command_args.website_url,
        folder_path=command_args.folder_path,
        element_tag=command_args.element_tag,
        requests_per_minute=command_args.requests_per_minute
    )

    downloader.download_all_elements()

#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
TODO:

1. mkdir
2. rename duplicate files
3. threading & multiprocessing
"""

import argparse
from pathlib import Path
from time import sleep, time
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


class ImageDownloader(object):
    """
    A class to download images from a specified website.

    Attributes
    ----------
    website_url: string
        The URL of the website to be crawled.
    folder_path: string
        The directory to store the downloaded images.
    requests_per_minute: integer
        The number of requests to the specified URL per minute.
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
                 requests_per_minute: int = 10) -> None:
        """
        Initialize the ImageDownloader object.
        """
        self.website_url = website_url
        self.folder_path = folder_path
        self.requests_per_minute = requests_per_minute
        self.last_request_time = 0.0

    def download_all_images(self) -> None:
        """
        Download all images from the specified website.
        """
        response = requests.get(
            url=self.website_url,
            headers=ImageDownloader.headers,
            timeout=10
        )

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            img_tags = soup.find_all("img")
            for img_tag in img_tags:
                img_url = img_tag.get("src")
                img_url = urljoin(self.website_url, img_url)
                self.download_single_image(img_url)

    def download_single_image(self, url: str) -> None:
        """
        Download a single image from the specified URL.

        Args
        ----
        url: string
            The URL of the image to be downloaded.
        """
        current_time = time()

        if current_time - self.last_request_time < 60 / self.requests_per_minute:
            sleep(
                60/self.requests_per_minute
                - (current_time - self.last_request_time)
            )

        response = requests.get(
            url=url,
            headers=ImageDownloader.headers,
            timeout=10
        )

        if response.status_code == 200:
            file_name = Path(self.folder_path) / Path(url).name
            with open(file_name, "wb") as file_object:
                file_object.write(response.content)
                print(f"Downloaded: {file_name}")
            self.last_request_time = time()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Download images from the specified website."
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
        help="The directory to store the downloaded images."
    )

    parser.add_argument(
        "--frequency_of_requests",
        type=int,
        default=10,
        help="The number of requests to the specified URL per minute."
    )

    command_args = parser.parse_args()

    downloader = ImageDownloader(
        website_url=command_args.website_url,
        folder_path=command_args.folder_path,
        requests_per_minute=command_args.frequency_of_requests
    )

    downloader.download_all_images()

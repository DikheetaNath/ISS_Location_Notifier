![NightGirlGIF](https://github.com/DikheetaNath/ISS_Location_Notifier/assets/149823138/692bb0dc-8029-4832-bb76-3acf5979e09a)# ISS Notifier

This project notifies you when the International Space Station (ISS) is overhead at your location during nighttime. The notification includes details about the ISS's visibility, allowing you to observe it from your location.🛰️🌌🔭🌌
![SkyGrayGIF](https://github.com/DikheetaNath/ISS_Location_Notifier/assets/149823138/fcda2323-8223-4ae6-9361-9c97243c928c)


## Contents
[Features](#features)
[Prerequisites](#prerequisites)
[Other Information](#other-information)
[How It Works](#how-it-works)
[API Reference](#api-reference)
[Acknowledgements](#Acknowledgements)


## Features

- Retrieves current ISS position and visibility information.
- Checks if the ISS is overhead at your location.
- Ensures notifications are sent only during nighttime.
- Sends notifications via your preferred mail address.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.x
- `requests` library
- `datetime` library
- `smtplib` or other relevant libraries for notifications

## Other Information
- Go to [Location Finder](https://www.latlong.net/) and find the latittudes and longitudes for your current address.
- Google and find the appropriate timezone for your location.

## How It Works
- Fetch ISS position:📍
  The script uses the Open Notify API to fetch the current position of the ISS.

- Check visibility:
  It calculates if the ISS is within a certain range of your location.

- Check nighttime:🌃
  It verifies if the current time at your location is nighttime based on sunset and sunrise times.

- Send notification:
  If the ISS is overhead during nighttime, it sends a notification via the configured mail.📩

## API Reference
  [Open Notify API]: Provides the current location of the ISS.

## Acknowledgements
- Thanks to Open Notify for providing the ISS position API.
- Inspired by the enthusiasm of space watchers worldwide.

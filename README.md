# ThorchainPy

<!-- Badges -->

[![Project Status: WIP -- Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://img.shields.io/badge/repo%20status-WIP-yellow.svg)](https://www.repostatus.org/#wip)
[![PyPI Version][pypi-image]][pypi-url]
[![Documentation Status][docs-badge]][docs-url]
[![Discord][discord-badge]][discord-url]
[![MIT license][license-badge]][license-link]

<!-- Badges links -->

[docs-badge]: https://img.shields.io/badge/docs-passing-green.svg
[docs-url]: https://docs.thorchain.org/
[discord-badge]: https://dcbadge.vercel.app/api/server/kvZhpEtHAw?style=flat
[discord-url]: https://discord.com/invite/c4EhDZdFMA
[pypi-image]: https://img.shields.io/pypi/v/thorchainpy
[pypi-url]: https://pypi.org/project/thorchainpy/
[license-badge]: https://img.shields.io/badge/License-MIT-blue.svg
[license-link]: /LICENSE


This is a Python SDK for querying Thorchain. It provides a convenient interface to access various functionalities of Thorchain, including getting information about pools, swaps, and more.

## Installation

You can install the Thorchain Python SDK using pip:

```bash
pip install thorchainpy
```

## Usage

Here's a simple example of how to use the SDK to query the Thorchain network:

```python
from thorchainpy import Client
from thorchainpy.api.health.ping import sync as ping

client = Client(
  base_url="https://thornode.ninerealms.com",
)

ping_result = ping(client=client)

print(ping_result)
```

For more examples, please check out the [notebook](examples/connect.ipynb).

## Documentation

The full documentation for the Thorchain Python SDK can be found on Read the Docs.

## License

The Thorchain Python SDK is licensed under the [MIT License](/LICENSE).

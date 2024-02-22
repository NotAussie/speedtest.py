## `🛜` Speedtest.py
> This project is not an offical Speedtest wrapper and therefore is not endorsed by Ookla.

Speedtest.py is a simple asynchronous wrapper for [Speedtest.net](https://www.speedtest.net/) built around the OOP coding style. We also use zero external packages/modules.

<br>

## `📥` Installing
> Speedtest.py requires the [Speedtest.net CLI](https://www.speedtest.net/apps/cli) to function.

<br>

PIP: `pip install speedtest.py`
> We're in the works of publishing to PIP.

<br>

Conda: `conda install speedtest.py`
> We're currently not published on Conda

## `✨` Example
Example of using Speedtest.py

```python
from speedtest import Client
import asyncio

client = Client(
  executable="speedtest"  # Only needs changing on Windows or Linux installs that have a different executable/command name.
)

async def app():
  result = await client.test()

  print("Bandwidth: " + str(result.download.bandwidth))


asyncio.run(app())
```

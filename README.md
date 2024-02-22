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
Examples of using Speedtest.py

### 1: Basic speedtest
```python
# Imports
from speedtest import Client
import asyncio

# Define the client
client = Client(
  executable="speedtest"  # Only needs changing on Windows or Linux installs that have a different executable/command name.
)

# Define app function
async def app():
  # Run a test with an automatically picked server
  result = await client.test()

  # Print statistics
  print(f"Download bandwidth:  {str(result.download.bandwidth) * 8 / 1_000_000:.2f} Mbps")
  print(f"Upload bandwidth:  {str(result.upload.bandwidth) * 8 / 1_000_000:.2f} Mbps")


asyncio.run(app())
```

### 2: Speedtest with selected server
```python
# Imports
from speedtest import Client
import asyncio

# Define the client
client = Client(
  executable="speedtest"  # Only needs changing on Windows or Linux installs that have a different executable/command name.
)

# Define app function
async def app():
  # Get a list of nearby servers
  servers = await client.servers()

  # Run a test with the first server
  result = await client.test(server=servers[0])

  # Print statistics
  print(f"Download bandwidth:  {str(result.download.bandwidth) * 8 / 1_000_000:.2f} Mbps")
  print(f"Upload bandwidth:  {str(result.upload.bandwidth) * 8 / 1_000_000:.2f} Mbps")


asyncio.run(app())
```

## `📈` Star History
<a href="https://star-history.com/#notaussie/speedtest.py&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=notaussie/speedtest.py&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=notaussie/speedtest.py&type=Date" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=notaussie/speedtest.py&type=Date" />
  </picture>
</a>

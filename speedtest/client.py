import asyncio
from asyncio import subprocess
from typing import List
import json
from .classes import Server
from .errors import *


class Client:
    def __init__(self, executable: str) -> None:
        self.executable = executable

    async def run(self, inputs: List[str]) -> dict:
        """Runs a CLI command and then parses the output into either a JSON object or an error"""

        # Add the format arg
        inputs.append("-f")
        inputs.append("json")

        # Create and run the process
        process: subprocess.Process = await asyncio.create_subprocess_exec(
            self.executable,
            *inputs,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        await process.wait()

        stdout, stderr = await process.communicate()

        # If there is an error (exit code ~= 0)
        if process.returncode != 0:
            # Decode the STDERR and get the final line (the JSON contents)
            errLines = stderr.decode()
            err = errLines.split("\n")[0]

            # If the final line isn't empty
            if err != "":
                errObj = json.loads(err)
                print(
                    json.dumps(errObj, indent=4)
                )  # Used until we create error processer
                return

            raise genericError

        # Else decode the STDOUT and parse it to JSON
        outputLines = stdout.decode()
        output = json.loads(outputLines.split("\n")[0])

        # Return JSON object
        return output

    async def servers(self) -> List[Server]:
        """Returns a list of nearby servers"""

        result = await self.run(["-L"])
        if result["type"] == "serverList":
            output = []
            for server in result["servers"]:
                output.append(Server(server))

            return output

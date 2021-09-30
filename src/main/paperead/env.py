from dataclasses import dataclass, field
import pathlib
from typing import Optional
import configparser
from .repository.materials import MaterialRepository


@dataclass
class ServerConfig:
    port: int = 3649
    dist: str = "./dist"


class Environment:
    def __init__(self, path: pathlib.Path) -> None:
        self.setPath(path)

    def setPath(self, path: pathlib.Path) -> None:
        self.path = path
        self.repo = MaterialRepository(path)

        self.configPath = self.path.joinpath("paperead.ini")
        self.serverConfig = ServerConfig()

        if self.configPath.exists() and self.configPath.is_file():
            config = configparser.ConfigParser()
            config.read_string(self.configPath.read_text(encoding="utf-8"))

            sections = config.sections()

            if "server" in sections:
                dic = {key: value for key, value in config.items("server")}
                self.serverConfig = ServerConfig(
                    port=int(dic.get("port", "3649")), dist=dic.get("dist", "./dist"))


env: Environment = Environment(pathlib.Path("."))

if __name__ == "__main__":
    env.setPath(pathlib.Path(
        __file__).parent.parent.parent.parent.joinpath("temp/materials"))
    print(env.serverConfig)

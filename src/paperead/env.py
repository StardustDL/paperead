from dataclasses import dataclass, field, asdict
import pathlib
from typing import Optional
from .repository.materials import MaterialRepository
import yaml

DEFAULT_SERVER_PORT = 3649
DEFAULT_BUILD_DIST = "./dist"
DEFAULT_BUILD_HOST = "empty"


@dataclass
class SiteConfig:
    title: str = ""
    subtitle: str = ""
    description: str = ""


@dataclass
class ServerConfig:
    port: int = DEFAULT_SERVER_PORT
    auth: str = ""
    readonly: bool = False
    dynamicTimeout: float = 60.0


@dataclass
class BuildConfig:
    dist: str = DEFAULT_BUILD_DIST
    host: str = DEFAULT_BUILD_HOST


class Environment:
    def __init__(self, path: pathlib.Path) -> None:
        self.setPath(path)

    def setPath(self, path: pathlib.Path) -> None:
        self.path = path
        self.repo = MaterialRepository(path)

        self.configPath = self.path.joinpath(".paperead.yml")
        self.serverConfig = ServerConfig()
        self.buildConfig = BuildConfig()
        self.siteConfig = SiteConfig()

        if self.configPath.exists() and self.configPath.is_file():
            text = self.configPath.read_text(encoding="utf-8")
            raw = yaml.safe_load(text)

            if "server" in raw:
                self.serverConfig = ServerConfig(**raw["server"])
            if "build" in raw:
                self.buildConfig = BuildConfig(**raw["build"])
            if "site" in raw:
                self.siteConfig = SiteConfig(**raw["site"])

    def generateConfigFile(self):
        self.configPath.write_text(yaml.safe_dump({
            "server": asdict(ServerConfig()),
            "build": asdict(BuildConfig()),
            "site": asdict(SiteConfig())
        }))


env: Environment = Environment(pathlib.Path("."))

if __name__ == "__main__":
    env.setPath(pathlib.Path(
        __file__).parent.parent.parent.parent.joinpath("temp/materials"))
    print(env.serverConfig)

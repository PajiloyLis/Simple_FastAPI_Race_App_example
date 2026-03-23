from abc import ABC, abstractmethod
from contextlib import contextmanager, AbstractContextManager
from typing import Callable, Generator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker


from Core.Common.Singleton import SingletonMeta


class Database(metaclass=SingletonMeta):
    def __init__(self):
        self.__engine = None
        self.__session_factory = None
        self.__is_connected = False

    async def connect(self, db_url: str, echo: bool = False):
        if self.__is_connected:
            return

        self.__engine = create_async_engine(
            db_url,
            echo=echo,
            future=True,
            pool_size=10,
            max_overflow=20,
            pool_pre_ping=True
        )

        self.__session_factory = async_sessionmaker(
            self.__engine,
            class_=AsyncSession,
            expire_on_commit=False,
            autoflush=False
        )

        self.__is_connected = True

    async def disconnect(self):
        if self.__engine:
            await self.__engine.dispose()
            self.__engine = None
            self.__session_factory = None
            self.__is_connected = False

    def get_session(self) -> AsyncSession:
        if not self.__is_connected:
            raise RuntimeError("Database is not connected. Call connect() first.")
        return self.__session_factory()

    @property
    def is_connected(self) -> bool:
        return self.__is_connected



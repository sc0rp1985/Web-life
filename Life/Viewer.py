from abc import ABC, abstractmethod


class AbstractViewer(ABC):
    @abstractmethod
    def show_world(self, world, fix_window, legend):
        pass

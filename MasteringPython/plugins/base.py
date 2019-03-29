import abc
import importlib


class Plugins(abc.ABCMeta):
    plugins = dict()

    def __new__(mcs, name, bases, namespace):
        cls = abc.ABCMeta.__new__(
            mcs, name, bases, namespace
        )
        if isinstance(cls.name, str):
            mcs.plugins[cls.name] = cls
        return cls

    @classmethod
    def get(mcs, name):
        if name not in mcs.plugins:
            print('Loading plugins from plugins.%s' % name)
            importlib.import_module('plugins.%s' % name)
        return mcs.plugins[name]

    @classmethod
    def load_directory(cls, module, directory):
        for file_ in os.listdir(directory):
            name, ext = os.path.splitext(file_)
            full_path = os.path.join(directory, file_)
            import_path = [module]
            if os.path.isdir(full_path):
                import_path.append(file_)
            elif ext == '.py' and MODULE_NAME_RE.match(name):
                import_path.append(name)
            else:
                # Ignoring non-matching files/directories
                continue
        plugin = importlib.import_module('.'.join(import_path))


        @classmethod
        def load(cls, **plugin_directories):
            for module, directory in plugin_directories.items():
                cls.load_directory(module, directory)

class Plugin(metaclass=Plugins):
    @property
    @abc.abstractmethod
    def name(self):
        raise NotImplemented()

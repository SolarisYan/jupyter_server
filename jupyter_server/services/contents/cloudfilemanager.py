import os
from traitlets import Any, Unicode, Bool, TraitError, observe, default, validate
from jupyter_server.services.contents.filemanager import FileContentsManager # ,AsyncFileContentsManager


class CloudFileManager(FileContentsManager):
    """Handle cloud file """
    root_dir = Unicode(config=True)

    @default('root_dir')
    def _default_root_dir(self):
        return os.getenv("DATA_PATH") or "/data"
        # try:
        #     return self.parent.notebook_dir
        # except AttributeError:
        #     return getcwd()
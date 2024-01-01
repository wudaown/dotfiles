#!/usr/bin/env python3

import os
import shutil
import logging
# from pathlib import Path

maps = [ x.replace("\n", "") for x in open('.map').readlines()]
logger = logging.getLogger(__name__)
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

HOME = os.path.expanduser('~')
DIR = os.getcwd()

# HOME = Path.home()
for m in maps:
    src, dest = m.split()
    dest = os.path.join(HOME, dest)
    if os.path.exists(dest):
        if os.path.isfile(dest):
            os.remove(dest)
            logger.info(f"remove file/symlink {dest}")
        elif os.path.isdir(dest):
            try:
                shutil.rmtree(dest)
                logger.info(f"remove directory {dest}")
            except OSError:
                os.unlink(dest)
                logger.info(f"remove symlink {dest}")
    else:
        logger.warning(f"{dest} does not exist")

    src = os.path.join(DIR, src)
    os.symlink(src, dest)
    logger.info(f"created symlink {dest}")

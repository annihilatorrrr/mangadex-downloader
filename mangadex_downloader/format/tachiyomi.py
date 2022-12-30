# MIT License

# Copyright (c) 2022 Rahman Yusuf

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import logging
import os
from .raw import Raw
from .comic_book import ComicBookArchive
from .utils import write_tachiyomi_details

log = logging.getLogger(__name__)

class _TachiyomiFormatBase:
    def write_details(self):
        # Write details.json for tachiyomi local manga
        details_path = self.path / 'details.json'
        log.info('Writing details.json')
        write_tachiyomi_details(self.manga, details_path)
    
    def main(self):
        self.write_details()
        super().main()

class Tachiyomi(_TachiyomiFormatBase, Raw):
    pass

class TachiyomiZip(_TachiyomiFormatBase, ComicBookArchive):
    pass